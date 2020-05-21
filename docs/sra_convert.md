# Sraconvert

When you install geofetch, you also get a second utility called `sraconvert` that handles converting sra data into either `bam` or `fastq` format for downstream processing. Sraconvert is essentially a wrapper around NCBI's sra-tools that provides more convenient interface to converting pre-downloaded `sra` files. 

The basic advantages over just using prefetch are:

- it provides the same interface to either download or delete sra files
- it uses the same interface to delete converted files, if desired
- it can automatically delete sra data that has been already converted
- it allows a more flexible specification of locations, using either environment variables or command-line arguments.

This effectively makes it easier to interact with *project-level* management of sra and fastq data using [looper](http://looper.databio.org) and PEP-compatible projects.



## Tutorial

The [GSE67303 data set](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE67303) has about 250 mb of data across 4 samples, so it's a quick download for a test case. 

Create the metadata:
```
geofetch -i GSE59916 -n dr_rrbs -m 'sandbox' --just-metadata \
	-P $CODE/dnameth_pipelines/pipeline_interface.yaml
```

Grab the actual data with prefetch (you can skip the above step if you want to):

```
geofetch -i GSE59916 -n dr_rrbs -m 'sandbox' -P $CODE/dnameth_pipelines/pipeline_interface.yaml
```

Now, convert the prefetched sra data into fastq format:

```
export SRARAW=$HOME/ncbi/public/sra/
export SRAFQ=sandbox/fq
looper run dr_rrbs/dr_rrbs_config.yaml -a sra_convert
```

And finally, run the pipeline:
```
looper run dr_rrbs/dr_rrbs_config.yaml
```


## Here's how to use sraconvert to delete the sra data after processing

```
looper run /project/shefflab/data/sra_meta/GSE47966/GSE47966_config.yaml --sp sra_convert --mode delete_sra --package local
```