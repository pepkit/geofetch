import os
import shutil

import peppy
import pytest

import geofetch
from geofetch import Geofetcher, utils
from geofetch.utils import parse_accessions

INPUT_ACC_FILE = "tests/test_files/input_acc.txt"
GSE_FILES = "tests/test_files/soft_files"
GSE_SOFT_NAME = "GSE.soft"
GSM_SOFT_NAME = "GSM.soft"


def get_soft_path(gse_numb, sample_len, series_len):
    """
    Function that creates parameters to
    run  test test_file_list
    """
    return (
        gse_numb,
        os.path.join(GSE_FILES, gse_numb, GSE_SOFT_NAME),
        os.path.join(GSE_FILES, gse_numb, GSM_SOFT_NAME),
        sample_len,
        series_len,
    )


# Soft files that are in the folder
processed_meta_file_test = [
    get_soft_path("GSE138657", 14, 0),
    get_soft_path("GSE146537", 6, 0),
    get_soft_path("GSE146539", 24, 0),
    get_soft_path("GSE146540", 0, 1),
    get_soft_path("GSE146583", 42, 0),
    get_soft_path("GSE150868", 35, 2),
]


def test_max_prefetch_size__default_is_50g():
    fetcher = Geofetcher()
    assert fetcher.max_prefetch_size == "50g"


class TestAccParser:
    """
    Testing input parser
    """

    def test_accessions(self):
        parser_data = parse_accessions("GSE12345", "")
        assert parser_data == {"GSE12345": {}}

    def test_accessions_file(self):
        actuall_data = {
            "GSE185701": {
                "GSM5621756": "Huh7_siNC_H3K27ac",
                "GSM5621758": "",
                "GSM5621760": "Huh7_DHX38",
                "GSM5621761": "",
            },
            "GSE201096": {},
        }

        parser_data = parse_accessions(INPUT_ACC_FILE, "")

        assert parser_data == actuall_data


class TestListProcessedMetaFiles:
    """
    Testing downloading and saving process soft files
    """

    @pytest.fixture(scope="function")
    def initiate_geofetcher(self, tmpdir):
        instance = Geofetcher(
            just_metadata=True,
            processed=True,
            name="test",
            metadata_folder=tmpdir,
            data_source="all",
        )
        yield instance

    @pytest.mark.parametrize(
        "gse_numb,soft_gse, soft_gsm, sample_len, series_len", processed_meta_file_test
    )
    def test_file_list(
        self, gse_numb, soft_gse, soft_gsm, sample_len, series_len, initiate_geofetcher
    ):
        file_gse_content = geofetch.utils.Accession(gse_numb).fetch_metadata(
            soft_gse, typename="GSE", clean=False
        )
        file_gsm_content = geofetch.utils.Accession(gse_numb).fetch_metadata(
            soft_gsm, typename="GSM", clean=False
        )
        (
            meta_processed_samples,
            meta_processed_series,
        ) = initiate_geofetcher._get_list_of_processed_files(
            file_gse_content, file_gsm_content
        )
        assert len(meta_processed_samples) == sample_len
        assert len(meta_processed_series) == series_len

    def test_downloading_soft_files(self, initiate_geofetcher):
        initiate_geofetcher.fetch_all("GSE138657")
        downloaded_meta_files = list(os.walk(initiate_geofetcher.metadata_expanded))[0][
            2
        ]

        assert "GSE138657_GSM.soft" in downloaded_meta_files
        assert "GSE138657_GSE.soft" in downloaded_meta_files

    def test_creating_sample_pep_files(self, initiate_geofetcher):
        gse_numb = "GSE138657"
        initiate_geofetcher.fetch_all(gse_numb)
        downloaded_meta_files = list(
            os.walk(initiate_geofetcher.metadata_expanded + f"/{gse_numb}_samples")
        )[0][2]

        assert f"{gse_numb}_samples.csv" in downloaded_meta_files
        assert f"{gse_numb}_samples.yaml" in downloaded_meta_files

    def test_creating_series_pep_files(self, initiate_geofetcher):
        gse_numb = "GSE199313"
        initiate_geofetcher.fetch_all(gse_numb)
        downloaded_meta_files = list(
            os.walk(initiate_geofetcher.metadata_expanded + f"/{gse_numb}_series")
        )[0][2]

        assert f"{gse_numb}_series.csv" in downloaded_meta_files
        assert f"{gse_numb}_series.yaml" in downloaded_meta_files


class TestListRawMetaFiles:
    """
    Testing downloading and saving raw files and metadata
    """

    @pytest.fixture(scope="function")
    def initiate_geofetcher(self, tmpdir):
        instance = Geofetcher(
            just_metadata=True,
            processed=False,
            name="test",
            metadata_folder=tmpdir,
            discard_soft=True,
        )
        yield instance

    def test_creating_series_pep_files(self, initiate_geofetcher):
        gse_numb = "GSE138656"
        initiate_geofetcher.fetch_all(gse_numb)
        downloaded_meta_files = list(
            os.walk(initiate_geofetcher.metadata_expanded + f"/{gse_numb}_PEP")
        )[0][2]

        assert f"{gse_numb}_PEP_raw.csv" in downloaded_meta_files
        assert f"{gse_numb}_PEP.yaml" in downloaded_meta_files
        assert f"{gse_numb}_PEP_raw_subtable.csv" in downloaded_meta_files


class TestDownloadingProcFiles:
    """
    Testing downloading processed files
    """

    @pytest.fixture(scope="function")
    def initiate_geofetcher(self, tmpdir):
        instance = Geofetcher(
            just_metadata=True, processed=True, name="test", metadata_folder=tmpdir
        )
        yield instance

    @pytest.mark.parametrize(
        "file_url, file_name",
        [
            (
                "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5025nnn/GSM5025270/suppl/GSM5025270_CBS-u2-KO-H3K4me3-ChIP-seq_peaks.bed.gz",
                "GSM5025270_CBS-u2-KO-H3K4me3-ChIP-seq_peaks.bed.gz",
            )
        ],
    )
    def test_downloading_files(self, file_url, file_name, tmpdir, initiate_geofetcher):
        initiate_geofetcher._download_processed_file(file_url, tmpdir)

        assert len(tmpdir.listdir()) == 1
        assert os.path.basename(tmpdir.listdir()[0]) == file_name


class TestFilters:
    """
    Testing file filters
    """

    @pytest.fixture(scope="function")
    def initiate_geofetcher(self, tmpdir):
        instance = Geofetcher(
            just_metadata=True,
            processed=True,
            name="test",
            metadata_folder=tmpdir,
            filter=r"\.Bed.gz$",
            filter_size="2MB",
        )
        yield instance

    @pytest.mark.parametrize(
        "meta_list, output",
        [
            (
                [
                    {"name": "dupa", "file": "dupa.bed.gz", "file_size": "3MB"},
                    {"name": "cycki", "file": "cycki.BED.gz", "file_size": "13KB"},
                    {"name": "ogon", "file": "ogon.xlx.gz", "file_size": "4B"},
                    {"name": "KROwa", "file": "muuu.BigBed.gz", "file_size": "2000KB"},
                ],
                [
                    {"name": "dupa", "file": "dupa.bed.gz", "file_size": "3MB"},
                    {"name": "cycki", "file": "cycki.BED.gz", "file_size": "13KB"},
                ],
            )
        ],
    )
    def test_filter(self, meta_list, output, initiate_geofetcher):
        result = initiate_geofetcher._run_filter(meta_list)
        assert result == output

    @pytest.mark.parametrize(
        "meta_list, output",
        [
            (
                [
                    {"name": "dupa", "file": "dupa.bed.gz", "file_size": 3000000},
                    {"name": "cycki", "file": "cycki.BED.gz", "file_size": 2203000},
                    {"name": "ogon", "file": "ogon.xlx.gz", "file_size": 1103000},
                    {"name": "KROwa", "file": "muuu.BigBed.gz", "file_size": 53000},
                ],
                [
                    {"name": "ogon", "file": "ogon.xlx.gz", "file_size": 1103000},
                    {"name": "KROwa", "file": "muuu.BigBed.gz", "file_size": 53000},
                ],
            )
        ],
    )
    def test_size_filter(self, meta_list, output, initiate_geofetcher):
        result = initiate_geofetcher._run_size_filter(meta_list)
        assert result == output

    @pytest.mark.parametrize(
        "init_meta_data,  result_sample, result_proj,",
        [
            (
                [
                    {
                        "name": "Antonio",
                        "number": 1,
                        "car": "Fiat",
                    },
                    {
                        "name": "Markus",
                        "number": 1,
                        "car": "Jeep",
                    },
                    {
                        "name": "Pablo",
                        "number": 1,
                        "car": "Jeep",
                    },
                ],
                [
                    {
                        "name": "Antonio",
                        "car": "Fiat",
                    },
                    {
                        "name": "Markus",
                        "car": "Jeep",
                    },
                    {
                        "name": "Pablo",
                        "car": "Jeep",
                    },
                ],
                [
                    {
                        "number": 1,
                    },
                ],
            )
        ],
    )
    def test_large_meta_separation(
        self, init_meta_data, result_sample, result_proj, initiate_geofetcher
    ):
        samp, proj = initiate_geofetcher._separate_common_meta(
            init_meta_data, max_len=0
        )
        assert samp == result_sample
        assert proj == result_proj


class TestPeppyInitProcessed:
    """
    Testing downloading and saving raw files and metadata
    """

    @pytest.fixture(scope="function")
    def initiate_geofetcher(self, tmpdir):
        instance = Geofetcher(
            just_metadata=True,
            processed=True,
            name="test",
            metadata_folder=tmpdir,
            discard_soft=True,
            data_source="all",
        )
        yield instance

    def test_creating_processed_peppy(self, initiate_geofetcher):
        gse_numb = "GSE190287"
        p_prop = initiate_geofetcher.get_projects(gse_numb)
        assert isinstance(p_prop[f"{gse_numb}_samples"], peppy.Project)
        assert isinstance(p_prop[f"{gse_numb}_series"], peppy.Project)

    def test_number_of_samples(self, initiate_geofetcher):
        gse_numb = "GSE190287"
        p_prop = initiate_geofetcher.get_projects(gse_numb)
        assert (
            len(p_prop[f"{gse_numb}_samples"].samples) == 11
        )  # it has 11 files but 8 samples
        assert len(p_prop[f"{gse_numb}_series"].samples) == 2


class TestPeppyInitRaw:
    """
    Testing downloading and saving raw files and metadata
    """

    @pytest.fixture(scope="function")
    def initiate_geofetcher(self, tmpdir):
        instance = Geofetcher(
            just_metadata=True,
            processed=False,
            name="test",
            metadata_folder=tmpdir,
            discard_soft=True,
        )
        yield instance

    def test_creating_processed_peppy(self, initiate_geofetcher):
        gse_numb = "GSE189141"
        p_prop = initiate_geofetcher.get_projects(gse_numb)
        assert isinstance(p_prop[f"{gse_numb}_raw"], peppy.Project)

    def test_number_of_samples(self, initiate_geofetcher):
        gse_numb = "GSE189141"
        p_prop = initiate_geofetcher.get_projects(gse_numb)
        # a = [d["sample_name"] for d in p_prop[f"{gse_numb}_raw"].samples]
        assert len(p_prop[f"{gse_numb}_raw"].samples) == 16  # it has 16 samples

    def test_description_created_correctly_series(self, initiate_geofetcher):
        gse_numb = "GSE189141"
        p_prop = initiate_geofetcher.get_projects(gse_numb)
        peppy_obj = p_prop[f"{gse_numb}_raw"].to_dict(extended=True)
        assert peppy_obj["_config"]["description"] is not None

    def test_description_created_correctly_samples(self, initiate_geofetcher):
        gse_numb = "GSE189141"
        p_prop = initiate_geofetcher.get_projects(gse_numb)
        peppy_obj = p_prop[f"{gse_numb}_raw"].to_dict(extended=True)
        assert peppy_obj["_config"]["description"] is not None


def test_clean_func(tmpdir):
    """
    Testing deleting soft files
    """
    files_dir = os.path.join(GSE_FILES, "GSE138657")
    for file_name in os.listdir(files_dir):
        shutil.copyfile(
            os.path.join(files_dir, file_name), os.path.join(tmpdir, file_name)
        )
    utils.clean_soft_files(tmpdir)
