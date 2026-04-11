"""Package-level data."""

from importlib.metadata import PackageNotFoundError, version

from geofetch.finder import Finder
from geofetch.geofetch import Geofetcher

__author__: list[str] = ["Oleksandr Khoroshevskyi", "Vince Reuter", "Nathan Sheffield"]

try:
    __version__: str = version("geofetch")
except PackageNotFoundError:
    __version__ = "unknown"

__all__: list[str] = ["Finder", "Geofetcher", "__version__"]
