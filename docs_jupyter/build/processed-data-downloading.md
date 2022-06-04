jupyter:True
# geofetch tutorial for processed data

The [GSE185701 data set](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE185701) has about 355 Mb of processed data that contains 57 Supplementary files, so it's a quick download for a test case. Let's take a quick peek at the geofetch version:


```bash
geofetch -V
```

```.output
geofetch 0.8.0

```

To see your CLI options, invoke `geofetch -h`:


```bash
geofetch -h
```

```.output
usage: geofetch [-h] [-V] -i INPUT [-n NAME] [-m METADATA_ROOT]
                [-u METADATA_FOLDER] [--just-metadata] [-r]
                [--config-template CONFIG_TEMPLATE] [-P PIPELINE_INTERFACES]
                [-k SKIP] [--acc-anno] [--use-key-subset] [-p]
                [--data-source {all,samples,series}] [--filter FILTER]
                [--filter-size FILTER_SIZE] [-g GEO_FOLDER] [-x]
                [-b BAM_FOLDER] [-f FQ_FOLDER] [--silent] [--verbosity V]
                [--logdev]

Automatic GEO and SRA data downloader

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -i INPUT, --input INPUT
                        required: a GEO (GSE) accession, or a file with a list
                        of GSE numbers
  -n NAME, --name NAME  Specify a project name. Defaults to GSE number
  -m METADATA_ROOT, --metadata-root METADATA_ROOT
                        Specify a parent folder location to store metadata.
                        The project name will be added as a subfolder
                        [Default: $SRAMETA:]
  -u METADATA_FOLDER, --metadata-folder METADATA_FOLDER
                        Specify an absolute folder location to store metadata.
                        No subfolder will be added. Overrides value of
                        --metadata-root [Default: Not used (--metadata-root is
                        used by default)]
  --just-metadata       If set, don't actually run downloads, just create
                        metadata
  -r, --refresh-metadata
                        If set, re-download metadata even if it exists.
  --config-template CONFIG_TEMPLATE
                        Project config yaml file template.
  -P PIPELINE_INTERFACES, --pipeline_interfaces PIPELINE_INTERFACES
                        Optional: Specify one or more filepaths to pipeline
                        interface yaml files. These will be added to the
                        project config file to make it immediately compatible
                        with looper. [Default: null]
  -k SKIP, --skip SKIP  Skip some accessions. [Default: no skip].
  --acc-anno            Also produce annotation sheets for each accession, not
                        just for the whole project combined
  --use-key-subset      Use just the keys defined in this module when writing
                        out metadata.
  --silent              Silence logging. Overrides verbosity.
  --verbosity V         Set logging level (1-5 or logging module level name)
  --logdev              Expand content of logging message format.

processed:
  -p, --processed       Download processed data [Default: download raw data].
  --data-source {all,samples,series}
                        Optional: Specifies the source of data on the GEO
                        record to retrieve processed data, which may be
                        attached to the collective series entity, or to
                        individual samples. Allowable values are: samples,
                        series or both (all). Ignored unless 'processed' flag
                        is set. [Default: all]
  --filter FILTER       Optional: Filter regex for processed filenames
                        [Default: None].Ignored unless 'processed' flag is
                        set.
  --filter-size FILTER_SIZE
                        Optional: Filter size for processed files that are
                        stored as sample repository [Default: None]. Supported
                        input formats : 12B, 12KB, 12MB, 12GB. Ignored unless
                        'processed' flag is set.
  -g GEO_FOLDER, --geo-folder GEO_FOLDER
                        Optional: Specify a location to store processed GEO
                        files. Ignored unless 'processed' flag is
                        set.[Default: $GEODATA:]

raw:
  -x, --split-experiments
                        Split SRR runs into individual samples. By default,
                        SRX experiments with multiple SRR Runs will have a
                        single entry in the annotation table, with each run as
                        a separate row in the subannotation table. This
                        setting instead treats each run as a separate sample
  -b BAM_FOLDER, --bam-folder BAM_FOLDER
                        Optional: Specify folder of bam files. Geofetch will
                        not download sra files when corresponding bam files
                        already exist. [Default: $SRABAM:]
  -f FQ_FOLDER, --fq-folder FQ_FOLDER
                        Optional: Specify folder of fastq files. Geofetch will
                        not download sra files when corresponding fastq files
                        already exist. [Default: $SRAFQ:]

```

Calling geofetch will do 4 tasks: 

1. download all or filtered processed files from `GSE#####` into your geo folder.
2. download all metadata from GEO and store in your metadata folder.
2. produce a PEP-compatible sample table, `PROJECT_NAME_sample_processed.csv` and `PROJECT_NAME_series_processed.csv`, in your metadata folder.
3. produce a PEP-compatible project configuration file, `PROJECT_NAME_sample_processed.yaml` and `PROJECT_NAME_series_processed.yaml`, in your metadata folder.

Complete details about geofetch outputs is cataloged in the [metadata outputs reference](metadata_output.md).

## Download the data

First, create the metadata for processed data (by adding --processed and --just-metadata):


```bash
geofetch -i GSE185701 --processed -n bright_test --just-metadata
```

```.output
Metadata folder: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test
Trying GSE185701 (not a file) as accession...
Skipped 0 accessions. Starting now.
Processing accession 1 of 1: 'GSE185701'
--2022-03-10 11:32:18--  https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?targ=gse&acc=GSE185701&form=text&view=full
Resolving www.ncbi.nlm.nih.gov (www.ncbi.nlm.nih.gov)... 2607:f220:41e:4290::110, 130.14.29.110
Connecting to www.ncbi.nlm.nih.gov (www.ncbi.nlm.nih.gov)|2607:f220:41e:4290::110|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [geo/text]
Saving to: ‘/home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/GSE185701_GSE.soft’

/home/bnt4me/Virgin     [ <=>                ]   2.79K  --.-KB/s    in 0s      

2022-03-10 11:32:18 (262 MB/s) - ‘/home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/GSE185701_GSE.soft’ saved [2855]

--2022-03-10 11:32:18--  https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?targ=gsm&acc=GSE185701&form=text&view=full
Resolving www.ncbi.nlm.nih.gov (www.ncbi.nlm.nih.gov)... 2607:f220:41e:4290::110, 130.14.29.110
Connecting to www.ncbi.nlm.nih.gov (www.ncbi.nlm.nih.gov)|2607:f220:41e:4290::110|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [geo/text]
Saving to: ‘/home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/GSE185701_GSM.soft’

/home/bnt4me/Virgin     [  <=>               ]  39.51K   139KB/s    in 0.3s    

2022-03-10 11:32:19 (139 KB/s) - ‘/home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/GSE185701_GSM.soft’ saved [40454]


--2022-03-10 11:32:19--  ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE185nnn/GSE185701/suppl/filelist.txt
           => ‘/home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/GSE185701_file_list.txt’
Resolving ftp.ncbi.nlm.nih.gov (ftp.ncbi.nlm.nih.gov)... 2607:f220:41e:250::10, 2607:f220:41f:250::228, 130.14.250.11, ...
Connecting to ftp.ncbi.nlm.nih.gov (ftp.ncbi.nlm.nih.gov)|2607:f220:41e:250::10|:21... connected.
Logging in as anonymous ... Logged in!
==> SYST ... done.    ==> PWD ... done.
==> TYPE I ... done.  ==> CWD (1) /geo/series/GSE185nnn/GSE185701/suppl ... done.
==> SIZE filelist.txt ... 794
==> EPSV ... done.    ==> RETR filelist.txt ... done.
Length: 794 (unauthoritative)

filelist.txt        100%[===================>]     794  --.-KB/s    in 0.04s   

2022-03-10 11:32:20 (18.3 KB/s) - ‘/home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/GSE185701_file_list.txt’ saved [794]

0

Total number of processed SAMPLES files found is: 8
Total number of processed SERIES files found is: 1
Finished processing 1 accession(s)
Expanding metadata list...
Unifying and saving of metadata... 
File /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/bright_test_annotation_sample_processed.csv has been saved successfully
  Config file: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/bright_test_annotation_sample_processed.yaml
Unifying and saving of metadata... 
File /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/bright_test_annotation_series_processed.csv has been saved successfully
  Config file: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/bright_test_annotation_series_processed.yaml

```


```bash
ls bright_test
```

```.output
bright_test_annotation_sample_processed.csv   GSE185701_file_list.txt
bright_test_annotation_sample_processed.yaml  GSE185701_GSE.soft
bright_test_annotation_series_processed.csv   GSE185701_GSM.soft
bright_test_annotation_series_processed.yaml

```

The `.soft` files are the direct output from GEO, which contain all the metadata as stored by GEO, for both the experiment (`_GSE`) and for the individual samples (`_GSM`). Geofetch also produces a `csv` file with the SRA metadata. The filtered version (ending in `_filt`) would contain only the specified subset of the samples if we didn't request them all, but in this case, since we only gave an accession, it is identical to the complete file. Additionally, file_list.txt is downloaded, that contains information about size, type and creation date of all sample files.

Finally, there are the 2 files that make up the PEP: the `_config.yaml` file and the `_annotation.csv` file (for samples and series). Let's see what's in these files now.


```bash
cat bright_test/bright_test_annotation_sample_processed.yaml
```

```.output
pep_version: 2.0.0
project_name: bright_test
sample_table: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/bright_test_annotation_sample_processed.csv

sample_modifiers:
  append:
    output_file_path: FILES
  derive:
    attributes: [output_file_path]
    sources:
      FILES: /{SRA}/{sample_name}



```

There are two important things to note in his file: First, see in the PEP that `sample_table` points to the csv file produced by geofetch. Second: output_file_path is location of all the files.

Now let's look at the first 100 characters of the csv file:


```bash
cut -c -100 bright_test/bright_test_annotation_sample_processed.csv
```

```.output
GSE,Sample_title,Sample_geo_accession,Sample_status,Sample_submission_date,Sample_last_update_date,S
GSE185701,Huh7_siNC_H3K27ac,GSM5621756,Public on Mar 01 2022,Oct 12 2021,Mar 03 2022,SRA,1,Huh 7,Hom
GSE185701,Huh7_siNC_H3K27ac,GSM5621756,Public on Mar 01 2022,Oct 12 2021,Mar 03 2022,SRA,1,Huh 7,Hom
GSE185701,Huh7_siDHX37_H3K27ac,GSM5621758,Public on Mar 01 2022,Oct 12 2021,Mar 03 2022,SRA,1,Huh 7,
GSE185701,Huh7_siDHX37_H3K27ac,GSM5621758,Public on Mar 01 2022,Oct 12 2021,Mar 03 2022,SRA,1,Huh 7,
GSE185701,Huh7_DHX37,GSM5621760,Public on Mar 01 2022,Oct 12 2021,Mar 03 2022,SRA,1,Huh 7,Homo sapie
GSE185701,Huh7_DHX37,GSM5621760,Public on Mar 01 2022,Oct 12 2021,Mar 03 2022,SRA,1,Huh 7,Homo sapie
GSE185701,Huh7_PLRG1,GSM5621761,Public on Mar 01 2022,Oct 12 2021,Mar 03 2022,SRA,1,Huh 7,Homo sapie
GSE185701,Huh7_PLRG1,GSM5621761,Public on Mar 01 2022,Oct 12 2021,Mar 03 2022,SRA,1,Huh 7,Homo sapie

```

Now let's download the actual data. This time we will will be downloading data from the [GSE185701 data set](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE185701) .
Let's additionally add few arguments:
- _geo-folder_ (required) - path to the location where processed files have to be saved
- _filter_ argument, to download only _bed_ files  (--filter ".Bed.gz$") 
- _data-source_ argument, to download files only from sample location (--data-source samples)


```bash
geofetch -i GSE185701 --processed -n bright_test --filter ".bed.gz$" --data-source samples \
--geo-folder /home/bnt4me/Virginia/for_docs/geo
```

```.output
Metadata folder: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test
Trying GSE185701 (not a file) as accession...
Skipped 0 accessions. Starting now.
Processing accession 1 of 1: 'GSE185701'
Found previous GSE file: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/GSE185701_GSE.soft
Found previous GSM file: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/GSE185701_GSM.soft
File /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/GSE185701_file_list.txt exists.
Total number of processed SAMPLES files found is: 8
Total number of files after filter is: 4 
Total number of processed SERIES files found is: 1
Total number of files after filter is: 0 

--2022-03-10 11:35:36--  ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5621nnn/GSM5621756/suppl/GSM5621756_ChIPseq_Huh7_siNC_H3K27ac_summits.bed.gz
           => ‘/home/bnt4me/Virginia/for_docs/geo/GSE185701/GSM5621756_ChIPseq_Huh7_siNC_H3K27ac_summits.bed.gz’
Resolving ftp.ncbi.nlm.nih.gov (ftp.ncbi.nlm.nih.gov)... 2607:f220:41e:250::12, 2607:f220:41e:250::11, 165.112.9.228, ...
Connecting to ftp.ncbi.nlm.nih.gov (ftp.ncbi.nlm.nih.gov)|2607:f220:41e:250::12|:21... connected.
Logging in as anonymous ... Logged in!
==> SYST ... done.    ==> PWD ... done.
==> TYPE I ... done.  ==> CWD (1) /geo/samples/GSM5621nnn/GSM5621756/suppl ... done.
==> SIZE GSM5621756_ChIPseq_Huh7_siNC_H3K27ac_summits.bed.gz ... 785486
==> EPSV ... done.    ==> RETR GSM5621756_ChIPseq_Huh7_siNC_H3K27ac_summits.bed.gz ... done.
Length: 785486 (767K) (unauthoritative)

GSM5621756_ChIPseq_ 100%[===================>] 767.08K  1.90MB/s    in 0.4s    

2022-03-10 11:35:37 (1.90 MB/s) - ‘/home/bnt4me/Virginia/for_docs/geo/GSE185701/GSM5621756_ChIPseq_Huh7_siNC_H3K27ac_summits.bed.gz’ saved [785486]

0

File /home/bnt4me/Virginia/for_docs/geo/GSE185701/GSM5621756_ChIPseq_Huh7_siNC_H3K27ac_summits.bed.gz has been downloaded successfully

--2022-03-10 11:35:38--  ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5621nnn/GSM5621758/suppl/GSM5621758_ChIPseq_Huh7_siDHX37_H3K27ac_summits.bed.gz
           => ‘/home/bnt4me/Virginia/for_docs/geo/GSE185701/GSM5621758_ChIPseq_Huh7_siDHX37_H3K27ac_summits.bed.gz’
Resolving ftp.ncbi.nlm.nih.gov (ftp.ncbi.nlm.nih.gov)... 2607:f220:41e:250::11, 2607:f220:41e:250::12, 130.14.250.12, ...
Connecting to ftp.ncbi.nlm.nih.gov (ftp.ncbi.nlm.nih.gov)|2607:f220:41e:250::11|:21... connected.
Logging in as anonymous ... Logged in!
==> SYST ... done.    ==> PWD ... done.
==> TYPE I ... done.  ==> CWD (1) /geo/samples/GSM5621nnn/GSM5621758/suppl ... done.
==> SIZE GSM5621758_ChIPseq_Huh7_siDHX37_H3K27ac_summits.bed.gz ... 784432
==> EPSV ... done.    ==> RETR GSM5621758_ChIPseq_Huh7_siDHX37_H3K27ac_summits.bed.gz ... done.
Length: 784432 (766K) (unauthoritative)

GSM5621758_ChIPseq_ 100%[===================>] 766.05K  2.48MB/s    in 0.3s    

2022-03-10 11:35:39 (2.48 MB/s) - ‘/home/bnt4me/Virginia/for_docs/geo/GSE185701/GSM5621758_ChIPseq_Huh7_siDHX37_H3K27ac_summits.bed.gz’ saved [784432]

0

File /home/bnt4me/Virginia/for_docs/geo/GSE185701/GSM5621758_ChIPseq_Huh7_siDHX37_H3K27ac_summits.bed.gz has been downloaded successfully

--2022-03-10 11:35:39--  ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5621nnn/GSM5621760/suppl/GSM5621760_CUTTag_Huh7_DHX37_summits.bed.gz
           => ‘/home/bnt4me/Virginia/for_docs/geo/GSE185701/GSM5621760_CUTTag_Huh7_DHX37_summits.bed.gz’
Resolving ftp.ncbi.nlm.nih.gov (ftp.ncbi.nlm.nih.gov)... 2607:f220:41e:250::11, 2607:f220:41e:250::12, 130.14.250.12, ...
Connecting to ftp.ncbi.nlm.nih.gov (ftp.ncbi.nlm.nih.gov)|2607:f220:41e:250::11|:21... connected.
Logging in as anonymous ... Logged in!
==> SYST ... done.    ==> PWD ... done.
==> TYPE I ... done.  ==> CWD (1) /geo/samples/GSM5621nnn/GSM5621760/suppl ... done.
==> SIZE GSM5621760_CUTTag_Huh7_DHX37_summits.bed.gz ... 163441
==> EPSV ... done.    ==> RETR GSM5621760_CUTTag_Huh7_DHX37_summits.bed.gz ... done.
Length: 163441 (160K) (unauthoritative)

GSM5621760_CUTTag_H 100%[===================>] 159.61K   862KB/s    in 0.2s    

2022-03-10 11:35:40 (862 KB/s) - ‘/home/bnt4me/Virginia/for_docs/geo/GSE185701/GSM5621760_CUTTag_Huh7_DHX37_summits.bed.gz’ saved [163441]

0

File /home/bnt4me/Virginia/for_docs/geo/GSE185701/GSM5621760_CUTTag_Huh7_DHX37_summits.bed.gz has been downloaded successfully

--2022-03-10 11:35:41--  ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5621nnn/GSM5621761/suppl/GSM5621761_CUTTag_Huh7_PLRG1_summits.bed.gz
           => ‘/home/bnt4me/Virginia/for_docs/geo/GSE185701/GSM5621761_CUTTag_Huh7_PLRG1_summits.bed.gz’
Resolving ftp.ncbi.nlm.nih.gov (ftp.ncbi.nlm.nih.gov)... 2607:f220:41e:250::11, 2607:f220:41e:250::12, 130.14.250.12, ...
Connecting to ftp.ncbi.nlm.nih.gov (ftp.ncbi.nlm.nih.gov)|2607:f220:41e:250::11|:21... connected.
Logging in as anonymous ... Logged in!
==> SYST ... done.    ==> PWD ... done.
==> TYPE I ... done.  ==> CWD (1) /geo/samples/GSM5621nnn/GSM5621761/suppl ... done.
==> SIZE GSM5621761_CUTTag_Huh7_PLRG1_summits.bed.gz ... 117250
==> EPSV ... done.    ==> RETR GSM5621761_CUTTag_Huh7_PLRG1_summits.bed.gz ... done.
Length: 117250 (115K) (unauthoritative)

GSM5621761_CUTTag_H 100%[===================>] 114.50K   644KB/s    in 0.2s    

2022-03-10 11:35:41 (644 KB/s) - ‘/home/bnt4me/Virginia/for_docs/geo/GSE185701/GSM5621761_CUTTag_Huh7_PLRG1_summits.bed.gz’ saved [117250]

0

File /home/bnt4me/Virginia/for_docs/geo/GSE185701/GSM5621761_CUTTag_Huh7_PLRG1_summits.bed.gz has been downloaded successfully
Finished processing 1 accession(s)
Expanding metadata list...
Unifying and saving of metadata... 
File /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/bright_test_annotation_sample_processed.csv has been saved successfully
  Config file: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/bright_test_annotation_sample_processed.yaml

```

Now lets list the folder to see what data is there. And let's see what's in pep files now.


```bash
ls /home/bnt4me/Virginia/for_docs/geo/GSE185701
```

```.output
GSM5621756_ChIPseq_Huh7_siNC_H3K27ac_summits.bed.gz
GSM5621758_ChIPseq_Huh7_siDHX37_H3K27ac_summits.bed.gz
GSM5621760_CUTTag_Huh7_DHX37_summits.bed.gz
GSM5621761_CUTTag_Huh7_PLRG1_summits.bed.gz

```


```bash
cut -c -100 bright_test/bright_test_annotation_sample_processed.csv
```

```.output
GSE,Sample_title,Sample_geo_accession,Sample_status,Sample_submission_date,Sample_last_update_date,S
GSE185701,Huh7_siNC_H3K27ac,GSM5621756,Public on Mar 01 2022,Oct 12 2021,Mar 03 2022,SRA,1,Huh 7,Hom
GSE185701,Huh7_siDHX37_H3K27ac,GSM5621758,Public on Mar 01 2022,Oct 12 2021,Mar 03 2022,SRA,1,Huh 7,
GSE185701,Huh7_DHX37,GSM5621760,Public on Mar 01 2022,Oct 12 2021,Mar 03 2022,SRA,1,Huh 7,Homo sapie
GSE185701,Huh7_PLRG1,GSM5621761,Public on Mar 01 2022,Oct 12 2021,Mar 03 2022,SRA,1,Huh 7,Homo sapie

```


```bash
cat bright_test/bright_test_annotation_sample_processed.yaml
```

```.output
pep_version: 2.0.0
project_name: bright_test
sample_table: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/bright_test/bright_test_annotation_sample_processed.csv

sample_modifiers:
  append:
    output_file_path: FILES
  derive:
    attributes: [output_file_path]
    sources:
      FILES: /home/bnt4me/Virginia/for_docs/geo/{SRA}/{sample_name}



```

Now we have easy access to this data by using [peppy](http://peppy.databio.org/en/latest/) package in python or [pepr](https://code.databio.org/pepr/) in r in further analysis 
