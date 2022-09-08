# <img src="docs/img/geofetch_logo.svg" alt="geofetch logo" height="70">

[![PEP compatible](http://pepkit.github.io/img/PEP-compatible-green.svg)](http://pepkit.github.io)
![Run pytests](https://github.com/pepkit/geofetch/workflows/Run%20pytests/badge.svg)
[![docs-badge](https://readthedocs.org/projects/geofetch/badge/?version=latest)](http://geofetch.databio.org/en/latest/)
[![pypi-badge](https://img.shields.io/pypi/v/geofetch)](https://pypi.org/project/geofetch)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

`geofetch` is a command-line tool that downloads sequencing data and metadata from GEO and SRA and creates [standard PEPs](http://pep.databio.org/). `geofetch` is hosted at [pypi](https://pypi.org/project/geofetch/) and documentation is hosted at [geofetch.databio.org](http://geofetch.databio.org) (source in the [/docs](/docs) folder).

You can convert the result of geofetch into unmapped `bam` or `fastq` files with the included `sraconvert` command.

Key geofetch features:

- Works with GEO and SRA metadata
- Combines samples from different projects
- Standardizes output metadata
- Filters type and size of processed files (from GEO) before downloading them
- Easy to use
- Fast execution time
- Available GSE search tool
- Available both as command-line tool and Python execution Package
