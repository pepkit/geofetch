[![PEP compatible](http://pepkit.github.io/img/PEP-compatible-green.svg)](http://pepkit.github.io)

# <img src="../img/geofetch_logo.svg" class="img-fluid" style="max-height:45px; margin-top:-15px; margin-bottom:-10px">  usage reference

Given one or more GEO or SRA accessions, `geofetch` can 1) download either raw or processed data from either GEO or SRA and 2) produce a standardized [PEP](http://pepkit.github.io) sample annotation sheet of public metadata. This makes it really easy to run [looper](https://pepkit.github.io/docs/looper/)-compatible pipelines on public datasets by handling data acquisition and metadata formatting and standardization for you.

`geofetch` is a command-line script that downloads metadata and produces PEP-compatible sample annotation files, and downloads `.sra` files (or processed data from GEO if requested). You can use it with the [sra_convert](http://github.com/pepkit/sra_convert) pipeline, a [pypiper](http://pypiper.readthedocs.io) pipeline that converts SRA files into BAM files.


## Installing

```bash
pip install geofetch
```

To get started, next see the [tutorial](tutorial).
