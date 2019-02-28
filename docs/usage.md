# <img src="../img/geofetch_logo.svg" class="img-header">  usage reference

`geofetch` command-line usage instructions:



`geofetch --help`
```{console}
usage: geofetch [-h] -i INPUT [-n NAME] [-m METADATA_FOLDER] [-f]
                [--just-metadata] [-r] [--acc-anno] [--use-key-subset] [-x]
                [--config-template CONFIG_TEMPLATE] [-p] [-g GEO_FOLDER]
                [-b BAM_FOLDER] [-P PIPELINE_INTERFACES]

Automatic GEO SRA data downloader

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        required: a GEO (GSE) accession, or a file with a list
                        of GSE numbers
  -n NAME, --name NAME  Specify a project name. Defaults to GSE number
  -m METADATA_FOLDER, --metadata-folder METADATA_FOLDER
                        Specify a location to store metadata [Default:
                        $SRAMETA:]
  -f, --no-subfolder    Don't automatically put metadata into a subfolder
                        named with project name
  --just-metadata       If set, don't actually run downloads, just create
                        metadata
  -r, --refresh-metadata
                        If set, re-download metadata even if it exists.
  --acc-anno            Also produce annotation sheets for each accession, not
                        just for the whole project combined
  --use-key-subset      Use just the keys defined in this module when writing
                        out metadata.
  -x, --split-experiments
                        Split SRR runs into individual samples. By default,
                        SRX experiments with multiple SRR Runs will have a
                        single entry in the annotation table, with each run as
                        a separate row in the subannotation table. This
                        setting instead treats each run as a separate sample
  --config-template CONFIG_TEMPLATE
                        Project config yaml file template.
  -p, --processed       Download processed data [Default: download raw data].
  -g GEO_FOLDER, --geo-folder GEO_FOLDER
                        Optional: Specify a location to store processed GEO
                        files [Default: $GEODATA:]
  -b BAM_FOLDER, --bam-folder BAM_FOLDER
                        Optional: Specify folder of bam files. Geofetch will
                        not download sra files when corresponding bam files
                        already exist. [Default: $SRABAM:]
  -P PIPELINE_INTERFACES, --pipeline_interfaces PIPELINE_INTERFACES
                        Optional: Specify the filepath of a pipeline interface
                        yaml file. [Default: null]
```
