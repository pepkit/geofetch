#  How to specify samples to download

The command-line interface provides a way to give GSE or SRA accession IDs. By default, `geofetch` will download all the samples it can find in the accession you give it. What if you want to restrict the download to just a few samples? Or what if you want to combine samples from multiple accessions? If you want more control, either because you have multiple accessions or you want to specify a subset of samples, then you can use the *file-based sample specification*, in which you provide `geofetch` with a file listing your GSE/GSM accessions.

## The file-based sample specification


Create a file with 3 columns that correspond to `GSE`, `GSM`, and `Sample_name. You may mix 1, 2, and 3 column lines in the file. An example input file could look like this:

```console
GSE123  GSM#### Sample1
GSE123  GSM#### Sample2
GSE123  GSM####
GSE456
```

By default, `geofetch` will download all the samples in every included accession, but you can limit this by adding a second column with **GSM accessions** (which specify individual samples with a **GSE dataset**). If the second column is included, a third column may also be included and will be used
as the sample_name; otherwise, the sample will be named according to the GEO Sample_title field. Any columns after the third will be ignored.

This will download 3 particular GSM experiments from GSE123, and everything from GSE456. It will name the first two samples Sample1 and Sample2, and the third, plus any from GSE456, will have names according to GEO metadata.
