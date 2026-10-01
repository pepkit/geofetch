# Metadata output

Geofetch produces [PEPs](http://pep.databio.org/) for either processed or raw data (including metadata from SRA).
A project can be created either for a single combined (whole) input or for each project separately. 
(if `--acc-anno` is set). "combined" means that it will have rows for every sample in every GSE included 
in your input. So if you just gave a single GSE, then the combined file is the same as the GSE file.

**For raw data**: a metadata file will be created including SRA and GSM annotation.

**For processed data**: a metadata file will be created just for GSE and GSM annotation. User
can choose which data should he download. There are 3 downloading options for processed: samples, series and both.

### Single PEP will contain:
- project_name.csv - all metadata for sample processed data
- project_name_subannotation.csv (*just for raw data*) - for *merged* samples
(samples for which there are multiple SRR Runs for a single SRX `Experiment`)
- project_name.yaml - project config file that stores all project information + common samples metadata

Storing common metadata in project file is an efficient way to reduce project size and complexity of csv files. 
To specify and manage common metadata (where and how it should be stored) you can use next arguments: 
`--const-limit-project`, `--const-limit-discard`, `--attr-limit-truncate`

### Saving actual data:
Actual data will be saved if `--just-metadata` argument is not set. User should specify path to the folder where this
data should be downloaded.

----
Additionally, for each GSE input accession (ACC), `geofetch` produces (if discard-soft is not set):

- GSE_ACC####.soft a SOFT file (annotating the experiment itself)
- GSM_ACC####.soft a SOFT file (annotating the samples within the experiment)
- SRA_ACC####.soft a CSV file (annotating each SRA Run, retrieved from GSE->GSM->SRA)

____
# geofetch - Geofetcher using Python

user can use geofetch in Python without saving any files. All the geofetch projects will be automatically downloaded
as peppy Project. It helps save time and processing work.

THe output in this case will be dictionary of projects:
```python
{'key1': (some_project),
 'key2': (second_project)}
```

More information you can find in tutorial files.