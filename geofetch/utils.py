""" Independently-importable utilities to circumvent true scripts. """

import logging
import os
import subprocess
import re


__author__ = [
    "Oleksandr Khoroshevskyi",
    "Vince Reuter",
    "Nathan Sheffield",
]
__email__ = "bnt4me@virginia.edu"

__all__ = ["parse_accessions"]


_LOGGER = logging.getLogger(__name__)


# This dict provides NCBI lookup URLs for different accession types. SRX
# identifiers can be used to grab metadata from SRA for a single sample, just as
# an SRP identifier is used to grab the same table for multiple samples, so
# these accessions are the same.
URL_BY_ACC = {
    "GSE": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?targ=gse&acc={ACCESSION}&form=text&view=full",
    "GSM": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?targ=gsm&acc={ACCESSION}&form=text&view=full",
    "SRP": "https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?save=efetch&db=sra&rettype=runinfo&term={ACCESSION}",
    "SRX": "https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?save=efetch&db=sra&rettype=runinfo&term={ACCESSION}",
}


def is_known_type(accn=None, typename=None):
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


def parse_accessions(input_arg, metadata_folder, just_metadata=False):
    """
    Create a list of GSE accessions, either from file or a single value.

    This will be a dict, with the GSE# as the key, and
    corresponding value is a list of GSM# specifying the samples we're
    interested in from that GSE#. An empty sample list means we should get all
    samples from that GSE#. This loop will create this dict.

    :param input_arg:
    :param str metadata_folder: path to folder for accession metadata
    :param bool just_metadata: whether to only process metadata, not the
        actual data associated with the accession
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
                subprocess.call(["prefetch", r_id, "--max-size", "50000000"])
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


def parse_SOFT_line(l):
    """
    Parse SOFT formatted line, returning a dictionary with the key-value pair.

    :param str l: A SOFT-formatted line to parse ( !key = value )
    :return dict[str, str]: A python Dict object representing the key-value.
    :raise InvalidSoftLineException: if given line can't be parsed as SOFT line
    """
    elems = l[1:].split("=")
    return {elems[0].rstrip(): elems[1].lstrip()}


class AccessionException(Exception):
    """Exceptional condition(s) dealing with accession number(s)."""

    def __init__(self, reason=""):
        """
        Optionally provide explanation for exceptional condition.

        :param str reason: some context or perhaps just a value that
            could not be interpreted as an accession
        """
        super(AccessionException, self).__init__(reason)


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

    def fetch_metadata(self, outpath=None, typename=None):
        """
        Fetch the metadata associated with this accession.

        :param str outpath: path to file to which to write output, optional
        :param str typename: type indicating URL format, use type
            parsed at construction if unspecified
        """

        # TODO: note this sort of type-dependent strategy suggests subclassing.
        # For now, class is small, but that should maybe be done if it grows.

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

        if outpath:
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
            cmd = "wget -O {} {}".format(outpath, full_url)
        else:
            cmd = "wget {}".format(full_url)

        subprocess.call(cmd.split(" "))

    @staticmethod
    def _validate(accn):
        """Determine if given value looks like an accession."""
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
    def accn_type_exception(accn, typename, include_known=True):
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


def split_accn(accn):
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

    return size_in_bytes


def clean_soft_files(meta_dir: str):
    """
    Cleaning, deleting all soft files after downloading files
    and creating PEPs
    :param str meta_dir: Path to the metadata files
    """
    dir_files = os.listdir(meta_dir)

    for item in dir_files:
        if item.endswith(".soft") \
                or item.endswith("_file_list.txt")\
                or item.endswith("SRA.csv")\
                or item.endswith("SRA_filt.csv"):
            os.remove(os.path.join(meta_dir, item))
