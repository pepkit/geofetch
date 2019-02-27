
## How to build a PEP from SRA or GEO data

1. You must have the `sratoolkit` from NCBI installed, with tools in your `PATH` (check to make sure you can run `prefetch`). Make sure it's configured to store `sra` files where you want them. For more information, see [how to change sratools download location](howto-location.md).

2. Download SRA data using `geofetch`. To see full options, see the help menu with:

```console
geofetch -h
```

For example, run it like:

```console
geofetch -i GSE##### -m path/to/metadata/folder -n PROJECT_NAME
```

This will do 3 things:

1. download all `.sra` files from `GSE#####` into your SRA folder (wherever you have configured `sratools` to stick data).
2. produce a sample annotation sheet (currently called `PROJECT_NAME_annotation.csv` in your metadata folder), which is what you will use as part of your PEP.
3. produce a project configuration file (`PROJECT_NAME_config.yaml`) in your metadata folder.

Here are some other examples:

```console
geofetch -i GSE95654 --just-metadata -n crc_rrbs -m '${CODE}sandbox'
geofetch -i GSE73215 --just-metadata -n cohesin_dose -m '${CODE}sandbox'
```

Once you've produced your PEP annotation files and downloaded your SRA data, you should go check out the config files and annotation sheets and make sure they make sense to you. Then, you're ready to run pipelines on the data! The next thing is to convert the `sra` data into a format that can be used by pipelines, which we go over in the next section.

