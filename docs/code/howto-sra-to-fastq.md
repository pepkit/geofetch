## How to extract fastq files from SRA

1. Install geofetch


```bash
pip install geofetch
```

    Defaulting to user installation because normal site-packages is not writeable
    Requirement already satisfied: geofetch in /home/bnt4me/.local/lib/python3.10/site-packages (0.12.7)
    Requirement already satisfied: colorama>=0.3.9 in /usr/lib/python3/dist-packages (from geofetch) (0.4.4)
    Requirement already satisfied: coloredlogs>=15.0.1 in /home/bnt4me/.local/lib/python3.10/site-packages (from geofetch) (15.0.1)
    Requirement already satisfied: logmuse>=0.2.6 in /home/bnt4me/.local/lib/python3.10/site-packages (from geofetch) (0.2.7)
    Requirement already satisfied: pandas>=1.5.3 in /home/bnt4me/.local/lib/python3.10/site-packages (from geofetch) (2.2.2)
    Requirement already satisfied: peppy>=0.40.6 in /home/bnt4me/.local/lib/python3.10/site-packages (from geofetch) (0.40.7)
    Requirement already satisfied: piper>=0.14.4 in /home/bnt4me/.local/lib/python3.10/site-packages (from geofetch) (0.14.4)
    Requirement already satisfied: requests>=2.28.1 in /home/bnt4me/.local/lib/python3.10/site-packages (from geofetch) (2.31.0)
    Requirement already satisfied: rich>=12.5.1 in /home/bnt4me/.local/lib/python3.10/site-packages (from geofetch) (13.7.1)
    Requirement already satisfied: ubiquerg>=0.6.2 in /home/bnt4me/.local/lib/python3.10/site-packages (from geofetch) (0.8.1)
    Requirement already satisfied: xmltodict>=0.13.0 in /home/bnt4me/.local/lib/python3.10/site-packages (from geofetch) (0.13.0)
    Requirement already satisfied: humanfriendly>=9.1 in /home/bnt4me/.local/lib/python3.10/site-packages (from coloredlogs>=15.0.1->geofetch) (10.0)
    Requirement already satisfied: numpy>=1.22.4 in /home/bnt4me/.local/lib/python3.10/site-packages (from pandas>=1.5.3->geofetch) (1.25.2)
    Requirement already satisfied: python-dateutil>=2.8.2 in /home/bnt4me/.local/lib/python3.10/site-packages (from pandas>=1.5.3->geofetch) (2.8.2)
    Requirement already satisfied: pytz>=2020.1 in /usr/lib/python3/dist-packages (from pandas>=1.5.3->geofetch) (2022.1)
    Requirement already satisfied: tzdata>=2022.7 in /home/bnt4me/.local/lib/python3.10/site-packages (from pandas>=1.5.3->geofetch) (2023.3)
    Requirement already satisfied: pyyaml in /usr/lib/python3/dist-packages (from peppy>=0.40.6->geofetch) (5.4.1)
    Requirement already satisfied: pephubclient>=0.4.2 in /home/bnt4me/.local/lib/python3.10/site-packages (from peppy>=0.40.6->geofetch) (0.4.2)
    Requirement already satisfied: psutil in /home/bnt4me/.local/lib/python3.10/site-packages (from piper>=0.14.4->geofetch) (5.9.4)
    Requirement already satisfied: yacman>=0.9.3 in /home/bnt4me/.local/lib/python3.10/site-packages (from piper>=0.14.4->geofetch) (0.9.3)
    Requirement already satisfied: pipestat>=0.11.0 in /home/bnt4me/.local/lib/python3.10/site-packages (from piper>=0.14.4->geofetch) (0.12.1)
    Requirement already satisfied: charset-normalizer<4,>=2 in /home/bnt4me/.local/lib/python3.10/site-packages (from requests>=2.28.1->geofetch) (3.0.1)
    Requirement already satisfied: idna<4,>=2.5 in /usr/lib/python3/dist-packages (from requests>=2.28.1->geofetch) (3.3)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /home/bnt4me/.local/lib/python3.10/site-packages (from requests>=2.28.1->geofetch) (1.26.18)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/lib/python3/dist-packages (from requests>=2.28.1->geofetch) (2020.6.20)
    Requirement already satisfied: markdown-it-py>=2.2.0 in /home/bnt4me/.local/lib/python3.10/site-packages (from rich>=12.5.1->geofetch) (3.0.0)
    Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /home/bnt4me/.local/lib/python3.10/site-packages (from rich>=12.5.1->geofetch) (2.17.2)
    Requirement already satisfied: mdurl~=0.1 in /home/bnt4me/.local/lib/python3.10/site-packages (from markdown-it-py>=2.2.0->rich>=12.5.1->geofetch) (0.1.2)
    Requirement already satisfied: typer>=0.7.0 in /home/bnt4me/.local/lib/python3.10/site-packages (from pephubclient>=0.4.2->peppy>=0.40.6->geofetch) (0.9.4)
    Requirement already satisfied: pydantic>2.5.0 in /home/bnt4me/.local/lib/python3.10/site-packages (from pephubclient>=0.4.2->peppy>=0.40.6->geofetch) (2.7.3)
    Requirement already satisfied: jsonschema in /home/bnt4me/.local/lib/python3.10/site-packages (from pipestat>=0.11.0->piper>=0.14.4->geofetch) (4.23.0)
    Requirement already satisfied: eido in /home/bnt4me/.local/lib/python3.10/site-packages (from pipestat>=0.11.0->piper>=0.14.4->geofetch) (0.2.4)
    Requirement already satisfied: jinja2 in /usr/lib/python3/dist-packages (from pipestat>=0.11.0->piper>=0.14.4->geofetch) (3.0.3)
    Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil>=2.8.2->pandas>=1.5.3->geofetch) (1.16.0)
    Requirement already satisfied: attmap>=0.13.0 in /home/bnt4me/.local/lib/python3.10/site-packages (from yacman>=0.9.3->piper>=0.14.4->geofetch) (0.13.2)
    Requirement already satisfied: oyaml in /home/bnt4me/.local/lib/python3.10/site-packages (from yacman>=0.9.3->piper>=0.14.4->geofetch) (1.0)
    Requirement already satisfied: attrs>=22.2.0 in /home/bnt4me/.local/lib/python3.10/site-packages (from jsonschema->pipestat>=0.11.0->piper>=0.14.4->geofetch) (25.3.0)
    Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /home/bnt4me/.local/lib/python3.10/site-packages (from jsonschema->pipestat>=0.11.0->piper>=0.14.4->geofetch) (2025.4.1)
    Requirement already satisfied: referencing>=0.28.4 in /home/bnt4me/.local/lib/python3.10/site-packages (from jsonschema->pipestat>=0.11.0->piper>=0.14.4->geofetch) (0.36.2)
    Requirement already satisfied: rpds-py>=0.7.1 in /home/bnt4me/.local/lib/python3.10/site-packages (from jsonschema->pipestat>=0.11.0->piper>=0.14.4->geofetch) (0.24.0)
    Requirement already satisfied: annotated-types>=0.4.0 in /home/bnt4me/.local/lib/python3.10/site-packages (from pydantic>2.5.0->pephubclient>=0.4.2->peppy>=0.40.6->geofetch) (0.6.0)
    Requirement already satisfied: pydantic-core==2.18.4 in /home/bnt4me/.local/lib/python3.10/site-packages (from pydantic>2.5.0->pephubclient>=0.4.2->peppy>=0.40.6->geofetch) (2.18.4)
    Requirement already satisfied: typing-extensions>=4.6.1 in /home/bnt4me/.local/lib/python3.10/site-packages (from pydantic>2.5.0->pephubclient>=0.4.2->peppy>=0.40.6->geofetch) (4.8.0)
    Requirement already satisfied: click<9.0.0,>=7.1.1 in /usr/lib/python3/dist-packages (from typer>=0.7.0->pephubclient>=0.4.2->peppy>=0.40.6->geofetch) (8.0.3)
    
    [1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m A new release of pip is available: [0m[31;49m23.2.1[0m[39;49m -> [0m[32;49m25.1.1[0m
    [1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m To update, run: [0m[32;49mpython3 -m pip install --upgrade pip[0m



```bash
geofetch --version
```

    geofetch 0.12.8


1) Download SRA files and PEP using GEOfetch

Add flags:
1) `--add-convert-modifier` (To add looper configurations for conversion)
2) `--discard-soft` (To delete soft files. We don't need them :D)


```bash
geofetch -i GSE67303 -n red_algae -m `pwd` --add-convert-modifier --discard-soft
```

    [1;30m[INFO][0m [32m[00:54:23][0m Metadata folder: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae
    [1;30m[INFO][0m [32m[00:54:24][0m Trying GSE67303 (not a file) as accession...
    [1;30m[INFO][0m [32m[00:54:24][0m Skipped 0 accessions. Starting now.
    [1;30m[INFO][0m [32m[00:54:24][0m [38;5;200mProcessing accession 1 of 1: 'GSE67303'[0m
    [1;30m[INFO][0m [32m[00:54:24][0m Processed 4 samples.
    [1;30m[INFO][0m [32m[00:54:24][0m Expanding metadata list...
    [1;30m[INFO][0m [32m[00:54:24][0m Found SRA Project accession: SRP056574
    [1;30m[INFO][0m [32m[00:54:24][0m Downloading SRP056574 sra metadata
    [1;30m[INFO][0m [32m[00:54:25][0m Parsing SRA file to download SRR records
    [1;30m[INFO][0m [32m[00:54:25][0m Getting SRR: SRR1930183  in (GSE67303)
    
    2025-07-10T04:54:26 prefetch.2.11.3: Current preference is set to retrieve SRA Normalized Format files with full base quality scores.
    2025-07-10T04:54:26 prefetch.2.11.3: 1) Downloading 'SRR1930183'...
    2025-07-10T04:54:26 prefetch.2.11.3: SRA Normalized Format file is being retrieved, if this is different from your preference, it may be due to current file availability.
    2025-07-10T04:54:26 prefetch.2.11.3:  Downloading via HTTPS...
    2025-07-10T04:54:31 prefetch.2.11.3:  HTTPS download succeed
    2025-07-10T04:54:31 prefetch.2.11.3:  'SRR1930183' is valid
    2025-07-10T04:54:31 prefetch.2.11.3: 1) 'SRR1930183' was downloaded successfully
    2025-07-10T04:54:31 prefetch.2.11.3: 'SRR1930183' has 0 unresolved dependencies
    [1;30m[INFO][0m [32m[00:54:31][0m Getting SRR: SRR1930184  in (GSE67303)
    
    2025-07-10T04:54:32 prefetch.2.11.3: Current preference is set to retrieve SRA Normalized Format files with full base quality scores.
    2025-07-10T04:54:32 prefetch.2.11.3: 1) Downloading 'SRR1930184'...
    2025-07-10T04:54:32 prefetch.2.11.3: SRA Normalized Format file is being retrieved, if this is different from your preference, it may be due to current file availability.
    2025-07-10T04:54:32 prefetch.2.11.3:  Downloading via HTTPS...
    2025-07-10T04:54:36 prefetch.2.11.3:  HTTPS download succeed
    2025-07-10T04:54:36 prefetch.2.11.3:  'SRR1930184' is valid
    2025-07-10T04:54:36 prefetch.2.11.3: 1) 'SRR1930184' was downloaded successfully
    2025-07-10T04:54:36 prefetch.2.11.3: 'SRR1930184' has 0 unresolved dependencies
    [1;30m[INFO][0m [32m[00:54:36][0m Getting SRR: SRR1930185  in (GSE67303)
    
    2025-07-10T04:54:37 prefetch.2.11.3: Current preference is set to retrieve SRA Normalized Format files with full base quality scores.
    2025-07-10T04:54:37 prefetch.2.11.3: 1) Downloading 'SRR1930185'...
    2025-07-10T04:54:37 prefetch.2.11.3: SRA Normalized Format file is being retrieved, if this is different from your preference, it may be due to current file availability.
    2025-07-10T04:54:37 prefetch.2.11.3:  Downloading via HTTPS...
    2025-07-10T04:54:45 prefetch.2.11.3:  HTTPS download succeed
    2025-07-10T04:54:45 prefetch.2.11.3:  'SRR1930185' is valid
    2025-07-10T04:54:45 prefetch.2.11.3: 1) 'SRR1930185' was downloaded successfully
    2025-07-10T04:54:45 prefetch.2.11.3: 'SRR1930185' has 0 unresolved dependencies
    [1;30m[INFO][0m [32m[00:54:45][0m Getting SRR: SRR1930186  in (GSE67303)
    
    2025-07-10T04:54:46 prefetch.2.11.3: Current preference is set to retrieve SRA Normalized Format files with full base quality scores.
    2025-07-10T04:54:46 prefetch.2.11.3: 1) Downloading 'SRR1930186'...
    2025-07-10T04:54:46 prefetch.2.11.3: SRA Normalized Format file is being retrieved, if this is different from your preference, it may be due to current file availability.
    2025-07-10T04:54:46 prefetch.2.11.3:  Downloading via HTTPS...
    2025-07-10T04:54:52 prefetch.2.11.3:  HTTPS download succeed
    2025-07-10T04:54:52 prefetch.2.11.3:  'SRR1930186' is valid
    2025-07-10T04:54:52 prefetch.2.11.3: 1) 'SRR1930186' was downloaded successfully
    2025-07-10T04:54:52 prefetch.2.11.3: 'SRR1930186' has 0 unresolved dependencies
    [1;30m[INFO][0m [32m[00:54:52][0m Finished processing 1 accession(s)
    [1;30m[INFO][0m [32m[00:54:52][0m Cleaning soft files ...
    [1;30m[INFO][0m [32m[00:54:52][0m Creating complete project annotation sheets and config file...
    [1;30m[INFO][0m [32m[00:54:52][0m [92mSample annotation sheet: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/GSE67303_PEP/GSE67303_PEP_raw.csv . Saved![0m
    [1;30m[INFO][0m [32m[00:54:52][0m [92mFile has been saved successfully[0m
    [1;30m[INFO][0m [32m[00:54:52][0m Config file: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/GSE67303_PEP/GSE67303_PEP.yaml
    [1;30m[INFO][0m [32m[00:54:52][0m Looper config file: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/looper_config.yaml


Let's see if files were downloaded:


```bash
ls
```

    [0m[01;34mfq_folder[0m                         raw-data-downloading.ipynb  [01;34mSRR1930185[0m
    howto-sra-to-fastq.ipynb          [01;34mred_algae[0m                   [01;34mSRR1930186[0m
    processed-data-downloading.ipynb  [01;34mSRR1930183[0m
    python-usage.ipynb                [01;34mSRR1930184[0m


now let's check how does our config file looks like:


```bash
cat ./red_algae/GSE67303_PEP/GSE67303_PEP.yaml
```

    # Autogenerated by geofetch
    
    name: GSE67303
    pep_version: 2.1.0
    sample_table: GSE67303_PEP_raw.csv
    
    "experiment_metadata":
      "series_contact_address": "930 N University Ave"
      "series_contact_city": "Ann Arbor"
      "series_contact_country": "USA"
      "series_contact_department": "Chemistry"
      "series_contact_email": "mtardu@umich.edu"
      "series_contact_institute": "University of Michigan"
      "series_contact_laboratory": "Koutmou Lab"
      "series_contact_name": "mehmet,,tardu"
      "series_contact_state": "MI"
      "series_contact_zip_postal_code": "48109"
      "series_contributor": "Mehmet,,Tardu + Ugur,M,Dikbas + Ibrahim,,Baris + Ibrahim,H,Kavakli"
      "series_geo_accession": "GSE67303"
      "series_last_update_date": "May 15 2019"
      "series_overall_design": "Identification of blue light and red light regulated genes\
        \ by deep sequencing in biological duplicates. qRT-PCR was performed to verify\
        \ the RNA-seq results."
      "series_platform_id": "GPL19949"
      "series_platform_organism": "Cyanidioschyzon merolae strain 10D"
      "series_platform_taxid": "280699"
      "series_pubmed_id": "27614431"
      "series_relation": "BioProject: https://www.ncbi.nlm.nih.gov/bioproject/PRJNA279462\
        \ + SRA: https://www.ncbi.nlm.nih.gov/sra?term=SRP056574"
      "series_sample_id": "GSM1644066 + GSM1644067 + GSM1644068 + GSM1644069"
      "series_sample_organism": "Cyanidioschyzon merolae strain 10D"
      "series_sample_taxid": "280699"
      "series_status": "Public on Sep 01 2016"
      "series_submission_date": "Mar 26 2015"
      "series_summary": "Light is one of the main environmental cues that affects the\
        \ physiology and behavior of many organisms. The effect of light on genome-wide\
        \ transcriptional regulation has been well-studied in green algae and plants,\
        \ but not in red algae. Cyanidioschyzon merolae is used as a model red algae,\
        \ and is suitable for studies on transcriptomics because of its compact genome\
        \ with a relatively small number of genes. In addition, complete genome sequences\
        \ of the nucleus, mitochondrion, and chloroplast of this organism have been determined.\
        \ Together, these attributes make C. merolae an ideal model organism to study\
        \ the response to light stimuli at the transcriptional and the systems biology\
        \ levels. Previous studies have shown that light significantly affects cell signaling\
        \ in this organism, but there are no reports on its blue light- and red light-mediated\
        \ transcriptional responses. We investigated the direct effects of blue and red\
        \ light at the transcriptional level using RNA-seq. Blue and red light were found\
        \ to regulate 35% of the total genes in C. merolae. Blue light affected the transcription\
        \ of genes involved protein synthesis while red light specifically regulated the\
        \ transcription of genes involved in photosynthesis and DNA repair. Blue or red\
        \ light regulated genes involved in carbon metabolism and pigment biosynthesis.\
        \ Overall, our data showed that red and blue light regulate the majority of the\
        \ cellular, cell division, and repair processes in C. merolae."
      "series_supplementary_file": "ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE67nnn/GSE67303/suppl/GSE67303_DEG_cuffdiff.xlsx"
      "series_title": "RNA-seq analysis of the transcriptional response to blue and red\
        \ light in the extremophilic red alga, Cyanidioschyzon merolae"
      "series_type": "Expression profiling by high throughput sequencing"
    
    
    
    sample_modifiers:
      append:
        # Project metadata:
        sample_treatment_protocol_ch1: "Cells were exposed to blue-light (15 µmole m-2s-1) for 30 minutes"
        sample_growth_protocol_ch1: "Cyanidioschyzon merolae cells were grown in 2xMA media"
        sample_extract_protocol_ch1: "Dark kept and blue-light exposed C.merolae cells were removed and RNA was harvested using Trizol reagent. Illumina TruSeq RNA Sample Prep Kit (Cat#RS-122-2001) was used with 1 ug of total RNA for the construction of sequencing libraries., RNA libraries were prepared for sequencing using standard Illumina protocols"
        sample_data_processing: "The purified cDNA library was sequenced on Illumina''s MiSeq sequencing platform following vendor''s instruction for running the instrument., Sequenced reads were trimmed for adaptor sequence, and masked for low-complexity or low-quality sequence, then mapped to Cyanidioschyzon merolae 10D reference genome (assembly ID:ASM9120v1) using TopHat (v2.0.5)., Differential expression analysis was conducted by using cuffdiff tool in cufflink suite (v2.2)"
        supplementary_files_format_and_content: "Excel spreadsheet includes FPKM values for Darkness and Blue-Light exposed samples with p and q values of cuffdiff output."
        # End of project metadata
        
    
        # Adding sra convert looper pipeline
        SRR_files: SRA
    
      derive:
        attributes: [read1, read2, SRR_files]
        sources:
          SRA: "${SRARAW}/{srr}/{srr}.sra"
          FQ: "${SRAFQ}/{srr}.fastq.gz"
          FQ1: "${SRAFQ}/{srr}_1.fastq.gz"
          FQ2: "${SRAFQ}/{srr}_2.fastq.gz"
      imply:
        - if:
            organism: "Mus musculus"
          then:
            genome: mm10
        - if:
            organism: "Homo sapiens"
          then:
            genome: hg38
        - if:
            read_type: "PAIRED"
          then:
            read1: FQ1
            read2: FQ2
        - if:
            read_type: "SINGLE"
          then:
            read1: FQ1
    
    
    
    


To run pipeline, you should set up few environmental variables:
1) SRARAW - folder where SRA files were downloaded
2) SRAFQ -folder where fastq should be produced
3) CODE - (first you should clone geofetch), and $CODE is where geofetch folder is located


```bash
# Set SRARAW env
export SRARAW=`pwd`
```


```bash
# Create folder where you want to store fq
mkdir fq_folder
```


```bash
# Set SRAFQ env
export SRAFQ=`pwd`/fq_folder
```

### Now install looper if you don't have it


```bash
# pip install looper
```


```bash
looper --version
```

    2.0.1
    [0m


Let's check where is looper config file and whats inside:


```bash
ls red_algae
```

    [0m[01;34mGSE67303_PEP[0m  looper_config.yaml  [01;34moutput_dir[0m



```bash
cat red_algae/looper_config.yaml
```

    pep_config: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/GSE67303_PEP/GSE67303_PEP.yaml
    output_dir: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir
    pipeline_interfaces:
      - /home/bnt4me/.local/lib/python3.10/site-packages/geofetch/templates/pipeline_interface_convert.yaml


Geofetch automatically generated paths to pep_config and pipeline interfaces that are embedded into geofetch


```bash
looper run --config ./red_algae/looper_config.yaml -p local --output-dir .
```

    Looper version: 2.0.1
    Command: run
    Using default divvy config. You may specify in env var: ['DIVCFG']
    Activating compute package 'local'
    [36m## [1 of 4] sample: cm_bluelight_rep1; pipeline: sra_convert[0m
    Writing script to /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/submission/sra_convert_cm_bluelight_rep1.sub
    Job script (n=1; 0.00Gb): /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/submission/sra_convert_cm_bluelight_rep1.sub
    Compute node: alex-laptop
    Start time: 2025-07-10 00:59:02
    Using outfolder: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930183
    No pipestat output schema was supplied to PipestatManager.
    Initializing results file '/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930183/stats.yaml'
    ### Pipeline run code and environment:
    
    *          Command: `/home/bnt4me/.local/bin/sraconvert --srr /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/SRR1930183/SRR1930183.sra -O /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline`
    *     Compute host: `alex-laptop`
    *      Working dir: `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks`
    *        Outfolder: `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930183/`
    *         Log file: `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930183/sra_convert_log.md`
    *       Start time:  (07-10 00:59:03) elapsed: 0.0 _TIME_
    
    ### Version log:
    
    *   Python version: `3.10.12`
    *      Pypiper dir: `/home/bnt4me/.local/lib/python3.10/site-packages/pypiper`
    *  Pypiper version: `0.14.4`
    *     Pipeline dir: `/home/bnt4me/.local/bin`
    * Pipeline version: 
    
    ### Arguments passed to pipeline:
    
    *          `bamfolder`:  ``
    *        `config_file`:  `sraconvert.yaml`
    *             `format`:  `fastq`
    *           `fqfolder`:  `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/fq_folder`
    *           `keep_sra`:  `False`
    *             `logdev`:  `False`
    *               `mode`:  `convert`
    *      `output_parent`:  `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline`
    *            `recover`:  `False`
    *        `sample_name`:  `None`
    *             `silent`:  `False`
    *          `srafolder`:  `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks`
    *                `srr`:  `['/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/SRR1930183/SRR1930183.sra']`
    *          `verbosity`:  `None`
    
    ### Initialized Pipestat Object:
    
    * PipestatManager (sra_convert)
    * Backend: File
    *  - results: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930183/stats.yaml
    *  - status: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930183
    * Multiple Pipelines Allowed: False
    * Pipeline name: sra_convert
    * Pipeline type: sample
    * Status Schema key: None
    * Results formatter: default_formatter
    * Results schema source: None
    * Status schema source: None
    * Records count: 2
    * Sample name: DEFAULT_SAMPLE_NAME
    
    
    ----------------------------------------
    
    Processing 1 of 1 files: SRR1930183
    Target to produce: `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/fq_folder/SRR1930183_1.fastq.gz`  
    
    > `fasterq-dump /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/SRR1930183/SRR1930183.sra -O /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/fq_folder` (871210)
    <pre>
    spots read      : 1,068,319
    reads read      : 2,136,638
    reads written   : 2,136,638
    </pre>
    Command completed. Elapsed time: 0:00:02. Running peak memory: 0.069GB.  
      PID: 871210;	Command: fasterq-dump;	Return code: 0;	Memory used: 0.069GB
    
    Already completed files: []
    
    ### Pipeline completed. Epilogue
    *        Elapsed time (this run):  0:00:02
    *  Total elapsed time (all runs):  0:00:02
    *         Peak memory (this run):  0.0685 GB
    *        Pipeline completed time: 2025-07-10 00:59:05
    Using default schema: /home/bnt4me/.local/bin/pipestat_output_schema.yaml
    [36m## [2 of 4] sample: cm_bluelight_rep2; pipeline: sra_convert[0m
    Writing script to /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/submission/sra_convert_cm_bluelight_rep2.sub
    Job script (n=1; 0.00Gb): /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/submission/sra_convert_cm_bluelight_rep2.sub
    Compute node: alex-laptop
    Start time: 2025-07-10 00:59:06
    Using outfolder: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930184
    No pipestat output schema was supplied to PipestatManager.
    Initializing results file '/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930184/stats.yaml'
    ### Pipeline run code and environment:
    
    *          Command: `/home/bnt4me/.local/bin/sraconvert --srr /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/SRR1930184/SRR1930184.sra -O /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline`
    *     Compute host: `alex-laptop`
    *      Working dir: `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks`
    *        Outfolder: `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930184/`
    *         Log file: `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930184/sra_convert_log.md`
    *       Start time:  (07-10 00:59:06) elapsed: 0.0 _TIME_
    
    ### Version log:
    
    *   Python version: `3.10.12`
    *      Pypiper dir: `/home/bnt4me/.local/lib/python3.10/site-packages/pypiper`
    *  Pypiper version: `0.14.4`
    *     Pipeline dir: `/home/bnt4me/.local/bin`
    * Pipeline version: 
    
    ### Arguments passed to pipeline:
    
    *          `bamfolder`:  ``
    *        `config_file`:  `sraconvert.yaml`
    *             `format`:  `fastq`
    *           `fqfolder`:  `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/fq_folder`
    *           `keep_sra`:  `False`
    *             `logdev`:  `False`
    *               `mode`:  `convert`
    *      `output_parent`:  `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline`
    *            `recover`:  `False`
    *        `sample_name`:  `None`
    *             `silent`:  `False`
    *          `srafolder`:  `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks`
    *                `srr`:  `['/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/SRR1930184/SRR1930184.sra']`
    *          `verbosity`:  `None`
    
    ### Initialized Pipestat Object:
    
    * PipestatManager (sra_convert)
    * Backend: File
    *  - results: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930184/stats.yaml
    *  - status: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930184
    * Multiple Pipelines Allowed: False
    * Pipeline name: sra_convert
    * Pipeline type: sample
    * Status Schema key: None
    * Results formatter: default_formatter
    * Results schema source: None
    * Status schema source: None
    * Records count: 2
    * Sample name: DEFAULT_SAMPLE_NAME
    
    
    ----------------------------------------
    
    Processing 1 of 1 files: SRR1930184
    Target to produce: `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/fq_folder/SRR1930184_1.fastq.gz`  
    
    > `fasterq-dump /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/SRR1930184/SRR1930184.sra -O /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/fq_folder` (871261)
    <pre>
    spots read      : 762,229
    reads read      : 1,524,458
    reads written   : 1,524,458
    </pre>
    Command completed. Elapsed time: 0:00:02. Running peak memory: 0.083GB.  
      PID: 871261;	Command: fasterq-dump;	Return code: 0;	Memory used: 0.083GB
    
    Already completed files: []
    
    ### Pipeline completed. Epilogue
    *        Elapsed time (this run):  0:00:02
    *  Total elapsed time (all runs):  0:00:02
    *         Peak memory (this run):  0.0832 GB
    *        Pipeline completed time: 2025-07-10 00:59:08


    Using default schema: /home/bnt4me/.local/bin/pipestat_output_schema.yaml
    [36m## [3 of 4] sample: cm_darkness_rep1; pipeline: sra_convert[0m
    Writing script to /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/submission/sra_convert_cm_darkness_rep1.sub
    Job script (n=1; 0.00Gb): /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/submission/sra_convert_cm_darkness_rep1.sub
    Compute node: alex-laptop
    Start time: 2025-07-10 00:59:08
    Using outfolder: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930185
    No pipestat output schema was supplied to PipestatManager.
    Initializing results file '/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930185/stats.yaml'
    ### Pipeline run code and environment:
    
    *          Command: `/home/bnt4me/.local/bin/sraconvert --srr /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/SRR1930185/SRR1930185.sra -O /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline`
    *     Compute host: `alex-laptop`
    *      Working dir: `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks`
    *        Outfolder: `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930185/`
    *         Log file: `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930185/sra_convert_log.md`
    *       Start time:  (07-10 00:59:09) elapsed: 0.0 _TIME_
    
    ### Version log:
    
    *   Python version: `3.10.12`
    *      Pypiper dir: `/home/bnt4me/.local/lib/python3.10/site-packages/pypiper`
    *  Pypiper version: `0.14.4`
    *     Pipeline dir: `/home/bnt4me/.local/bin`
    * Pipeline version: 
    
    ### Arguments passed to pipeline:
    
    *          `bamfolder`:  ``
    *        `config_file`:  `sraconvert.yaml`
    *             `format`:  `fastq`
    *           `fqfolder`:  `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/fq_folder`
    *           `keep_sra`:  `False`
    *             `logdev`:  `False`
    *               `mode`:  `convert`
    *      `output_parent`:  `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline`
    *            `recover`:  `False`
    *        `sample_name`:  `None`
    *             `silent`:  `False`
    *          `srafolder`:  `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks`
    *                `srr`:  `['/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/SRR1930185/SRR1930185.sra']`
    *          `verbosity`:  `None`
    
    ### Initialized Pipestat Object:
    
    * PipestatManager (sra_convert)
    * Backend: File
    *  - results: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930185/stats.yaml
    *  - status: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930185
    * Multiple Pipelines Allowed: False
    * Pipeline name: sra_convert
    * Pipeline type: sample
    * Status Schema key: None
    * Results formatter: default_formatter
    * Results schema source: None
    * Status schema source: None
    * Records count: 2
    * Sample name: DEFAULT_SAMPLE_NAME
    
    
    ----------------------------------------
    
    Processing 1 of 1 files: SRR1930185
    Target to produce: `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/fq_folder/SRR1930185_1.fastq.gz`  
    
    > `fasterq-dump /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/SRR1930185/SRR1930185.sra -O /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/fq_folder` (871306)
    <pre>
    spots read      : 1,707,508
    reads read      : 3,415,016
    reads written   : 3,415,016
    </pre>
    Command completed. Elapsed time: 0:00:04. Running peak memory: 0.07GB.  
      PID: 871306;	Command: fasterq-dump;	Return code: 0;	Memory used: 0.07GB
    
    Already completed files: []
    
    ### Pipeline completed. Epilogue
    *        Elapsed time (this run):  0:00:04
    *  Total elapsed time (all runs):  0:00:04
    *         Peak memory (this run):  0.0701 GB
    *        Pipeline completed time: 2025-07-10 00:59:13
    Using default schema: /home/bnt4me/.local/bin/pipestat_output_schema.yaml
    [36m## [4 of 4] sample: cm_darkness_rep2; pipeline: sra_convert[0m
    Writing script to /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/submission/sra_convert_cm_darkness_rep2.sub
    Job script (n=1; 0.00Gb): /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/submission/sra_convert_cm_darkness_rep2.sub
    Compute node: alex-laptop
    Start time: 2025-07-10 00:59:13
    Using outfolder: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930186
    No pipestat output schema was supplied to PipestatManager.
    Initializing results file '/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930186/stats.yaml'
    ### Pipeline run code and environment:
    
    *          Command: `/home/bnt4me/.local/bin/sraconvert --srr /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/SRR1930186/SRR1930186.sra -O /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline`
    *     Compute host: `alex-laptop`
    *      Working dir: `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks`
    *        Outfolder: `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930186/`
    *         Log file: `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930186/sra_convert_log.md`
    *       Start time:  (07-10 00:59:14) elapsed: 0.0 _TIME_
    
    ### Version log:
    
    *   Python version: `3.10.12`
    *      Pypiper dir: `/home/bnt4me/.local/lib/python3.10/site-packages/pypiper`
    *  Pypiper version: `0.14.4`
    *     Pipeline dir: `/home/bnt4me/.local/bin`
    * Pipeline version: 
    
    ### Arguments passed to pipeline:
    
    *          `bamfolder`:  ``
    *        `config_file`:  `sraconvert.yaml`
    *             `format`:  `fastq`
    *           `fqfolder`:  `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/fq_folder`
    *           `keep_sra`:  `False`
    *             `logdev`:  `False`
    *               `mode`:  `convert`
    *      `output_parent`:  `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline`
    *            `recover`:  `False`
    *        `sample_name`:  `None`
    *             `silent`:  `False`
    *          `srafolder`:  `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks`
    *                `srr`:  `['/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/SRR1930186/SRR1930186.sra']`
    *          `verbosity`:  `None`
    
    ### Initialized Pipestat Object:
    
    * PipestatManager (sra_convert)
    * Backend: File
    *  - results: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930186/stats.yaml
    *  - status: /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/red_algae/output_dir/results_pipeline/SRR1930186
    * Multiple Pipelines Allowed: False
    * Pipeline name: sra_convert
    * Pipeline type: sample
    * Status Schema key: None
    * Results formatter: default_formatter
    * Results schema source: None
    * Status schema source: None
    * Records count: 2
    * Sample name: DEFAULT_SAMPLE_NAME
    
    
    ----------------------------------------
    
    Processing 1 of 1 files: SRR1930186
    Target to produce: `/home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/fq_folder/SRR1930186_1.fastq.gz`  
    
    > `fasterq-dump /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/SRR1930186/SRR1930186.sra -O /home/bnt4me/virginia/repos/pepspec/docs/geofetch/notebooks/fq_folder` (871369)
    <pre>
    spots read      : 1,224,029
    reads read      : 2,448,058
    reads written   : 2,448,058
    </pre>
    Command completed. Elapsed time: 0:00:02. Running peak memory: 0.083GB.  
      PID: 871369;	Command: fasterq-dump;	Return code: 0;	Memory used: 0.083GB
    
    Already completed files: []
    
    ### Pipeline completed. Epilogue
    *        Elapsed time (this run):  0:00:02
    *  Total elapsed time (all runs):  0:00:02
    *         Peak memory (this run):  0.0832 GB
    *        Pipeline completed time: 2025-07-10 00:59:16
    Using default schema: /home/bnt4me/.local/bin/pipestat_output_schema.yaml


    
    Looper finished
    Samples valid for job generation: 4 of 4
    [0m


### Check if everything worked:


```bash
cd fq_folder
```


```bash
ls
```

    SRR1930183_1.fastq  SRR1930184_1.fastq  SRR1930185_1.fastq  SRR1930186_1.fastq
    SRR1930183_2.fastq  SRR1930184_2.fastq  SRR1930185_2.fastq  SRR1930186_2.fastq


Everything was executed successfully and SRA files were converted into fastq files
