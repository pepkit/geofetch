"""Package constants."""

import re

_LOGGER = None

# A set of hard-coded keys if you want to limit to just a few instead of taking
# all information provided in GEO. Use with `--use-key-subset`
ANNOTATION_SHEET_KEYS: list[str] = [
    "sample_name",
    "protocol",
    "read_type",
    "organism",
    "data_source",
    "Sample_title",
    "Sample_source_name_ch1",
    "Sample_organism_ch1",
    "Sample_library_selection",
    "Sample_library_strategy",
    "Sample_type",
    "SRR",
    "SRX",
    "Sample_geo_accession",
    "Sample_series_id",
    "Sample_instrument_model",
]

# Regex to parse out SRA accession identifiers
PROJECT_PATTERN: re.Pattern[str] = re.compile(r"(SRP\d{4,8})")
EXPERIMENT_PATTERN: re.Pattern[str] = re.compile(r"(SRX\d{4,8})")
GSE_PATTERN: re.Pattern[str] = re.compile(r"(GSE\d{4,8})")
SUPP_FILE_PATTERN: re.Pattern[str] = re.compile("Sample_supplementary_file")
SER_SUPP_FILE_PATTERN: re.Pattern[str] = re.compile("Series_supplementary_file")

SAMPLE_SUPP_METADATA_FILE: str = "_samples.csv"
EXP_SUPP_METADATA_FILE: str = "_series.csv"
FILE_RAW_NAME_SAMPLE_PATTERN: str = "_raw.csv"
FILE_RAW_NAME_SUBSAMPLE_PATTERN: str = "_raw_subtable.csv"

# How many times should we retry failing prefetch call?
NUM_RETRIES: int = 3
REQUEST_SLEEP: float = 0.4

NCBI_ESEARCH: str = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=sra&term={SRP_NUMBER}&retmax=999&rettype=uilist&retmode=json"
NCBI_EFETCH: str = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=sra&id={ID}&rettype=runinfo&retmode=xml"

NEW_GENOME_COL_NAME: str = "ref_genome"

TEMPLATES_DIR: str = "templates"
CONFIG_PROCESSED_TEMPLATE_NAME: str = "config_processed_template.yaml"
CONFIG_RAW_TEMPLATE_NAME: str = "config_template.yaml"
CONFIG_SRA_TEMPLATE_NAME: str = "looper_sra_convert.yaml"
PIPELINE_INTERFACE_CONVERT_TEMPLATE_NAME: str = "pipeline_interface_convert.yaml"
LOOPER_SRA_CONVERT: str = "looper_config_template.yaml"

# const for Finder:
RETMAX: int = 10000000

# gds = geo DataSets
ETOOLS_GEO_BASE: str = (
    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds"
)
ETOOLS_GEO_GSE_BASE: str = f"{ETOOLS_GEO_BASE}&term=GSE[ETYP]"

ETOOLS_ENDING: str = "&retmax={retmax}&usehistory=y"

TODAY_DATE: str = "3000"

DATE_FILTER: str = (
    '+AND+("{start_date}"[Publication%20Date]%20:%20"{end_date}"[Publication%20Date])'
)
THREE_MONTH_FILTER: str = '+AND+"published+last+3+months"[Filter]'

LOOPER_CONFIG_FILE_NAME: str = "looper_config.yaml"
