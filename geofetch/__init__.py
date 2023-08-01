""" Package-level data """
import logmuse

from geofetch.geofetch import *
from geofetch.finder import *
from geofetch._version import __version__


__author__ = ["Oleksandr Khoroshevskyi", "Vince Reuter", "Nathan Sheffield"]
__all__ = ["Finder", "Geofetcher"]

_LOGGER = logmuse.init_logger("geofetch")
coloredlogs.install(
    logger=_LOGGER,
    datefmt="%H:%M:%S",
    fmt="[%(levelname)s] [%(asctime)s] %(message)s",
)
