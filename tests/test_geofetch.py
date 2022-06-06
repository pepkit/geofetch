from geofetch import parse_accessions, Geofetcher, utils
import os
import pytest
import shutil

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
    Testing
    """

    @pytest.fixture(scope="function")
    def initiate_geofetcher(self, tmpdir):
        instance = Geofetcher(
            just_metadata=True, processed=True, name="test", metadata_folder=tmpdir
        )
        yield instance

    @pytest.mark.parametrize(
        "soft_gse, soft_gsm, sample_len, series_len", processed_meta_file_test
    )
    def test_file_list(
        self, soft_gse, soft_gsm, sample_len, series_len, initiate_geofetcher
    ):
        (
            meta_processed_samples,
            meta_processed_series,
        ) = initiate_geofetcher.get_list_of_processed_files(soft_gse, soft_gsm)
        assert len(meta_processed_samples) == sample_len
        assert len(meta_processed_series) == series_len

    def test_downloading_soft_files(self, initiate_geofetcher):
        initiate_geofetcher.fetch_all("GSE138657")
        downloaded_meta_files = list(os.walk(initiate_geofetcher.metadata_expanded))[0][
            2
        ]

        assert "GSE138657_GSM.soft" in downloaded_meta_files
        assert "GSE138657_GSE.soft" in downloaded_meta_files

    def test_creating_pep_files(self, initiate_geofetcher):
        initiate_geofetcher.fetch_all("GSE138657")
        downloaded_meta_files = list(os.walk(initiate_geofetcher.metadata_expanded))[0][
            2
        ]

        assert "GSE138657_samples.csv" in downloaded_meta_files
        assert "GSE138657_samples.yaml" in downloaded_meta_files


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
        initiate_geofetcher.download_processed_file(file_url, tmpdir)

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
            filter="\.Bed.gz$",
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
        result = initiate_geofetcher.run_filter(meta_list)
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
        result = initiate_geofetcher.run_size_filter(meta_list)
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
        samp, proj = initiate_geofetcher.separate_common_meta(init_meta_data, max_len=0)
        assert samp == result_sample
        assert proj == result_proj


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
