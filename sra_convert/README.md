Converts `sra` data to `bam`.

* Download SRA data using `prefetch`. Actually, use `get_geo.py`.
* Set environment variables for `$SRARAW` (where `.sra` files will live) and `$SRABAM` (where `.bam` files will live).
* point `pconfig.yaml` to the annotation file produced by `get_geo.py`
* run the `sra_convert` pipeline using `looper`!

```
looper run pconfig.yaml
```

(You probably want to `--lump` these when you can).