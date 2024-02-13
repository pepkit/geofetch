# <img src="https://raw.githubusercontent.com/pepkit/geofetch/master/docs/img/geofetch_logo.svg?sanitize=true" alt="geofetch logo" height="70">

[![PEP compatible](https://pepkit.github.io/img/PEP-compatible-green.svg)](https://pepkit.github.io)
![Run pytests](https://github.com/pepkit/geofetch/workflows/Run%20pytests/badge.svg)
[![docs-badge](https://readthedocs.org/projects/geofetch/badge/?version=latest)](https://geofetch.databio.org/en/latest/)
[![pypi-badge](https://img.shields.io/pypi/v/geofetch)](https://pypi.org/project/geofetch)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io/recipes/geofetch/README.html)

`geofetch` is a command-line tool that downloads sequencing data and metadata from GEO and SRA and create metadata tables in [standard PEP format](https://pep.databio.org/). `geofetch` is hosted at [pypi](https://pypi.org/project/geofetch/). You can convert the result of geofetch into unmapped `bam` or `fastq` files with the included `sraconvert` command.

## Key geofetch features:

- Works with GEO and SRA metadata
- Combines samples from different projects
- Standardizes output metadata
- Filters type and size of processed files (from GEO) before downloading them
- Easy to use
- Fast execution time
- Can search GEO to find relevant data
- Can be used either as a command-line tool or from within Python using an API

For more information, see [complete documentation at geofetch.databio.org](http://geofetch.databio.org) (source in the [/docs](/docs) folder).
