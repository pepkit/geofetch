# Changelog

## [0.9.0] -- 2022-06-20
- Updated New pipeline interface.
- Fixed error sample_name error when title does not exist.
- Added `--discard-soft` argument.
- Added `--const-limit-project` argument.
- Added `--const-limit-discard` argument.
- Added `--attr-limit-truncate` argument.
- Added `"--add-dotfile"` argument.
- Disabled creating combined pep when flag `--acc-anno` is set.
- Improved finding and separating metadata keys and genotype information
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
