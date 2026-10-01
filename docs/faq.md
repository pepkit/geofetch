# FAQ


## I get an error: `geofetch: command not found` after installing. Why isn't the `geofetch` executable in my path?


By default, Python packages are installed to `~/.local/bin`. You can add this location to your path by appending it:

```
export PATH=$PATH:~/.local/bin
```

Add this line to your `.bashrc` or `.profile` to make it permanent.
