# Changelog

## [0.12.6] -- 2024-02-05
- Updated support for Windows in Prefetch (Note: Some functionality may still be unavailable on Windows)

## [0.12.5] -- 2023-11-29
- Fixed bug, where description was not populated in PEP

## [0.12.4] -- 2023-08-01
- Fixed SRA convert
- Added how to convert SRA

## [0.12.3] -- 2023-06-21
- Fixed preserving order of project keys (#119)

## [0.12.2] -- 2023-04-25
- Added `max-prefetch-size` argument. #113
- Improved code and logger structure.

## [0.12.0] -- 2023-03-27
- Added functionality that saves gse metadata to config file
- Fixed description in initialization of pepy object

## [0.11.2] -- 2022-12-25
- Changed sample_name of PEP of processed files to file oriented
- Added `--max-soft-size` argument, that sets size limit of soft files
- - Added functionality that skips downloading GEO tables that are in soft files
- Fixed bug of creating unwanted empty folders
- Fixed problem with missing data

## [0.11.1] -- 2022-11-28
- Fixed requirements file
- Fixed bug in expanding metadata list
- Fixed bug in metadata links

## [0.11.0] -- 2022-10-26
- Added initialization of peppy Project without saving any files (from within Python using an API)
- Added Finder (searching GSE tool)
- Added progress bar
- Switched way of saving soft files to request library
- Improved documentation
- Refactored code
- Added `--add-convert-modifier` flag
- fixed looper amendments in the config file
- Fixed special character bug in the config file
- Fixed None issue in config file
- Fixed saving raw peps bug

## [0.10.1] -- 2022-08-04
- Updated metadata fetching requests from SRA database

## [0.10.0] -- 2022-07-07
- Fixed subprocesses continuing to run during program interrupt.
- Fixed issues with compatibility with NCBI API

## [0.9.0] -- 2022-06-20
- Updated `--pipeline-interface` argument that adds it in for looper. `--pipeline-interface` argument was divided into: 
`--pipeline-samples` and `--pipeline-project`.
- Fixed empty sample_name error while creating PEP.
- Added `--discard-soft` argument.
- Added `--const-limit-project` argument.
- Added `--const-limit-discard` argument.
- Added `--attr-limit-truncate` argument.
- Added `"--add-dotfile"` argument.
- Disabled creating combined pep when flag `--acc-anno` is set.
- Improved finding and separating metadata keys and genome assembly information.
- Added standardization of column names by replacing characters to lowercase and spaces by underscore.


## [0.8.0] -- 2022-03-10
- Added `--filter-size` argument.
- Added `--data-source` argument.
- Removed `--tar_re` argument.
- Added PEP for processed data.
- Updated regex filter (case-insensitive update).
- Changed way of downloading processed data (downloading each file separately).
- Fixed code errors.
- Separated sample and experiment processed data.


## [0.7.0] -- 2020-05-21
- Fixed user interface for bam conversions
- Added regex filter for processed data filenames, which will also auto-extract from tar archives
- Updated output to PEP 2.0
- Added `--skip` argument
- Added more control over where to store results.
- Integrate `sraconvert` into geofetch package.


## [0.6.0] -- 2019-06-20
- Fixed a bug with specifying a processed data output folder
- Added a pre-check and warning message for `prefetch` command 


## [0.5.0] -- 2019-05-09

- `geofetch` will now re-try a failed prefetch 3 times and warn if unsuccessful.
- Fixed a bug that prevented writing metadata in python3.
- More robust SOFT line parsing
- Use [`logmuse`](http://logmuse.databio.org/en/latest/) for messaging
- Improve modularity to facilitate non-CLI use if desired
- Better documentation

## [0.4.0] -- (2019-03-13)

- Fixed a bug with default generic config template
- Added `--version` option
- Improved python 3 compatibility

## [0.2.0] -- (2019-02-28)

- Fixed bugs that prevented install from pypi

## [0.1.0] -- (2019-02-27)

- First official release
- Enabled command-line usage
- Packaged `geofetch` for release on PyPI


## [0.0.0] -- (2017-10-24)
  
  - Legacy, unversioned development initiated
