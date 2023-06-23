""" Independently-importable utilities to circumvent true scripts. """

import logging
import os
import subprocess
import sys
import re
import requests
from io import StringIO
import csv
from typing import *

_LOGGER = logging.getLogger(__name__)

# This dict provides NCBI lookup URLs for different accession types. SRX
# identifiers can be used to grab metadata from SRA for a single sample, just as
# an SRP identifier is used to grab the same table for multiple samples, so
# these accessions are the same.
URL_BY_ACC = {
    "GSE": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?targ=gse&acc={ACCESSION}&form=text&view=full",
    "GSM": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?targ=gsm&acc={ACCESSION}&form=text&view=full",
}


def build_prefetch_command(
    run_id: str, prefetch_path: str = "prefetch", max_size: Union[str, int] = None
) -> List[str]:
    cmd = [prefetch_path, run_id]
    if max_size is not None:
        cmd.extend(["--max-size", str(max_size)])
    return cmd


def is_known_type(accn: str = None, typename: str = None):
    """
    Determine if the given accession is of a known type.

    :param str accn: accession of interest
    :param str typename: check this typename for known status rather
        than parsing an accession
    :return bool: whether the given accession is of a known type.
    :raise TypeError: if neither argument is provided or one/both are empty.
    """
    if not (accn or typename):
        raise TypeError("Specify either accession or accession typename")
    if typename:
        return isinstance(typename, str) and typename.upper() in URL_BY_ACC
    try:
        prefix, number = split_accn(accn)
        return prefix.upper() in URL_BY_ACC
    except:
        return False


def parse_accessions(input_arg, metadata_folder, just_metadata=False, max_size=None):
    """
    Create a list of GSE accessions, either from file or a single value.

    This will be a dict, with the GSE# as the key, and
    corresponding value is a list of GSM# specifying the samples we're
    interested in from that GSE#. An empty sample list means we should get all
    samples from that GSE#. This loop will create this dict.

    :param input_arg: Input argument (GSE, or file)
    :param str metadata_folder: path to folder for accession metadata
    :param bool just_metadata: whether to only process metadata, not the
        actual data associated with the accession
    :param str | int max_size: argument for prefetch command's --max-size option
    """

    acc_GSE_list = {}

    if not os.path.isfile(input_arg):
        _LOGGER.info("Trying {} (not a file) as accession...".format(input_arg))
        # No limits accepted on command line, so keep an empty list.
        if input_arg.startswith("SRP"):
            base, ext = os.path.splitext(input_arg)
            if ext:
                raise ValueError("SRP-like input must be an SRP accession")
            file_sra = os.path.join(metadata_folder, "SRA_{}.csv".format(input_arg))
            # Fetch and write the metadata for this SRP accession.
            Accession(input_arg).fetch_metadata(file_sra)
            if just_metadata:
                return
            # Read the Run identifiers to download.
            run_ids = []
            with open(file_sra, "r") as f:
                for l in f:
                    if l.startswith("SRR"):
                        r_id = l.split(",")[0]
                        run_ids.append(r_id)
            _LOGGER.info("{} run(s)".format(len(run_ids)))
            for r_id in run_ids:
                run_subprocess(build_prefetch_command(run_id=r_id, max_size=max_size))
            # Early return if we've just handled SRP accession directly.
            return
        else:
            acc_GSE = input_arg
            acc_GSE_list[acc_GSE] = {}
    else:
        _LOGGER.info("Accession list file found: {}".format(input_arg))

        # Read input file line by line.
        for line in open(input_arg, "r"):
            if (not line) or (line[0] in ["#", "\n", "\t"]):
                continue
            fields = [x.rstrip() for x in line.split("\t")]
            gse = fields[0]
            if not gse:
                continue

            gse = gse.rstrip()

            if len(fields) > 1:
                gsm = fields[1]

                if len(fields) > 2 and gsm != "":
                    # There must have been a limit (GSM specified)
                    # include a name if it doesn't already exist
                    sample_name = fields[2].rstrip().replace(" ", "_")
                else:
                    sample_name = gsm

                if gse in acc_GSE_list:  # GSE already has a GSM; add the next one
                    acc_GSE_list[gse][gsm] = sample_name
                else:
                    acc_GSE_list[gse] = {gsm: sample_name}
            else:
                # No GSM limit; use empty dict.
                acc_GSE_list[gse] = {}

    return acc_GSE_list


def parse_SOFT_line(l: str) -> dict:
    """
    Parse SOFT formatted line, returning a dictionary with the key-value pair.

    :param str l: A SOFT-formatted line to parse ( !key = value )
    :return dict[str, str]: A python Dict object representing the key-value.
    """
    elems = l[1:].split("=")
    return {elems[0].rstrip(): "=".join(elems[1:]).lstrip()}


class AccessionException(Exception):
    """Exceptional condition(s) dealing with accession number(s)."""

    def __init__(self, reason: str = ""):
        """
        Optionally provide explanation for exceptional condition.

        :param str reason: some context or perhaps just a value that
            could not be interpreted as an accession
        """
        super(AccessionException, self).__init__(reason)


class SoftFileException(Exception):
    """Exceptional condition(s) dealing with accession number(s)."""

    def __init__(self, reason: str = ""):
        """
        Optionally provide explanation for exceptional condition.

        :param str reason: some context or perhaps just a value that
            could not be interpreted as an accession
        """
        super(SoftFileException, self).__init__(reason)


class Accession(object):
    """Working with accession numbers."""

    _LOGGER = logging.getLogger("{}.{}".format(__name__, "Accession"))

    def __init__(self, accn, strict=True):
        """
        Create an instance with an accession and optionally a validation
        strictness flag.

        :param str accn: accession
        :param bool strict: strictness of the validation (whether to require
            that the accession type is known here)
        :raise AccessionException: if the given accession value isn't
            prefixed with three characters followed by an integer, or if
            strict validation is required and the accession type is unknown
        """
        typename, number = self._validate(accn)
        if strict and not is_known_type(accn):
            raise AccessionException(
                "Unknown accession type for '{}': '{}'; "
                "supported types: {}".format(accn, typename, URL_BY_ACC.keys())
            )
        self.accn = accn
        self.typename = typename.upper()

    def fetch_metadata(
        self,
        outpath: str = None,
        typename: str = None,
        clean: bool = False,
        max_soft_size: int = 1073741824,
    ) -> list:
        """
        Fetch the metadata associated with this accession.

        :param str typename: type indicating URL format, use type
            parsed at construction if unspecified
        :param str outpath: path to file to which to write output, optional
        :param bool clean: if true, files won't be saved
        :param int max_soft_size: max soft file size in bytes
        :return: list of lines in soft file
        """

        typename = (typename or self.typename).upper()
        if not is_known_type(typename=typename):
            raise self.accn_type_exception(self.accn, typename)

        url_base = URL_BY_ACC[typename.upper()]
        format_kwargs = {"ACCESSION": self.accn}
        try:
            full_url = url_base.format(**format_kwargs)
        except KeyError:
            _LOGGER.error(
                "Couldn't populate URL format '{}' with {}".format(
                    url_base, format_kwargs
                )
            )
            raise
        _LOGGER.debug("Fetching: '%s'", full_url)
        if typename == "GSM":
            # check size of the file
            check_head_url = f"https://ftp.ncbi.nlm.nih.gov/geo/series/{self.accn[:-3]}nnn/{self.accn}/soft/{self.accn}_family.soft.gz"

            try:
                head_response = requests.head(check_head_url)
                file_size = head_response.headers["Content-Length"]

                if int(file_size) > max_soft_size:
                    raise SoftFileException(
                        f"Error in file size. Soft file: {self.accn}_family.soft.gz."
                        f"File size: {file_size}. Max_size_set: {max_soft_size}"
                    )
            except KeyError as err:
                self._LOGGER.warning(
                    f"Error in checking size of soft file, continuing... {err}"
                )
            except SoftFileException as err:
                self._LOGGER.error(f"Soft file is too large. {err}")
                return []

        result = requests.get(full_url)

        if result.ok:
            result.encoding = "UTF-8"
            result_text = result.text
            result_list = result_text.replace("\r", "").split("\n")
            result_list = [elem for elem in result_list if len(elem) > 0]

        else:
            raise Exception(f"Error in requesting file: {full_url}")

        if outpath and not clean:
            # Ensure we have filepath and that needed directories exist.
            if not os.path.splitext(outpath)[1]:
                _LOGGER.debug("Looks like folder, not file: %s", outpath)
                dirpath = outpath
                filename = "{}.csv".format(self.accn)
                outpath = os.path.join(dirpath, filename)
            else:
                dirpath = os.path.dirname(outpath)
            if not os.path.exists(dirpath):
                _LOGGER.debug("Forging path to '%s'", dirpath)
                os.makedirs(dirpath)

            # save file:
            with open(outpath, "w") as f:
                f.write(result_text)

        return result_list

    @staticmethod
    def _validate(accn: str):
        """
        Determine if given value looks like an accession.
        :param str accn: ordinary accession identifier.
        :return: typename, number
        """
        typename, number = split_accn(accn)
        if len(typename) != 3:
            raise AccessionException(
                "Not a three-character accession prefix: '{}' ('{}')".format(
                    accn, typename
                )
            )
        try:
            number = int(number)
        except (TypeError, ValueError):
            raise AccessionException(
                "Not an integral accession number: '{}' ('{}')".format(accn, number)
            )
        return typename, number

    @staticmethod
    def accn_type_exception(accn: str, typename: str, include_known: bool = True):
        """
        Create an exception instance based on an accession and a
        parsed unknown typename.

        :param str accn: accession identifier from which unknown typename
            was parsed
        :param str typename: unknown typename that was parsed
        :param bool include_known: whether to include the known
            typenames in the exception message
        :return AccessionException: the exception instance
        """
        message = "Unknown accn type for '{}': '{}'".format(accn, typename)
        if include_known:
            message = "{}; known types: {}".format(message, URL_BY_ACC.keys())
        return AccessionException(message)


def split_accn(accn: str):
    """
    Split accession into prefix and number, leaving suffix as text
    and converting the type prefix to uppercase.

    :param str accn: ordinary accession identifier.
    :return str, str: prefix and integral suffix
    """
    typename, number_text = accn[:3], accn[3:]
    return typename.upper(), number_text


def convert_size(size_str: str) -> int:
    """
    Converting size, that was provided as string with suffix
    :param str size_str: size as string with suffix: gb, mb, kb or b
    :return int: size as int value in bytes
    """
    abbreviation_dict = {"gb": 1073741824, "mb": 1048576, "kb": 1024, "b": 1}
    supported_formats = r"(\dgb|\dmb|\db|\dkb)$"
    reg_number = r"^\d+"
    abbreviation = re.findall(supported_formats, size_str)
    size_numb = re.findall(reg_number, size_str)

    # check if list is empty
    if len(abbreviation) == 0:
        size_in_bytes = size_numb[0]
    else:
        abb = abbreviation[0][1:]
        size_in_bytes = int(size_numb[0]) * abbreviation_dict[abb]

    if not isinstance(size_in_bytes, int):
        raise ValueError(
            f"Incorrect type of file size was provided! You provided:'{size_str}'"
        )

    return size_in_bytes


def clean_soft_files(meta_dir: str):
    """
    Cleaning, deleting all soft files after downloading files
    and creating PEPs
    :param str meta_dir: Path to the metadata files
    """
    try:
        dir_files = os.listdir(meta_dir)

        for item in dir_files:
            if (
                item.endswith(".soft")
                or item.endswith("_file_list.txt")
                or item.endswith("SRA.csv")
                or item.endswith("SRA_filt.csv")
            ):
                os.remove(os.path.join(meta_dir, item))
    except FileNotFoundError:
        _LOGGER.debug("Can't clean soft files...folder doesn't exist")


def run_subprocess(*args, **kwargs):
    """Wrapper to gracefully start and stop a running subprocess"""
    p = subprocess.Popen(*args, **kwargs)
    try:
        return p.wait()
    except KeyboardInterrupt:
        _LOGGER.info(f"Terminating subprocess: {p.pid} | ({p.args})")
        try:
            p.terminate()
            _LOGGER.info("Pipeline aborted.")
        except OSError as ose:
            _LOGGER.warning(f"Exception raised during subprocess termination: {ose}")
        sys.exit(1)


def _get_list_of_keys(list_of_dict: list):
    """
    Getting list of all keys that are in the dictionaries in the list

    :param list list_of_dict: list of dicts with metadata
    :return list: list of dictionary keys
    """

    dict_keys = {"sample_name": None}

    for sample in list_of_dict:
        for element in sample.keys():
            dict_keys[element] = None

    return list(dict_keys.keys())


def _get_value(all_line: str):
    """
    :param all_line: string with key value. (e.g. '!Series_geo_accession = GSE188720')
    :return: value (e.g. GSE188720)
    """
    line_value = all_line.split("= ")[-1]
    return line_value.split(": ")[-1].rstrip("\n")


def _read_tar_filelist(raw_text: str) -> dict:
    """
    Creating list for supplementary files that are listed in "filelist.txt"
    :param str raw_text: path to the file with information about files that are zipped ("filelist.txt")
    :return dict: dict of supplementary file names and additional information
    """
    f = StringIO(raw_text)
    files_info = {}
    csv_reader = csv.reader(f, delimiter="\t")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            name_index = row.index("Name")
            size_index = row.index("Size")
            type_index = row.index("Type")

            line_count += 1
        else:
            files_info[row[name_index]] = {
                "file_size": row[size_index],
                "type": row[type_index],
            }

    return files_info


def _check_file_existance(meta_processed_sample: list) -> list:
    """
    Checking if last element of the list has files. If list of files is empty deleting it
    :param: meta_processed_sample: list with metadata dictionary
    :return: list with metadata dictionary after processing
    """
    nb = len(meta_processed_sample) - 1
    if nb > -1:
        if len(meta_processed_sample[nb]["files"]) == 0:
            del meta_processed_sample[nb]
            nb -= 1
    return meta_processed_sample


def _separate_list_of_files(meta_list: Union[list, dict], col_name: str = "files"):
    """
    This method is separating list of files (dict value) or just simple dict
    into two different dicts
    :param col_name: column name that should be added with filenames
    :param meta_list: list, or dict with metadata
    """
    separated_list = []
    if isinstance(meta_list, list):
        for meta_elem in meta_list:
            for file_elem in meta_elem[col_name]:
                new_dict = meta_elem.copy()
                new_dict.pop(col_name, None)
                new_dict["file"] = file_elem
                separated_list.append(new_dict)
    elif isinstance(meta_list, dict):
        for file_elem in meta_list[col_name]:
            new_dict = meta_list.copy()
            new_dict.pop(col_name, None)
            new_dict["file"] = file_elem
            separated_list.append(new_dict)
    else:
        return TypeError("Incorrect type")

    return separated_list


def _update_columns(
    metadata: dict, experiment_name: str, sample_name: str, read_type: str
) -> dict:
    """
    Update the metadata associated with a particular experiment.

    For the experiment indicated, this function updates the value (mapping),
    including new data and populating columns used by looper based on
    existing values in the mapping.

    :param Mapping metadata: the key-value mapping to update
    :param str experiment_name: name of the experiment from which these
        data came and are associated; the key in the metadata mapping
        for which the value is to be updated
    :param str sample_name: name of the sample with which these data are
        associated
    :param str read_type: usually "single" or "paired," an indication of the
        type of sequencing reads for this experiment
    :return: updated metadata
    """

    exp = metadata[experiment_name]

    # Protocol-agnostic
    exp["sample_name"] = sample_name
    exp["protocol"] = exp["Sample_library_selection"]
    exp["read_type"] = read_type
    exp["organism"] = exp["Sample_organism_ch1"]
    exp["data_source"] = "SRA"
    exp["SRX"] = experiment_name

    # Protocol specified is lowercased prior to checking here to alleviate
    # dependence on case for the value in the annotations file.
    bisulfite_protocols = {"reduced representation": "RRBS", "random": "WGBS"}

    # Conditional on bisulfite sequencing
    # print(":" + exp["Sample_library_strategy"] + ":")
    # Try to be smart about some library methods, refining protocol if possible.
    if exp["Sample_library_strategy"] == "Bisulfite-Seq":
        # print("Parsing protocol")
        proto = exp["Sample_library_selection"].lower()
        if proto in bisulfite_protocols:
            exp["protocol"] = bisulfite_protocols[proto]

    return exp


def _sanitize_config_string(text: str) -> str:
    """
    Function that sanitizes text in config file.
    :param text: Any string that have to be sanitized
    :return: sanitized strings
    """
    new_str = text
    new_str = new_str.replace('"', f'\\"')
    new_str = new_str.replace("'", f"''")
    return new_str


def _sanitize_name(name_str: str) -> str:
    """
    Function that sanitizes strings. (Replace all odd characters)
    :param str name_str: Any string value that has to be sanitized.
    :return: sanitized strings
    """
    new_str = name_str
    punctuation1 = r"""!"#$%&'()*,./:;<=>?@[\]^_`{|}~"""
    for odd_char in list(punctuation1):
        new_str = new_str.replace(odd_char, "_")
    new_str = new_str.replace(" ", "_").replace("__", "_").lower()
    return new_str


def _create_dot_yaml(file_path: str, yaml_path: str) -> NoReturn:
    """
    Function that creates .pep.yaml file that points to actual yaml file
    :param str file_path: Path to the .pep.yaml file that we want to create
    :param str yaml_path: path or name of the actual yaml file
    """
    with open(file_path, "w+") as file:
        file.writelines(f"config_file: {yaml_path}")


def _which(program: str):
    """
    return str:  the path to a program to make sure it exists
    """
    import os

    def is_exe(fp):
        return os.path.isfile(fp) and os.access(fp, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file


def _dict_to_list_converter(
    proj_dict: Dict = None, proj_list: List = None
) -> Union[Dict, List]:
    """
    Converter project dict to list and vice versa
    dict -> list
    list -> dict
    :param proj_dict: project dictionary
    :param proj_list: project list
    :return: converted values
    """
    if proj_dict is not None:
        new_meta_list = []
        for key in proj_dict:
            new_dict = proj_dict[key]
            new_dict["big_key"] = key
            new_meta_list.append(new_dict)

        meta_list = new_meta_list

    elif proj_list is not None:
        new_sample_dict = {}
        for sample in proj_list:
            new_sample_dict[sample["big_key"]] = sample
        meta_list = new_sample_dict

    else:
        raise ValueError

    return meta_list


def _standardize_colnames(meta_list: Union[list, dict]) -> Union[list, dict]:
    """
    Standardize column names by lower-casing and underscore
    :param list meta_list: list of dictionaries of samples
    :return : list of dictionaries of samples with standard colnames
    """
    # check if meta_list is dict and converting it to list
    input_is_dict = False
    if isinstance(meta_list, dict):
        input_is_dict = True
        meta_list = _dict_to_list_converter(proj_dict=meta_list)

    new_metalist = []
    list_keys = _get_list_of_keys(meta_list)
    for item_nb, values in enumerate(meta_list):
        new_metalist.append({})
        for key in list_keys:
            try:
                new_key_name = key.lower().strip()
                new_key_name = _sanitize_name(new_key_name)

                new_metalist[item_nb][new_key_name] = values[key]

            except KeyError:
                pass

    if input_is_dict:
        new_metalist = _dict_to_list_converter(proj_list=new_metalist)

    return new_metalist


def _separate_file_url(meta_list):
    """
    This method is adding dict key without file_name without path
    """
    separated_list = []
    for meta_elem in meta_list:
        new_dict = meta_elem.copy()
        new_dict["file_url"] = meta_elem["file"]
        new_dict["file"] = os.path.basename(meta_elem["file"])
        # new_dict["sample_name"] = os.path.basename(meta_elem["file"])
        try:
            new_dict["sample_name"] = str(meta_elem["Sample_title"])
            if new_dict["sample_name"] == "" or new_dict["sample_name"] is None:
                raise KeyError("sample_name Does not exist. Creating .. ")
        except KeyError:
            new_dict["sample_name"] = os.path.basename(meta_elem["file"])

        # sanitize sample names
        sanit_name = _sanitize_name(new_dict["sample_name"])
        new_dict["sample_name"] = make_sample_name_unique(sanit_name, separated_list)

        separated_list.append(new_dict)
    return separated_list


def make_sample_name_unique(
    sanit_name: str, separated_list: list, new_number: int = 1
) -> str:
    """
    Check if name is unique for current sample
    """
    if sanit_name not in [f["sample_name"] for f in separated_list]:
        return sanit_name
    elif f"{sanit_name}_{new_number}" not in [f["sample_name"] for f in separated_list]:
        return f"{sanit_name}_{new_number}"
    else:
        return make_sample_name_unique(sanit_name, separated_list, new_number + 1)


def _filter_gsm(meta_processed_samples: list, gsm_list: dict) -> list:
    """
    Getting metadata list of all samples of one experiment and filtering it
    by the list of GSM that was specified in the input files.
    And then changing names of the sample names.

    :param meta_processed_samples: list of metadata dicts of samples
    :param gsm_list: list of dicts where GSM (samples) are keys and
        sample names are values. Where values can be empty string
    """

    if gsm_list.keys():
        new_gsm_list = []
        for gsm_sample in meta_processed_samples:
            if gsm_sample["Sample_geo_accession"] in gsm_list.keys():
                gsm_sample_new = gsm_sample
                if gsm_list[gsm_sample["Sample_geo_accession"]] != "":
                    gsm_sample_new["sample_name"] = gsm_list[
                        gsm_sample["Sample_geo_accession"]
                    ]
                new_gsm_list.append(gsm_sample_new)
        return new_gsm_list
    return meta_processed_samples


def _unify_list_keys(processed_meta_list: list) -> list:
    """
    Unifying list of dicts with metadata, so every dict will have
        same keys

    :param list processed_meta_list: list of dicts with metadata
    :return list: list of unified dicts with metadata
    """
    list_of_keys = _get_list_of_keys(processed_meta_list)
    for k in list_of_keys:
        for list_elem in range(len(processed_meta_list)):
            if k not in processed_meta_list[list_elem]:
                processed_meta_list[list_elem][k] = ""
    return processed_meta_list


def gse_content_to_dict(gse_content: List[str]) -> Dict[str, dict]:
    """
    Unpack gse soft file to dict
    :param gse_content: list of strings of gse soft file
    :return: dict of gse content
    """
    gse_dict = {}
    for line in gse_content:
        if line.startswith("^"):
            pass
        elif line.startswith("!"):
            key_value = line.split(" = ")
            new_key = _sanitize_name(key_value[0][1:])
            new_value = _sanitize_config_string(" ".join(key_value[1:]))
            if new_key in gse_dict.keys():
                gse_dict[new_key] = f"{gse_dict[new_key]} + {new_value}"
            else:
                gse_dict[new_key] = new_value

    return {"experiment_metadata": gse_dict}
