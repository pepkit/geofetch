# A start-to-finish example

Let's take a GEO project from start to finish.


1. *Download* the data

    ```
    geofetch -i GSE95654 --just-metadata -n crc_rrbs -m '${CODE}sandbox'
    ```

2. *Finalize project config*. Link to the pipeline you want to use by adding a `pipeline_interface` to the project config file produced by `geofetch`. Make any other configuration adjustments to your project.

3. *Finalize sample annotation*. Adjust the `sample_annotation` file to make sure you have the right column names and attributes needed by the pipeline you're using. Make sure the `protocol` column matches the pipeline's `protocol` -- GEO submitters are notoriously bad at getting the metadata correct. For example,  this project lists the protocol as 'other' instead of as 'ATAC', so we have to manually correct it in the sample annotation file.

4. *Run* your pipeline:

    ```
    looper run ${CODE}sandbox/cohesin_dose/cohesin_dose_config.yaml
    ```

    or:

    ```
    looper run ${CODE}sandbox/autism_microglia/autism_microglia_config.yaml -d
    ```

## Tips

* Set an environment variable for `$SRABAM` (where `.bam` files will live), and `geofetch` will check to see if you have an already-converted bamfile there before issuing the command to download the `sra` file. In this way, you can delete old `sra` files after conversion and not have to worry about re-downloading them. 

* The config template uses an environment variable `$SRARAW` for where `.sra` files will live. If you set this variable to the same place you instructed `sratoolkit` to download `sra` files, you won't have to tweak the config file.
