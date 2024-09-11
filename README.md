# <img src="https://raw.githubusercontent.com/pepkit/geofetch/master/docs/img/geofetch_logo.svg?sanitize=true" alt="geofetch logo" height="70">

[![PEP compatible](https://pepkit.github.io/img/PEP-compatible-green.svg)](https://pepkit.github.io)
![Run pytests](https://github.com/pepkit/geofetch/workflows/Run%20pytests/badge.svg)
[![docs-badge](https://readthedocs.org/projects/geofetch/badge/?version=latest)](https://geofetch.databio.org/en/latest/)
[![pypi-badge](https://img.shields.io/pypi/v/geofetch)](https://pypi.org/project/geofetch)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io/recipes/geofetch/README.html)

**geofetch** is a command-line tool that downloads sequencing data and metadata from GEO and SRA and create metadata tables in [standard PEP format](https://pep.databio.org/). `geofetch` is hosted at [pypi](https://pypi.org/project/geofetch/). You can convert the result of geofetch into unmapped `bam` or `fastq` files with the included `sraconvert` command.

## Key geofetch features:

- Works with GEO and SRA metadata
- Combines samples from different projects
- Standardizes output metadata
- Filters type and size of processed files (from GEO) before downloading them
- Easy to use
- Fast execution time
- Can search GEO to find relevant data
- Can be used either as a command-line tool or from within Python using an API

## Docs

---

**Documentation**: <a href="https://pep.databio.org/geofetch/" target="_blank">https://pep.databio.org/geofetch/</a>

**Source Code**: <a href="https://github.com/pepkit/geofetch/" target="_blank">https://github.com/pepkit/geofetch/</a>

---


## Installation
To install `geofetch` use this command: 
```
pip install geofetch
```
or install the latest version from the GitHub repository:
```
pip install git+https://github.com/pepkit/geofetch.git
```


## How to cite:
https://doi.org/10.1093/bioinformatics/btad069
```bibtex
@article{10.1093/bioinformatics/btad069,
    author = {Khoroshevskyi, Oleksandr and LeRoy, Nathan and Reuter, Vincent P and Sheffield, Nathan C},
    title = "{GEOfetch: a command-line tool for downloading data and standardized metadata from GEO and SRA}",
    journal = {Bioinformatics},
    volume = {39},
    number = {3},
    pages = {btad069},
    year = {2023},
    month = {03},
    abstract = "{The Gene Expression Omnibus has become an important source of biological data for secondary analysis. However, there is no simple, programmatic way to download data and metadata from Gene Expression Omnibus (GEO) in a standardized annotation format.To address this, we present GEOfetch—a command-line tool that downloads and organizes data and metadata from GEO and SRA. GEOfetch formats the downloaded metadata as a Portable Encapsulated Project, providing universal format for the reanalysis of public data.GEOfetch is available on Bioconda and the Python Package Index (PyPI).}",
    issn = {1367-4811},
    doi = {10.1093/bioinformatics/btad069},
    url = {https://doi.org/10.1093/bioinformatics/btad069},
    eprint = {https://academic.oup.com/bioinformatics/article-pdf/39/3/btad069/49407404/btad069.pdf},
}
```