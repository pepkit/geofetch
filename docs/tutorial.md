# <img src="../img/geofetch_logo.svg" class="img-header">  tutorial

## Download SRA data using `geofetch`

Before starting, make sure you've followed the [installation instructions](install.md). To see your options, display the help menu:

```console
geofetch -h
```

For example, run it like:

```console
geofetch -i GSE##### -m path/to/metadata/folder -n PROJECT_NAME
```

This will do 3 things:

1. download all `.sra` files from `GSE#####` into your SRA folder (wherever you have configured `sratools` to stick data).
2. produce a sample annotation sheet, `PROJECT_NAME_annotation.csv`, in your metadata folder
3. produce a project configuration file, `PROJECT_NAME_config.yaml`, in your metadata folder.


## Finalize the project config and sample annotation

That's basically it! `Geofetch` will have produced a general-purpose PEP for you, but you'll need to modify it for whatever purpose you have. For example, one common thing is to link to the pipeline you want to use by adding a `pipeline_interface` to the project config file. You may also need to adjust the `sample_annotation` file to make sure you have the right column names and attributes needed by the pipeline you're using. GEO submitters are notoriously bad at getting the metadata correct.

## A few real-world examples

```console
geofetch -i GSE95654 --just-metadata -n crc_rrbs -m '${CODE}sandbox'
geofetch -i GSE73215 --just-metadata -n cohesin_dose -m '${CODE}sandbox'
```

You'd next want to run these through a pipeline like this: 
```
looper run ${CODE}sandbox/cohesin_dose/cohesin_dose_config.yaml
```

or:

```
looper run ${CODE}sandbox/autism_microglia/autism_microglia_config.yaml -d
```

You can find a complete example of [using `geofetch` for RNA-seq data](https://github.com/databio/example-projects/tree/master/rna-seq). 


## Tips

* Set an environment variable for `$SRABAM` (where `.bam` files will live), and `geofetch` will check to see if you have an already-converted bamfile there before issuing the command to download the `sra` file. In this way, you can delete old `sra` files after conversion and not have to worry about re-downloading them. 

* The config template uses an environment variable `$SRARAW` for where `.sra` files will live. If you set this variable to the same place you instructed `sratoolkit` to download `sra` files, you won't have to tweak the config file. For more information refer to the [`sratools` page](howto-location.md).

