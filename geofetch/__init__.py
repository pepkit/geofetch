"""Package-level data."""

import coloredlogs
import logmuse

from geofetch.finder import Finder
from geofetch.geofetch import Geofetcher

__author__: list[str] = ["Oleksandr Khoroshevskyi", "Vince Reuter", "Nathan Sheffield"]
__all__: list[str] = ["Finder", "Geofetcher"]

_LOGGER = logmuse.init_logger("geofetch")
coloredlogs.install(
    logger=_LOGGER,
    datefmt="%H:%M:%S",
    fmt="[%(levelname)s] [%(asctime)s] %(message)s",
)
