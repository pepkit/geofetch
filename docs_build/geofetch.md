# Package geofetch Documentation

 Package-level data 
## Class Accession
Working with accession numbers.


## Class InvalidSoftLineException
Exception related to parsing SOFT line.


## Class OrderedDict
Dictionary that remembers insertion order


### add\_logging\_options
Augment a CLI argument parser with this package's logging options.
```python
def add_logging_options(parser)
```

**Parameters:**

- `parser` -- `argparse.ArgumentParser`:  CLI options and argument parser toaugment with logging options.


**Returns:**

`argparse.ArgumentParser`:  the input argument, supplemented with thispackage's logging options.




### expandpath
Expand a filesystem path that may or may not contain user/env vars.
```python
def expandpath(path)
```

**Parameters:**

- `path` -- `str`:  path to expand


**Returns:**

`str`:  expanded version of input path




### logger\_via\_cli
Convenience function creating a logger.

This module provides the ability to augment a CLI parser with
logging-related options/arguments so that client applications do not need
intimate knowledge of the implementation. This function completes that
lack of burden, parsing values for the options supplied herein.
```python
def logger_via_cli(opts, **kwargs)
```

**Parameters:**

- `opts` -- `argparse.Namespace`:  command-line options/arguments.


**Returns:**

`logging.Logger`:  configured logger instance.


**Raises:**

- `pararead.logs.AbsentOptionException`:  if one of the expected optionsisn't available in the given Namespace. Such a case suggests that a client application didn't use this module to add the expected logging options to a parser.




### main
Run the script.
```python
def main()
```




### parse\_SOFT\_line
Parse SOFT formatted line, returning a dictionary with the key-value pair.
```python
def parse_SOFT_line(l)
```

**Parameters:**

- `l` -- `str`:  A SOFT-formatted line to parse ( !key = value )


**Returns:**

`dict[str, str]`:  A python Dict object representing the key-value.


**Raises:**

- `InvalidSoftLineException`:  if given line can't be parsed as SOFT line




### parse\_accessions
Create a list of GSE accessions, either from file or a single value.

This will be a dict, with the GSE# as the key, and
corresponding value is a list of GSM# specifying the samples we're
interested in from that GSE#. An empty sample list means we should get all
samples from that GSE#. This loop will create this dict.
```python
def parse_accessions(input_arg, metadata_folder, just_metadata=False)
```

**Parameters:**

- `input_arg` -- ``: 
- `metadata_folder` -- `str`:  path to folder for accession metadata
- `just_metadata` -- `bool`:  whether to only process metadata, not theactual data associated with the accession




### run\_geofetch
Main script driver/workflow
```python
def run_geofetch(cmdl)
```




### safe\_echo
Returns an environment variable if it exists, or an empty string if not
```python
def safe_echo(var)
```




### update\_columns
Update the metadata associated with a particular experiment.

For the experiment indicated, this function updates the value (mapping), 
including new data and populating columns used by looper based on 
existing values in the mapping.
```python
def update_columns(metadata, experiment_name, sample_name, read_type)
```

**Parameters:**

- `metadata` -- `Mapping`:  the key-value mapping to update
- `experiment_name` -- `str`:  name of the experiment from which thesedata came and are associated; the key in the metadata mapping for which the value is to be updated
- `sample_name` -- `str`:  name of the sample with which these data areassociated
- `read_type` -- `str`:  usually "single" or "paired," an indication of thetype of sequencing reads for this experiment


**Returns:**

`Mapping`: 




### which
Returns the path to a program to make sure it exists
```python
def which(program)
```




### write\_annotation
Write metadata sheet out as an annotation file.
```python
def write_annotation(gsm_metadata, file_annotation, use_key_subset=False)
```

**Parameters:**

- `gsm_metadata` -- `Mapping`:  the data to write, parsed from a filewith metadata/annotation information
- `file_annotation` -- `str`:  the path to the file to write
- `use_key_subset` -- `bool`:  whether to use the keys present in themetadata object given (False), or instead use a fixed set of keys defined within this module (True)


**Returns:**

`str`:  path to file written




### write\_subannotation
Writes one or more tables to a given CSV filepath.
```python
def write_subannotation(tabular_data, filepath, column_names=None)
```

**Parameters:**

- `Iterable[Mapping]` -- `Mapping |`:  single KV pair collection, or collectionof such collections, to write to disk as tabular data
- `filepath` -- `str`:  path to file to write, possibly with environmentvariables included, e.g. from a config file
- `column_names` -- `Iterable[str]`:  collection of names for columns towrite


**Returns:**

`str`:  path to file written



