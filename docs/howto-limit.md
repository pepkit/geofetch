
## How to specify multiple accessions

If you just have a single accession, you can pass it to `geofetch` directly on
the command line. If you want more control, either because you have multiple
accessions, or you want to specify a subset of samples, then you can provide a
file with a list of GSE accessions.

By default, `geofetch` will download all the samples in every included
accession, but you can limit this by adding a second column with **GSM
accessions** (which specify individual samples with a **GSE dataset**). If the
second column is included, a third column may also be included and will be used
as the sample_name; otherwise, the sample will be named according to the GEO
Sample_title field. Any columns after the third will be ignored.

You may mix 1, 2, and 3 column lines in the file. SO, the 1, 2, or 3-column
input file could look like this:

```console
GSE123  GSM#### Sample1
GSE123  GSM#### Sample2
GSE123  GSM####
GSE456
```

This will download 3 particular GSM experiments from GSE123, and everything from
GSE456. It will name the first two samples Sample1 and Sample2, and the third,
plus any from GSE456, will have names according to GEO metadata.

## Metadata output

For each GSE input accession (ACC), `geofetch` produces:

- GSE_ACC####.soft a SOFT file (annotating the experiment itself)
- GSM_ACC####.soft a SOFT file (annotating the samples within the experiment)
- SRA_ACC####.soft a CSV file (annotating each SRA Run, retrieved from GSE->GSM->SRA)

In addition, a single combined metadata file ("annoComb") for the whole input,
including SRA and GSM annotations for each sample. Here, "combined" means that it will have
rows for every sample in every GSE included in your input. So if you just gave a single GSE,
then the combined file is the same as the GSE file. If any "merged" samples exist
(samples for which there are multiple SRR Runs for a single SRX `Experiment`), the
script will also produce a merge table CSV file with the relationships between
SRX and SRR.

The way this works: Starting from a GSE, select a subset of samples (GSM Accessions) provided, 
and then obtain the SRX identifier for each of these from GEO. Now, query SRA for these SRX 
accessions and get any associated SRR accessions. Finally, download all of these SRR data files.
