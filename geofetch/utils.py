""" Independently-importable utilities to circumvent true scripts. """

import logging
import os
import subprocess


__author__ = "Vince Reuter"
__email__ = "vreuter@virginia.edu"


_LOGGER = logging.getLogger(__name__)


# This dict provides NCBI lookup URLs for different accession types. SRX
# identifiers can be used to grab metadata from SRA for a single sample, just as
# an SRP identifier is used to grab the same table for multiple samples, so
# these accessions are the same.
URL_BY_ACC = {
    "GSE": "http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?targ=gse&acc={ACCESSION}&form=text&view=full",
    "GSM": "http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?targ=gsm&acc={ACCESSION}&form=text&view=full",
    "SRP": "http://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?save=efetch&db=sra&rettype=runinfo&term={ACCESSION}",
    "SRX": "http://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?save=efetch&db=sra&rettype=runinfo&term={ACCESSION}"
}



def is_known_type(accn=None, typename=None):
    """
    Determine if the given accession is of a known type.

    :param str accn: accession of interest
    :param str typename: check this typename for known status rather
        than parsing an accession
    :return bool: whether the given accession is of a known type.
    :raise TypeError: if neither argument is provided or one/both are empty.
    """
    if not (accn or typename):
        raise TypeError("Specify either accession or accession typename")
    if typename:
        return isinstance(typename, str) and typename.upper() in URL_BY_ACC
    try:
        prefix, number = split_accn(accn)
        return prefix.upper() in URL_BY_ACC
    except:
        return False



class AccessionException(Exception):
    """ Exceptional condition(s) dealing with accession number(s). """

    def __init__(self, reason=""):
        """
        Optionally provide explanation for exceptional condition.

        :param str reason: some context or perhaps just a value that
            could not be interpreted as an accession
        """
        super(AccessionException, self).__init__(reason)



class Accession(object):
    """ Working with accession numbers. """

    _LOGGER = logging.getLogger("{}.{}".format(__name__, "Accession"))

    def __init__(self, accn, strict=True):
        """
        Create an instance with an accession and optionally a validation
        strictness flag.

        :param str accn: accession
        :param bool strict: strictness of the validation (whether to require
            that the accession type is known here)
        :raise AccessionException: if the given accession value isn't
            prefixed with three characters followed by an integer, or if
            strict validation is required and the accession type is unknown
        """
        typename, number = self._validate(accn)
        if strict and not is_known_type(accn):
            raise AccessionException(
                    "Unknown accession type for '{}': '{}'; "
                    "supported types: {}".format(
                            accn, typename, URL_BY_ACC.keys()))
        self.accn = accn
        self.typename = typename.upper()


    def fetch_metadata(self, outpath=None, typename=None):
        """
        Fetch the metadata associated with this accession.

        :param str outpath: path to file to which to write output, optional
        :param str typename: type indicating URL format, use type
            parsed at construction if unspecified
        """

        # TODO: note this sort of type-dependent strategy suggests subclassing.
        # For now, class is small, but that should maybe be done if it grows.

        typename = (typename or self.typename).upper()
        if not is_known_type(typename=typename):
            raise self.accn_type_exception(self.accn, typename)

        url_base = URL_BY_ACC[typename.upper()]
        format_kwargs = {"ACCESSION": self.accn}
        try:
            full_url = url_base.format(**format_kwargs)
        except KeyError:
            _LOGGER.error("Couldn't populate URL format '{}' with {}".
                          format(url_base, format_kwargs))
            raise
        _LOGGER.debug("Fetching: '%s'", full_url)

        if outpath:
            # Ensure we have filepath and that needed directories exist.
            if not os.path.splitext(outpath)[1]:
                _LOGGER.debug("Looks like folder, not file: %s", outpath)
                dirpath = outpath
                filename = "{}.csv".format(self.accn)
                outpath = os.path.join(dirpath, filename)
            else:
                dirpath = os.path.dirname(outpath)
            if not os.path.exists(dirpath):
                _LOGGER.debug("Forging path to '%s'", dirpath)
                os.makedirs(dirpath)
            cmd = "wget -O {} {}".format(outpath, full_url)
        else:
            cmd = "wget {}".format(full_url)

        subprocess.call(cmd.split(" "))


    @staticmethod
    def _validate(accn):
        """ Determine if given value looks like an accession. """
        typename, number = split_accn(accn)
        if len(typename) != 3:
            raise AccessionException(
                    "Not a three-character accession prefix: '{}' ('{}')".
                    format(accn, typename))
        try:
            number = int(number)
        except (TypeError, ValueError):
            raise AccessionException(
                    "Not an integral accession number: '{}' ('{}')".
                    format(accn, number))
        return typename, number


    @staticmethod
    def accn_type_exception(accn, typename, include_known=True):
        """
        Create an exception instance based on an accession and a
        parsed unknown typename.

        :param str accn: accession identifier from which unknown typename
            was parsed
        :param str typename: unknown typename that was parsed
        :param bool include_known: whether to include the known
            typenames in the exception message
        :return AccessionException: the exception instance
        """
        message = "Unknown accn type for '{}': '{}'".format(accn, typename)
        if include_known:
            message = "{}; known types: {}".format(
                message, URL_BY_ACC.keys())
        return AccessionException(message)



def split_accn(accn):
    """
    Split accession into prefix and number, leaving suffix as text
    and converting the type prefix to uppercase.

    :param str accn: ordinary accession identifier.
    :return str, str: prefix and integral suffix
    """
    typename, number_text = accn[:3], accn[3:]
    return typename.upper(), number_text
