# Metadata output

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
