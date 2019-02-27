
## How to limit the files downloaded by `geofetch.py`

Fetch data and metadata from GEO and SRA.

This script will download either raw SRA data from SRA or processed GEO data
from GEO, given a GEO accession. It wants a GSE number, which can be passed
directly on the command line, or you can instead provide a file with a list of
GSE accessions. By default it will download all the samples in that accession,
but you can limit this by creating a long-format file with GSM numbers
specifying which individual samples to include. If the second column is
included, a third column may also be included and will be used as the
sample_name; otherwise, the sample will be named according to the GEO
Sample_title field. Any columns after the third will be ignored.

The 1, 2, or 3-column input file would look like this:

```console
GSE123  GSM#### Sample1
GSE123  GSM#### Sample2
GSE123  GSM####
GSE456
```

This will download 3 particular GSM experiments from GSE123, and everything from
GSE456. It will name the first two samples Sample1 and Sample2, and the third,
plus any from GSE456, will have names according to GEO metadata.

In addition to downloading the files (using the `sratoolkit`), this script also
produces an annotation metadata file for use as input to alignment pipelines. By
default, multiple `Run`s (SRR) in an `Experiment` (SRX) will be treated as samples
to combine, but this can be changed with a command-line argument.

Metadata output. For each GSE input accession (ACC),

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
