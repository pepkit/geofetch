"""Package-level data."""

from importlib.metadata import PackageNotFoundError, version

import coloredlogs
import logmuse

from geofetch.finder import Finder
from geofetch.geofetch import Geofetcher

__author__: list[str] = ["Oleksandr Khoroshevskyi", "Vince Reuter", "Nathan Sheffield"]

try:
    __version__: str = version("geofetch")
except PackageNotFoundError:
    __version__ = "unknown"

__all__: list[str] = ["Finder", "Geofetcher", "__version__"]

_LOGGER = logmuse.init_logger("geofetch")
coloredlogs.install(
    logger=_LOGGER,
    datefmt="%H:%M:%S",
    fmt="[%(levelname)s] [%(asctime)s] %(message)s",
)
