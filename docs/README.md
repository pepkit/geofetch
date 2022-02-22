# <img src="img/geofetch_logo.svg" class="img-header">

[![PEP compatible](http://pepkit.github.io/img/PEP-compatible-green.svg)](http://pepkit.github.io)

`geofetch` is a command-line tool that downloads and organizes data and metadata from GEO and SRA. When given one or more GEO/SRA accessions, `geofetch` is:

  - Download either raw or processed data from either SRA or GEO
  - Produce a standardized [PEP](http://pepkit.github.io) sample table. This makes it really easy to run [looper](https://pepkit.github.io/docs/looper/)-compatible pipelines on public datasets by handling data acquisition and metadata formatting and standardization for you.
  - Prepare a project to run with [sraconvert](sra_convert.md) to convert SRA files into FASTQ files.

## Quick example

`geofetch` runs on the command line. This command will download the raw data and metadata for the given GSE number.

```console
geofetch -i GSE95654
```

You can add `--processed` if you want to download processed files from the given experiment.


```console
geofetch -i GSE95654 --processed
```

You can add `--just-metadata` if you want to download metadata without the raw SRA files (or processed files if *processed* argument is added).

```console
geofetch -i GSE95654 --just-metadata
```

For more details, check out the [usage](usage.md) reference, [installation instructions](install.md), or head on over to the [tutorial](tutorial.md) for a detailed walkthrough.



