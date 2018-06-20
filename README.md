# geofetch

Given a GEO or SRA accessions, `geofetch` can 1) download either raw or processed data from either GEO or SRA and 2) produce a standardized [PEP](http://pepkit.github.io) sample annotation sheet of public metadata. This makes it really easy to run [looper](https://pepkit.github.io/docs/looper/)-compatible pipelines on public datasets by handling data acquisition and metadata formatting and standardization for you.

This project is still pre-release, but it is completely functional. However, some things may change in the near future.

## Overview

geofetch has two components:

1. `geofetch/geofetch.py` - A python script that downloads metadata and produces PEP-compatible sample annotation files, and downloads `.sra` files (or processed data from GEO if requested).
2. `sra_convert/sra_convert.py` - A [pypiper](http://pypiper.readthedocs.io) pipeline that converts SRA files into BAM files.


## How to build a PEP from SRA or GEO data

1. Set environment variables for `$SRARAW` (where `.sra` files will live) and `$SRABAM` (where `.bam` files will live). `geofetch` will use these environment variables to automatically know where to store the `.sra` and `.bam` files.
2. Download SRA data using `geofetch.py`. You run it like:

	```
	python geofetch.py -i GSE#####
	```

	This will download all `.sra` files into your `$SRARAW` folder. To see full options, see the help menu with:

	```
	python geofetch.py -h
	```

	This will also produce a sample annotation sheet (currently called `annocomb_GSE#####.csv` in your `$SRAMETA` folder), which is what you will use as part of your PEP.

3. With `.sra` data downloaded, we now need to convert these files into a more usable format (`.bam`). Build a configuration file (see `sra_convert/example/project_config.yaml` for example) and point the `sample_annotation` to the annotation file produced by earlier `geofetch.py`.

4. Run the `sra_convert` pipeline using `looper` by running this command:

```
looper run project_config.yaml --lump
```

## Setting data download location with `sratools`

`geofetch` is using the `sratoolkit` to download raw data from SRA -- which means it's stuck with the [default path for downloading SRA data](http://databio.org/posts/downloading_sra_data.html), which I've written about. So before you run `geofetch`, make sure you have set up your download location to the correct place. In our group, we use a shared group environment variable called `${SRARAW}`, which points to a shared folder where the whole group has access to downloaded SRA data. You can point the `sratoolkit` (and therefore `geofetch`) to use that location with this one-time configuration code:


```
echo "/repository/user/main/public/root = \"$SRARAW\"" > ${HOME}/.ncbi/user-settings.mkfg
```

