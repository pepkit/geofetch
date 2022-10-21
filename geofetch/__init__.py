""" Package-level data """
from .geofetch import *
from .finder import *
from ._version import __version__
import logmuse

logmuse.init_logger("geofetch")
