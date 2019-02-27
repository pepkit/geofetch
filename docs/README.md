[![PEP compatible](http://pepkit.github.io/img/PEP-compatible-green.svg)](http://pepkit.github.io)

# <img src="img/geofetch_logo.svg" class="img-fluid" style="max-height:45px; margin-top:-15px; margin-bottom:-10px">  geofetch

`geofetch` is a command-line tool that does two things when given one or more GEO/SRA accessions:

  - Downloads either raw or processed data from either GEO or SRA
  - Produces a standardized [PEP](http://pepkit.github.io) sample annotation sheet of public metadata. This makes it really easy to run [looper](https://pepkit.github.io/docs/looper/)-compatible pipelines on public datasets by handling data acquisition and metadata formatting and standardization for you.

You can use it with the [sra_convert](http://github.com/pepkit/sra_convert) pipeline, a [pypiper](http://pypiper.readthedocs.io) pipeline that converts SRA files into BAM files.


## Installing

```bash
pip install geofetch
```

## Quick start

Now, run it on the command line:

```console
geofetch --help
```

Next, check out the [usage](usage) reference, or for a detailed walkthrough, head on over to the [tutorial](tutorial).
