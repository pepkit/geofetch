# Sraconvert

When you install geofetch, you also get a second utility called `sraconvert` that handles converting sra data into either `bam` or `fastq` format for downstream processing. Sraconvert is essentially a wrapper around NCBI's sra-tools that provides more convenient interface to converting pre-downloaded `sra` files. 

The basic advantages over just using prefetch are:

- it provides the same interface to either download or delete sra files
- it uses the same intervace to delete converted files, if desired
- it can automatically delete sra data that has been already converted
- it allows a more flexibile specification of locations, using either
  environment variables or command-line arguments.

This effectively makes it easier to interact with *project-level* management of sra and fastq data using [looper](http://looper.databio.org) and PEP-compatible projects.



## Tutorial

This [data set](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE59916) one only has about 1GB of data across 4 samples:

Grab the actual data with prefetch:

```
geofetch -i GSE59916 -n dr_rrbs -m 'sandbox' -P $CODE/dnameth_pipelines/pipeline_interface.yaml
```

Create the metadata (you can do this all at once if you want to):
```
geofetch -i GSE59916 -n dr_rrbs -m 'sandbox' --just-metadata \
	-P $CODE/dnameth_pipelines/pipeline_interface.yaml
```

Now, convert the prefetched sra data into fastq format:

```
export SRARAW=$HOME/ncbi/public/sra/
export SRAFQ=sandbox/fq
looper run /home/nsheff/code/geofetch/sandbox/dr_rrbs/dr_rrbs_config.yaml --sp sra_convert
```

And finally, run the pipeline:
```
looper run /home/nsheff/code/geofetch/sandbox/dr_rrbs/dr_rrbs_config.yaml
```
