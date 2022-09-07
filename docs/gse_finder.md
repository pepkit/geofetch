s a python package that provides functions to find and retrieve a list of GSE ([GEO](https://www.ncbi.nlm.nih.gov/geo/) accession number) by using NCBI searching tool.


### The main features of the geofetch Finder are:
- Find GEO accession numbers (GSE) of the project that were uploaded or updated in certain period of time.
- Use the same filter query as [GEO DataSets Advanced Search Builder](https://www.ncbi.nlm.nih.gov/gds/advanced) is using
- Save list of the GSEs to file (This file with geo can be used later in **[geofetch](http://geofetch.databio.org/en/latest/)**)
- Fast execution time
- Easy to use


___
## Tutorial

0) Initiale Finder object. 
```python
from geofetch import Finder
gse_obj = Finder()

# Optionally: provide filter string and max number of retrieve elements
gse_obj = Finder(filter="((bed) OR narrow peak) AND Homo sapiens[Organism]", retmax=10)
```

1) Get list of all GSE in GEO 
```python

gse_list =  gse_obj.get_gse_all()

```

2) Get list of GSE that were uploaded and updated last week
```python

gse_list = gse_obj.get_gse_last_week() 

```

3) Get list of GSE that were uploaded and updated last 3 month
```python

gse_list = gse_obj.get_gse_last_3_month()

```

4) Get list of GSE that were uploaded and updated in las *number of days*
```python

# project that were uploaded in last 5 days:
gse_list = gse_obj.get_gse_by_day_count(5)

```

5) Get list of GSE that were uploaded in certain period of time
```python

gse_list = gse_obj.get_gse_by_date(start_date="2015/05/05", end_date="2020/05/05")

```

6) Save last searched list of items to the file
```python

gse_obj.generate_file("path/to/the/file")

# if you want to save different list of files you can provide it to the funciton
gse_obj.generate_file("path/to/the/file", gse_list=["123", "124"])

```

7) Compare two lists:
```python

new_gse_list = gse_obj.find_differences(list1, list2)

```

----

More information about gse and queries and id:
- https://www.ncbi.nlm.nih.gov/geo/info/geo_paccess.html
- https://newarkcaptain.com/how-to-retrieve-ncbi-geo-information-using-apis-part1/
- https://www.ncbi.nlm.nih.gov/books/NBK3837/#EntrezHelp.Using_the_Advanced_Search_Pag