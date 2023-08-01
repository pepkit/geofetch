# Sraconvert

When you install geofetch, you also get a second utility called `sraconvert` that handles converting sra data into either `bam` or `fastq` format for downstream processing. Sraconvert is essentially a wrapper around NCBI's sra-tools that provides more convenient interface to converting pre-downloaded `sra` files. 

The basic advantages over just using prefetch are:

- it provides the same interface to either download or delete sra files
- it uses the same interface to delete converted files, if desired
- it can automatically delete sra data that has been already converted
- it allows a more flexible specification of locations, using either environment variables or command-line arguments.

This effectively makes it easier to interact with *project-level* management of sra and fastq data using [looper](http://looper.databio.org) and PEP-compatible projects.



## Tutorial

See the [how-to](how_to_convert_fastq_from_sra.md) for an example of how to use `sraconvert`.