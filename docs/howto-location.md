
## Setting data download location with `sratools`

`geofetch` is using the [sratoolkit](https://trace.ncbi.nlm.nih.gov/Traces/sra/?view=toolkit_doc&f=std) to download raw data from SRA -- which means it's stuck with the [default path for downloading SRA data](http://databio.org/posts/downloading_sra_data.html), which I've written about. So before you run `geofetch`, make sure you have set up your download location to the correct place. In our group, we use a shared group environment variable called `${SRARAW}`, which points to a shared folder (`${DATA}/sra`) where the whole group has access to downloaded SRA data. You can point the `sratoolkit` (and therefore `geofetch`) to use that location with this one-time configuration code:

```
echo "/repository/user/main/public/root = \"$DATA\"" > ${HOME}/.ncbi/user-settings.mkfg
```

Now `sratoolkit` will download data into an `/sra` folder in `${DATA}`, which is what `${SRARAW}` points to.

If you are getting an error that the `.ncbi` folder does not exist in your home directory, you can just make a folder `.ncbi` with an empty file `user-settings.mkfg` and follow the same command above.
