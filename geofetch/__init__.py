""" Package-level data """
import logmuse

from geofetch.geofetch import *
from geofetch.finder import *
from geofetch._version import __version__


__author__ = ["Oleksandr Khoroshevskyi", "Vince Reuter", "Nathan Sheffield"]
__all__ = ["Finder", "Geofetcher"]

logmuse.init_logger("geofetch")
