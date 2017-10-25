# pepsra

Converts GEO or SRA accessions into PEP projects.

pepsra has two components:

1. `pepsra (get_geo)` - A script that downloads metadata and produces PEP files, and downloads `.sra` files.
2. `sra_convert` - A `pypiper` pipeline that converts SRA files into BAM files.