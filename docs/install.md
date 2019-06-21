# Installing geofetch

## Prerequisites

You must have the [sratoolkit from NCBI](https://www.ncbi.nlm.nih.gov/books/NBK158900/) installed, with the tools in your PATH. Once it's installed, you should check to make sure you can run `prefetch`. Also, make sure it's configured to store SRA files where you want them. For more information, see how to change sratools download location.

## Setting data download location for `sratools`

`geofetch` is using the [sratoolkit](https://trace.ncbi.nlm.nih.gov/Traces/sra/?view=toolkit_doc&f=std) to download raw data from SRA -- which means it's stuck with the [default path for downloading SRA data](http://databio.org/posts/downloading_sra_data.html), which is in your home directory. So before you run `geofetch`, make sure you have set up your download location to the correct place. In our group, we use a shared group environment variable called `${SRARAW}`, which points to a shared folder (`${DATA}/sra`) where the whole group has access to downloaded SRA data. You can point the `sratoolkit` (and therefore `geofetch`) to use that location with this one-time configuration code:

```
echo "/repository/user/main/public/root = \"$DATA\"" > ${HOME}/.ncbi/user-settings.mkfg
```

Now `sratoolkit` will download data into an `/sra` folder in `${DATA}`, which is what `${SRARAW}` points to.

If you are getting an error that the `.ncbi` folder does not exist in your home directory, you can just make a folder `.ncbi` with an empty file `user-settings.mkfg` and follow the same command above.

## Installing geofetch

Releases are posted as [GitHub releases](https://github.com/pepkit/geofetch/releases), or you can install from PyPI using `pip`:

```bash
pip install geofetch
```

Confirm it was successful by running it on the command line:

```console
geofetch --help
```

If the executable in not in your $PATH, append this to your `.bashrc` or `.profile` (or `.bash_profile` on macOS):

```
export PATH=~/.local/bin:$PATH
```
