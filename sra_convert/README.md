# sraconvert

Converts `.sra` files to `.bam`.

## How to convert the `sra` files to `bam`

With `.sra` data downloaded, we now need to convert these files into a more usable format. The `sra_convert` pipeline can convert `.sra` files into `.bam` format using the `sratoolkit`. The *PEP* files produced by `geofetch` can be immediately plugged into this pipeline to handle this conversion for you, either locally or on a compute cluster.

1. Make sure you have [looper](https://pepkit.github.io/docs/looper/) installed.

2. `geofetch` produces a configuration file with a built-in subproject for `sra_convert`, so we can run this pipeline with no further modification by activating that subproject using the `--sp sra_convert` argument. Here's how to convert one of the above samples:

```
looper run ${CODE}sandbox/cohesin_dose/cohesin_dose_config.yaml -d --sp sra_convert --lump 10
```

Here's what this means:

-`looper run` tells looper to `run` the project
- `${CODE}sandbox/cohesin_dose/cohesin_dose_config.yaml` is the project config file produced by `geofetch`. you can use any [PEP-compatible](http://pepkit.github.io) file here.
- `-d` means dry-run, so it won't actually submit the jobs, just to see if it works. 
- `--sp sra_convert` activates the *subproject* (`sp`) called `sra_convert`, which is defined in your project config file. It's created automatically by `geofetch`. This subproject points the `pipeline_interfaces` to `sra_convert` so `looper` knows which pipeline to use.
- `-lump 10` will tell `looper` to lump jobs together until it accumulates 10 GB of input files. This creates individual jobs that take about an hour or so, instead of submitting lots of 5-10 minute jobs. This is useful if you're using a cluster.


## Next steps

Once you've converted, then you just need to run the actual pipeline. What pipeline do you want to run? Add the pipeline interface into the `metadata.pipeline_interfaces` section on the project config file:

```yaml
metadata:
  pipeline_interfaces: path/to/pipeline_interface
```
