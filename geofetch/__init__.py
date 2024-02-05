""" Package-level data """

import logmuse
import coloredlogs

from geofetch.geofetch import Geofetcher
from geofetch.finder import Finder
from geofetch._version import __version__


__author__ = ["Oleksandr Khoroshevskyi", "Vince Reuter", "Nathan Sheffield"]
__all__ = ["Finder", "Geofetcher", "__version__"]

_LOGGER = logmuse.init_logger("geofetch")
coloredlogs.install(
    logger=_LOGGER,
    datefmt="%H:%M:%S",
    fmt="[%(levelname)s] [%(asctime)s] %(message)s",
)
