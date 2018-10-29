# geofetch

Given one or more GEO or SRA accessions, `geofetch` can 1) download either raw or processed data from either GEO or SRA and 2) produce a standardized [PEP](http://pepkit.github.io) sample annotation sheet of public metadata. This makes it really easy to run [looper](https://pepkit.github.io/docs/looper/)-compatible pipelines on public datasets by handling data acquisition and metadata formatting and standardization for you.

This project is still pre-release, but it is completely functional.

## Overview

The geofetch repository has two components:

1. `geofetch/geofetch.py` - A python script that downloads metadata and produces PEP-compatible sample annotation files, and downloads `.sra` files (or processed data from GEO if requested).
2. `sra_convert/sra_convert.py` - A [pypiper](http://pypiper.readthedocs.io) pipeline that converts SRA files into BAM files.


## How to build a PEP from SRA or GEO data

1. You must have the `sratoolkit` installed, with tools in your `PATH` (check to make sure you can run `prefetch`). Make sure it's configured to store `sra` files where you want them (see details below on `sratools`).

2. Download SRA data using `geofetch.py`. To see full options, see the help menu with:

	```
	python geofetch.py -h
	```
	
	For example, run it like:

	```
	python geofetch.py -i GSE##### -m path/to/metadata/folder -n PROJECT_NAME
	```

	This will do 2 things:

	1. download all `.sra` files from `GSE#####` into your SRA folder (wherever you have configured `sratools` to stick data).
	2. produce a sample annotation sheet (currently called `PROJECT_NAME_annotation.csv` in your metadata folder), which is what you will use as part of your PEP.
	3. produce a project configuration file (`PROJECT_NAME_config.yaml`) in your metadata folder.

	Here are some other examples:

	```
	./geofetch.py -i GSE95654 --just-metadata -n crc_rrbs -m '${CODE}sandbox'
	./geofetch.py -i GSE73215 --just-metadata -n cohesin_dose -m '${CODE}sandbox'
	
	```
 
3. Once you've produced your PEP annotation files and downloaded your SRA data, you should go check out the config files and annotation sheets and make sure they make sense to you. Then, you're ready to run pipelines on the data! The next thing is to convert the `sra` data into a format that can be used by pipelines, which we go over in the next section.

## How to convert the `sra` files to `bam`

With `.sra` data downloaded, we now need to convert these files into a more usable format. The `sra_convert` pipeline can convert `.sra` files into `.bam` format using the `sratoolkit`. The *PEP* files produced by `geofetch` can be immediately plugged into this pipeline to handle this conversion for you, either locally or on a compute cluster.

1. Make sure you have [looper](https://pepkit.github.io/docs/looper/) installed.

2. `geofetch` produces a configuration file with a built-in subproject for `sra_convert`, so we can run this pipeline with no further modification by activating that subproject using the `--sp sra_convert` argument. Here's how to convert one of the above samples:

```
looper run ${CODE}sandbox/cohesin_dose/cohesin_dose_config.yaml -d --sp sra_convert --lump 10
```

Here's what this means:

-`looper run` tells looper to `run` the project
- `${CODE}sandbox/cohesin_dose/cohesin_dose_config.yaml` is the project config file produced by `geofetch`. you can use any [PEP-compatible](http://pepkit.github.io) file here.
- `-d` means dry-run, so it won't actually submit the jobs, just to see if it works. 
- `--sp sra_convert` activates the *subproject* (`sp`) called `sra_convert`, which is defined in your project config file. It's created automatically by `geofetch`. This subproject points the `pipeline_interfaces` to `sra_convert` so `looper` knows which pipeline to use.
- `-lump 10` will tell `looper` to lump jobs together until it accumulates 10 GB of input files. This creates individual jobs that take about an hour or so, instead of submitting lots of 5-10 minute jobs. This is useful if you're using a cluster.


## Next steps

Once you've converted, then you just need to run the actual pipeline. What pipeline do you want to run? Add the pipeline interface into the `metadata.pipeline_interfaces` section on the project config file:

```
metadata:
  pipeline_interfaces: path/to/pipeline_interface
```


# A start-to-finish example

Let's take a GEO project from start to finish.


1. Download the data

```
./geofetch.py -i GSE95654 --just-metadata -n crc_rrbs -m '${CODE}sandbox'
```

2. *Finalize project config*. Link to the pipeline you want to use by adding a `pipeline_interface` to the project config file produced by `geofetch`. Make any other configuration adjustments to your project.

3. *Finalize sample annotation*. Adjust the `sample_annotation` file to make sure you have the right column names and attributes needed by the pipeline you're using. Make sure the `protocol` column matches the pipeline's `protocol` -- GEO submitters are notoriously bad at getting the metadata correct. For example,  this project lists the protocol as 'other' instead of as 'ATAC', so we have to manually correct it in the sample annotation file.

4. Run your pipeline:

	```
	looper run ${CODE}sandbox/cohesin_dose/cohesin_dose_config.yaml
	```

	or:

	```
	looper run ${CODE}sandbox/autism_microglia/autism_microglia_config.yaml -d
	```


## Tips

* Set an environment variable for `$SRABAM` (where `.bam` files will live), and `geofetch` will check to see if you have an already-converted bamfile there before issuing the command to download the `sra` file. In this way, you can delete old `sra` files after conversion and not have to worry about re-downloading them. 

* The config template uses an environment variable `$SRARAW` for where `.sra` files will live. If you set this variable to the same place you instructed `sratoolkit` to download `sra` files, you won't have to tweak the config file.

## Setting data download location with `sratools`

`geofetch` is using the `sratoolkit` to download raw data from SRA -- which means it's stuck with the [default path for downloading SRA data](http://databio.org/posts/downloading_sra_data.html), which I've written about. So before you run `geofetch`, make sure you have set up your download location to the correct place. In our group, we use a shared group environment variable called `${SRARAW}`, which points to a shared folder where the whole group has access to downloaded SRA data. You can point the `sratoolkit` (and therefore `geofetch`) to use that location with this one-time configuration code:

```
echo "/repository/user/main/public/root = \"$DATA\"" > ${HOME}/.ncbi/user-settings.mkfg
```

Now `sratoolkit` will download data into an `/sra` folder in `${DATA}`, which is what `${SRARAW}` points to.

If you are getting an error that the `.ncbi` folder does not exist in your home directory, you can just make a folder `.ncbi` with an empty file `user-settings.mkfg` and follow the same command above.

## How to limit the files downloaded by `geofetch.py`

Fetch data and metadata from GEO and SRA.

This script will download either raw SRA data from SRA or processed GEO data
from GEO, given a GEO accession. It wants a GSE number, which can be passed
directly on the command line, or you can instead provide a file with a list of
GSE accessions. By default it will download all the samples in that accession,
but you can limit this by creating a long-format file with GSM numbers
specifying which individual samples to include. If the second column is
included, a third column may also be included and will be used as the
sample_name; otherwise, the sample will be named according to the GEO
Sample_title field. Any columns after the third will be ignored.

The 1, 2, or 3-column input file would look like this:
```
GSE123	GSM####	Sample1
GSE123	GSM####	Sample2
GSE123	GSM####
GSE456
```

This will download 3 particular GSM experiments from GSE123, and everything from
GSE456. It will name the first two samples Sample1 and Sample2, and the third,
plus any from GSE456, will have names according to GEO metadata.

In addition to downloading the files (using the `sratoolkit`), this script also
produces an annotation metadata file for use as input to alignment pipelines. By
default, multiple Runs (SRR) in an Experiment (SRX) will be treated as samples
to combine, but this can be changed with a command-line argument.

Metadata output:
For each GSE input accession (ACC),
- GSE_ACC#.soft a SOFT file (annotating the experiment itself)
- GSM_ACC#.soft a SOFT file (annotating the samples within the experiment)
- SRA_ACC#.soft a CSV file (annotating each SRA Run, retrieved from GSE->GSM->SRA)

In addition, a single combined metadata file ("annoComb") for the whole input,
including SRA and GSM annotations for each sample. Here, "combined" means that it will have
rows for every sample in every GSE included in your input. So if you just gave a single GSE,
then the combined file is the same as the GSE file. If any "merged" samples exist
(samples for which there are multiple SRR Runs for a single SRX Experiment), the
script will also produce a merge table CSV file with the relationships between
SRX and SRR.

The way this works: Starting from a GSE, select a subset of samples (GSM Accessions) provided, 
and then obtain the SRX identifier for each of these from GEO. Now, query SRA for these SRX 
accessions and get any associated SRR accessions. Finally, download all of these SRR data files.
