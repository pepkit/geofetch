jupyter:True
# Tutorial of usage geofetch as python package

♪♫*•♪♪♫*•♪♪♫*•♪♪♫*•♪♪♫*

Geofetch provides python fuctions to fetch metadata and metadata from GEO and SRA by using python language. `get_project` function returns dictionary of peppy projects that were found using filters and input you specified.
 peppy is a Python package that provides an API for handling standardized project and sample metadata. 
 
More information you can get here:
 
http://peppy.databio.org/en/latest/

http://pep.databio.org/en/2.0.0/

### First let's import geofetch


```python
from geofetch import Geofetcher
```

### Initiate Geofetch object by specifing parameters that you want to use for downloading metadata/data

1) If you won't specify any parameters, defaul parameters will be used


```python
geof = Geofetcher()
```

```.output
Metadata folder: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/project_name

```

2) To download processed data with samples and series specify this two arguments:


```python
geof = Geofetcher(processed=True, data_source="all")
```

```.output
Metadata folder: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/project_name

```

3) To tune project parameter, where metadata should be stored use next parameters:


```python
geof = Geofetcher(processed=True, data_source="all", const_limit_project = 20, const_limit_discard = 500, attr_limit_truncate = 10000 )
```

```.output
Metadata folder: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/project_name

```

4) To add more filter of other options see documentation

## Run Geofetch

### By default: 
1) No actual data will be downloaded (just_metadata=True)

2) No soft files will be saved on the disc (discard_soft=True)


```python
projects = geof.get_projects("GSE95654")
```

```.output
Trying GSE95654 (not a file) as accession...
Trying GSE95654 (not a file) as accession...

```


    Output()


```.output
Skipped 0 accessions. Starting now.
Processing accession 1 of 1: 'GSE95654'

Total number of processed SAMPLES files found is: 40
Total number of processed SERIES files found is: 0
Expanding metadata list...
Expanding metadata list...

```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">
</pre>



```.output
Finished processing 1 accession(s)
Cleaning soft files ...
Unifying and saving of metadata... 

```


    Output()



<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">
</pre>




    Output()



<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">
</pre>



```.output
No files found. No data to save. File /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/project_name/GSE95654_series/GSE95654_series.csv won't be created

```

Check if projects were created by checking dict keys:


```python
projects.keys()
```




    dict_keys(['GSE95654_samples'])



project for smaples was created! Now let's look into it.

\* the values of the dictionary are peppy projects. More information about peppy Project you can find in the documentation: http://peppy.databio.org/en/latest/


```python
len(projects['GSE95654_samples'].samples)
```




    40



We got 40 samples from GSE95654 project. If you want to check if it's correct information go into: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE95654

Now let's see actuall data. first 15 project and 5 clolumns:


```python
projects['GSE95654_samples'].sample_table.iloc[:15 , :5]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sample_name</th>
      <th>sample_library_strategy</th>
      <th>genome_build</th>
      <th>tissue</th>
      <th>sample_organism_ch1</th>
    </tr>
    <tr>
      <th>sample_name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>RRBS_on_CRC_patient_8</th>
      <td>RRBS_on_CRC_patient_8</td>
      <td>Bisulfite-Seq</td>
      <td>hg19</td>
      <td>primary tumor</td>
      <td>Homo sapiens</td>
    </tr>
    <tr>
      <th>RRBS_on_adjacent_normal_colon_patient_8</th>
      <td>RRBS_on_adjacent_normal_colon_patient_8</td>
      <td>Bisulfite-Seq</td>
      <td>hg19</td>
      <td>adjacent normal colon</td>
      <td>Homo sapiens</td>
    </tr>
    <tr>
      <th>RRBS_on_CRC_patient_32</th>
      <td>RRBS_on_CRC_patient_32</td>
      <td>Bisulfite-Seq</td>
      <td>hg19</td>
      <td>primary tumor</td>
      <td>Homo sapiens</td>
    </tr>
    <tr>
      <th>RRBS_on_adjacent_normal_colon_patient_32</th>
      <td>RRBS_on_adjacent_normal_colon_patient_32</td>
      <td>Bisulfite-Seq</td>
      <td>hg19</td>
      <td>adjacent normal colon</td>
      <td>Homo sapiens</td>
    </tr>
    <tr>
      <th>RRBS_on_CRC_patient_41</th>
      <td>RRBS_on_CRC_patient_41</td>
      <td>Bisulfite-Seq</td>
      <td>hg19</td>
      <td>primary tumor</td>
      <td>Homo sapiens</td>
    </tr>
    <tr>
      <th>RRBS_on_adjacent_normal_colon_patient_41</th>
      <td>RRBS_on_adjacent_normal_colon_patient_41</td>
      <td>Bisulfite-Seq</td>
      <td>hg19</td>
      <td>adjacent normal colon</td>
      <td>Homo sapiens</td>
    </tr>
    <tr>
      <th>RRBS_on_CRC_patient_42</th>
      <td>RRBS_on_CRC_patient_42</td>
      <td>Bisulfite-Seq</td>
      <td>hg19</td>
      <td>primary tumor</td>
      <td>Homo sapiens</td>
    </tr>
    <tr>
      <th>RRBS_on_adjacent_normal_colon_patient_42</th>
      <td>RRBS_on_adjacent_normal_colon_patient_42</td>
      <td>Bisulfite-Seq</td>
      <td>hg19</td>
      <td>adjacent normal colon</td>
      <td>Homo sapiens</td>
    </tr>
    <tr>
      <th>RRBS_on_ACF_patient_173</th>
      <td>RRBS_on_ACF_patient_173</td>
      <td>Bisulfite-Seq</td>
      <td>hg19</td>
      <td>aberrant crypt foci</td>
      <td>Homo sapiens</td>
    </tr>
    <tr>
      <th>RRBS_on_ACF_patient_515</th>
      <td>RRBS_on_ACF_patient_515</td>
      <td>Bisulfite-Seq</td>
      <td>hg19</td>
      <td>aberrant crypt foci</td>
      <td>Homo sapiens</td>
    </tr>
    <tr>
      <th>RRBS_on_normal_crypts_patient_139</th>
      <td>RRBS_on_normal_crypts_patient_139</td>
      <td>Bisulfite-Seq</td>
      <td>hg19</td>
      <td>normal colonic crypt</td>
      <td>Homo sapiens</td>
    </tr>
    <tr>
      <th>RRBS_on_ACF_patient_143</th>
      <td>RRBS_on_ACF_patient_143</td>
      <td>Bisulfite-Seq</td>
      <td>hg19</td>
      <td>aberrant crypt foci</td>
      <td>Homo sapiens</td>
    </tr>
    <tr>
      <th>RRBS_on_normal_crypts_patient_143</th>
      <td>RRBS_on_normal_crypts_patient_143</td>
      <td>Bisulfite-Seq</td>
      <td>hg19</td>
      <td>normal colonic crypt</td>
      <td>Homo sapiens</td>
    </tr>
    <tr>
      <th>RRBS_on_normal_crypts_patient_165</th>
      <td>RRBS_on_normal_crypts_patient_165</td>
      <td>Bisulfite-Seq</td>
      <td>hg19</td>
      <td>normal colonic crypt</td>
      <td>Homo sapiens</td>
    </tr>
    <tr>
      <th>RRBS_on_ACF_patient_165</th>
      <td>RRBS_on_ACF_patient_165</td>
      <td>Bisulfite-Seq</td>
      <td>hg19</td>
      <td>aberrant crypt foci</td>
      <td>Homo sapiens</td>
    </tr>
  </tbody>
</table>
</div>


