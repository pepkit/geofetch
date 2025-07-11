import argparse
import os

import logmuse
from ubiquerg import VersionInHelpParser

from geofetch._version import __version__


def _safe_echo(var):
    """Returns an environment variable if it exists, or an empty string if not"""
    return os.getenv(var, "")


def _parse_cmdl(cmdl):
    """
    parser
    """
    parser = VersionInHelpParser(
        description="Automatic GEO and SRA data downloader",
        usage="""geofetch [<args>]

The example how to use geofetch (to download GSE573030 just metadata):
    geofetch -i GSE67303 -m <folder> --just-metadata

To download all processed data of GSE57303:
    geofetch -i GSE67303 --processed --geo-folder <folder> -m <folder>

""",
        version=__version__,
    )

    processed_group = parser.add_argument_group("processed")
    raw_group = parser.add_argument_group("raw")

    # Required
    parser.add_argument(
        "-i",
        "--input",
        dest="input",
        required=True,
        help="required: a GEO (GSE) accession, or a file with a list of GSE numbers",
    )

    # Optional
    parser.add_argument(
        "-n", "--name", help="Specify a project name. Defaults to GSE number"
    )

    parser.add_argument(
        "-m",
        "--metadata-root",
        dest="metadata_root",
        default=_safe_echo("SRAMETA"),
        help="Specify a parent folder location to store metadata. "
        "The project name will be added as a subfolder "
        "[Default: $SRAMETA:" + _safe_echo("SRAMETA") + "]",
    )

    parser.add_argument(
        "-u",
        "--metadata-folder",
        help="Specify an absolute folder location to store metadata. "
        "No subfolder will be added. Overrides value of --metadata-root.",
    )

    parser.add_argument(
        "--just-metadata",
        action="store_true",
        help="If set, don't actually run downloads, just create metadata",
    )

    parser.add_argument(
        "-r",
        "--refresh-metadata",
        action="store_true",
        help="If set, re-download metadata even if it exists.",
    )

    parser.add_argument(
        "--config-template", default=None, help="Project config yaml file template."
    )

    # Optional
    parser.add_argument(
        "--pipeline-samples",
        default=None,
        help="Optional: Specify one or more filepaths to SAMPLES pipeline interface yaml files. "
        "These will be added to the project config file to make it immediately "
        "compatible with looper. [Default: null]",
    )

    # Optional
    parser.add_argument(
        "--pipeline-project",
        default=None,
        help="Optional: Specify one or more filepaths to PROJECT pipeline interface yaml files. "
        "These will be added to the project config file to make it immediately "
        "compatible with looper. [Default: null]",
    )
    # Optional
    parser.add_argument(
        "--disable-progressbar",
        action="store_true",
        help="Optional: Disable progressbar",
    )

    # Optional
    parser.add_argument(
        "-k",
        "--skip",
        default=0,
        type=int,
        help="Skip some accessions. [Default: no skip].",
    )

    parser.add_argument(
        "--acc-anno",
        action="store_true",
        help="Optional: Produce annotation sheets for each accession."
        " Project combined PEP for the whole project won't be produced.",
    )

    parser.add_argument(
        "--discard-soft",
        action="store_true",
        help="Optional: After creation of PEP files, all .soft files will be deleted",
    )

    parser.add_argument(
        "--const-limit-project",
        type=int,
        default=50,
        help="Optional: Limit of the number of the constant sample characters "
        "that should not be in project yaml. [Default: 50]",
    )

    parser.add_argument(
        "--const-limit-discard",
        type=int,
        default=1000,
        help="Optional: Limit of the number of the constant sample characters "
        "that should not be discarded [Default: 250]",
    )

    parser.add_argument(
        "--attr-limit-truncate",
        type=int,
        default=500,
        help="Optional: Limit of the number of sample characters."
        "Any attribute with more than X characters will truncate to the first X,"
        " where X is a number of characters [Default: 500]",
    )

    parser.add_argument(
        "--add-dotfile",
        action="store_true",
        help="Optional: Add .pep.yaml file that points .yaml PEP file",
    )

    parser.add_argument(
        "--max-soft-size",
        type=str,
        default="1GB",
        help="""Optional: Max size of soft file.
                [Default: 1GB].
                Supported input formats : 12B, 12KB, 12MB, 12GB. """,
    )

    parser.add_argument(
        "--max-prefetch-size",
        help="Argument to pass to prefetch program's --max-size option, if prefetch will be used in this run of geofetch; "
        "for reference: https://github.com/ncbi/sra-tools/wiki/08.-prefetch-and-fasterq-dump#check-the-maximum-size-limit-of-the-prefetch-tool",
    )

    processed_group.add_argument(
        "-p",
        "--processed",
        default=False,
        action="store_true",
        help="Download processed data [Default: download raw data].",
    )

    processed_group.add_argument(
        "--data-source",
        dest="data_source",
        choices=["all", "samples", "series"],
        default="samples",
        help="Optional: Specifies the source of data on the GEO record"
        " to retrieve processed data, which may be attached to the"
        " collective series entity, or to individual samples. "
        "Allowable values are: samples, series or both (all). "
        "Ignored unless 'processed' flag is set. [Default: samples]",
    )

    processed_group.add_argument(
        "--filter",
        default=None,
        help="Optional: Filter regex for processed filenames [Default: None]."
        "Ignored unless 'processed' flag is set.",
    )

    processed_group.add_argument(
        "--filter-size",
        dest="filter_size",
        default=None,
        help="""Optional: Filter size for processed files
                that are stored as sample repository [Default: None].
                Works only for sample data.
                Supported input formats : 12B, 12KB, 12MB, 12GB. 
                Ignored unless 'processed' flag is set.""",
    )

    processed_group.add_argument(
        "-g",
        "--geo-folder",
        default=_safe_echo("GEODATA"),
        help="Optional: Specify a location to store processed GEO files."
        " Ignored unless 'processed' flag is set."
        "[Default: $GEODATA:" + _safe_echo("GEODATA") + "]",
    )

    raw_group.add_argument(
        "-x",
        "--split-experiments",
        action="store_true",
        help="""Split SRR runs into individual samples. By default, SRX
            experiments with multiple SRR Runs will have a single entry in the
            annotation table, with each run as a separate row in the
            subannotation table. This setting instead treats each run as a
            separate sample""",
    )

    raw_group.add_argument(
        "-b",
        "--bam-folder",
        dest="bam_folder",
        default=_safe_echo("SRABAM"),
        help="""Optional: Specify folder of bam files. Geofetch will not
            download sra files when corresponding bam files already exist.
            [Default: $SRABAM:"""
        + _safe_echo("SRABAM")
        + "]",
    )

    raw_group.add_argument(
        "-f",
        "--fq-folder",
        dest="fq_folder",
        default=_safe_echo("SRAFQ"),
        help="""Optional: Specify folder of fastq files. Geofetch will not
            download sra files when corresponding fastq files already exist.
            [Default: $SRAFQ:"""
        + _safe_echo("SRAFQ")
        + "]",
    )

    # Deprecated; these are for bam conversion which now happens in sra_convert
    # it still works here but I hide it so people don't use it, because it's confusing.
    raw_group.add_argument(
        "-s",
        "--sra-folder",
        dest="sra_folder",
        default=_safe_echo("SRARAW"),
        help=argparse.SUPPRESS,
        # help="Optional: Specify a location to store sra files "
        #   "[Default: $SRARAW:" + safe_echo("SRARAW") + "]"
    )
    raw_group.add_argument(
        "--bam-conversion",
        action="store_true",
        # help="Turn on sequential bam conversion. Default: No conversion.",
        help=argparse.SUPPRESS,
    )

    raw_group.add_argument(
        "--picard-path",
        dest="picard_path",
        default=_safe_echo("PICARD"),
        # help="Specify a path to the picard jar, if you want to convert "
        # "fastq to bam [Default: $PICARD:" + safe_echo("PICARD") + "]",
        help=argparse.SUPPRESS,
    )

    raw_group.add_argument(
        "--use-key-subset",
        action="store_true",
        help="Use just the keys defined in this module when writing out metadata.",
    )

    raw_group.add_argument(
        "--add-convert-modifier",
        action="store_true",
        help="Add looper SRA convert modifier to config file.",
    )

    logmuse.add_logging_options(parser)
    return parser.parse_args(cmdl)
