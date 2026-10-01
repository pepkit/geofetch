# Package `geofetch` Documentation

## Package Overview

The `geofetch` package provides tools for downloading metadata and data from Gene Expression Omnibus (GEO) and Sequence Read Archive (SRA). It can convert GEO/SRA metadata into PEP format for easy integration with other PEPkit tools.

### Key Features

- **GEO/SRA Download**: Fetch metadata and raw data from NCBI repositories
- **PEP Generation**: Automatically create PEP-formatted project configs
- **Flexible Filtering**: Search and filter GEO datasets by date and criteria
- **SRA Integration**: Download and convert SRA data to FASTQ format
- **Processed Data**: Download processed data matrices from GEO

### Installation

```bash
pip install geofetch
```

### Quick Example

```python
from geofetch import Geofetcher

# Initialize geofetcher
gf = Geofetcher()

# Fetch a GEO series
gf.fetch_all(input="GSE####", name="my_project")
```

## API Reference

### Geofetcher Class

The main class for fetching data from GEO/SRA:

::: geofetch.Geofetcher
    options:
      docstring_style: google
      show_source: true
      show_signature: true
      merge_init_into_class: true

### Finder Class

Class for searching and finding GSE accessions:

::: geofetch.Finder
    options:
      docstring_style: google
      show_source: true
      show_signature: true
      merge_init_into_class: true
