import re

_LOGGER = None

# A set of hard-coded keys if you want to limit to just a few instead of taking
# all information provided in GEO. Use with `--use-key-subset`
ANNOTATION_SHEET_KEYS = [
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
PROJECT_PATTERN = re.compile(r"(SRP\d{4,8})")
EXPERIMENT_PATTERN = re.compile(r"(SRX\d{4,8})")
GSE_PATTERN = re.compile(r"(GSE\d{4,8})")
SUPP_FILE_PATTERN = re.compile("Sample_supplementary_file")
SER_SUPP_FILE_PATTERN = re.compile("Series_supplementary_file")

SAMPLE_SUPP_METADATA_FILE = "_samples.csv"
EXP_SUPP_METADATA_FILE = "_series.csv"
FILE_RAW_NAME_SAMPLE_PATTERN = "_raw.csv"
FILE_RAW_NAME_SUBSAMPLE_PATTERN = "_raw_subtable.csv"

# How many times should we retry failing prefetch call?
NUM_RETRIES = 3
REQUEST_SLEEP = 0.4

NCBI_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=sra&term={SRP_NUMBER}&retmax=999&rettype=uilist&retmode=json"
NCBI_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=sra&id={ID}&rettype=runinfo&retmode=xml"

NEW_GENOME_COL_NAME = "ref_genome"

CONFIG_PROCESSED_TEMPLATE_NAME = "config_processed_template.yaml"
CONFIG_RAW_TEMPLATE_NAME = "config_template.yaml"
CONFIG_SRA_TEMPLATE = "looper_sra_convert.yaml"

# const for Finder:
RETMAX = 10000000  # once it should be increased

# gds = geo DataSets
ETOOLS_GEO_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds"
ETOOLS_GEO_GSE_BASE = f"{ETOOLS_GEO_BASE}&term=GSE[ETYP]"

ETOOLS_ENDING = "&retmax={retmax}&usehistory=y"

TODAY_DATE = "3000"

DATE_FILTER = (
    '+AND+("{start_date}"[Publication%20Date]%20:%20"{end_date}"[Publication%20Date])'
)
THREE_MONTH_FILTER = '+AND+"published+last+3+months"[Filter]'
