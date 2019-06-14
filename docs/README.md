# <img src="img/geofetch_logo.svg" class="img-header">

[![PEP compatible](http://pepkit.github.io/img/PEP-compatible-green.svg)](http://pepkit.github.io)

`geofetch` is a command-line tool that downloads and organizes data and metadata from GEO and SRA. When given one or more GEO/SRA accessions, `geofetch` will:

  - Download either raw or processed data from either GEO or SRA
  - Produces a standardized [PEP](http://pepkit.github.io) sample annotation sheet of public metadata. This makes it really easy to run [looper](https://pepkit.github.io/docs/looper/)-compatible pipelines on public datasets by handling data acquisition and metadata formatting and standardization for you.

You can use it with the [sra_convert](http://github.com/pepkit/sra_convert) pipeline, a [pypiper](http://pypiper.readthedocs.io) pipeline that converts SRA files into BAM files.

## Quick demo

`geofetch` runs on the command line. This command will download the metadata for the given GSE number.

```console
geofetch -i GSE95654
```

You can add `--just-metadata` if you don't want to download the raw SRA files.

```console
geofetch -i GSE95654 --just-metadata
```

For more details, check out the [usage](usage.md) reference, [installation instructions](install.md), or head on over to the [tutorial](tutorial.md) for a detailed walkthrough.
