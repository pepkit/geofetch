import logging
import os
import re
from datetime import datetime, timedelta

import coloredlogs
import requests
import xmltodict

from .const import (
    DATE_FILTER,
    ETOOLS_ENDING,
    ETOOLS_GEO_GSE_BASE,
    RETMAX,
    THREE_MONTH_FILTER,
    TODAY_DATE,
)

__author__ = "Oleksandr Khoroshevskyi"

_LOGGER = logging.getLogger("__name__")
coloredlogs.install(
    logger=_LOGGER,
    datefmt="%H:%M:%S",
    fmt="[%(levelname)s] [%(asctime)s] %(message)s",
)


class Finder:
    """Class for finding GSE accessions in special period of time.

    Additionally, user can add specific filters for the search,
    while initialization of the class.
    """

    def __init__(self, filters: str = None, retmax: int = RETMAX):
        """Initialize Finder.

        Args:
            filters: Filters that have to be added to the query.
                Filter Patterns can be found here:
                https://www.ncbi.nlm.nih.gov/books/NBK3837/#EntrezHelp.Using_the_Advanced_Search_Pag.
            retmax: Maximum number of retrieved accessions.
        """
        self.query_customized_ending = ETOOLS_ENDING.format(retmax=retmax)
        self.query_filter_str = self._create_filter_str(filters)
        self.last_result = []

    def get_gse_all(self) -> list:
        """Get list of all gse accession available in GEO.

        Returns:
            List of gse accession.
        """
        return self.get_gse_id_by_query(url=self._compose_url())

    def get_gse_last_3_month(self) -> list:
        """Get list of gse accession that were uploaded or updated in last 3 month.

        Returns:
            List of gse accession.
        """
        return self.get_gse_id_by_query(url=self._compose_url(THREE_MONTH_FILTER))

    def get_gse_last_week(self) -> list:
        """Get list of gse accession that were uploaded or updated in last week.

        Returns:
            List of gse accession.
        """
        return self.get_gse_by_day_count(7)

    def get_gse_by_day_count(self, n_days: int = 1) -> list:
        """Get list of gse accessions that were uploaded or updated in last X days.

        Args:
            n_days: Number of days from now [e.g. 5].

        Returns:
            List of gse accession.
        """
        today = datetime.today()
        start_date = today - timedelta(days=n_days)
        start_date_str = start_date.strftime("%Y/%m/%d")
        return self.get_gse_by_date(start_date_str)

    def get_gse_by_date(self, start_date: str, end_date: str = None) -> list:
        """Search gse accessions by providing start date and end date.

        By default, the last date is today.

        Args:
            start_date: The oldest date of update (from YYYY/MM/DD to now) [input format: 'YYYY/MM/DD'].
            end_date: The nearest date of update (from __ to YYYY/MM/DD) [input format: 'YYYY/MM/DD'].

        Returns:
            List of gse accessions.
        """
        if end_date is None:
            end_date = TODAY_DATE
        new_date_filter = DATE_FILTER.format(start_date=start_date, end_date=end_date)
        return self.get_gse_id_by_query(url=self._compose_url(new_date_filter))

    def get_gse_id_by_query(self, url: str) -> list:
        """Run esearch (ncbi search tool) by specifying URL and retrieve gse list result.

        Args:
            url: Url of the query.

        Returns:
            List of gse ids.
        """
        uids_list = self._run_search_query(url)
        gse_id_list = [self.uid_to_gse(d) for d in uids_list]
        self.last_result = gse_id_list
        return gse_id_list

    @staticmethod
    def uid_to_gse(uid: str) -> str:
        """Convert UID to GSE accession.

        Args:
            uid: Uid string (Unique Identifier Number in GEO).

        Returns:
            GSE id string.
        """
        uid_regex = re.compile(r"[1-9]+0+([1-9]+[0-9]*)")
        return "GSE" + uid_regex.match(uid).group(1)

    @staticmethod
    def find_differences(old_list: list, new_list: list) -> list:
        """Compare 2 lists and search for elements that are not in old list.

        Args:
            old_list: Old list of elements.
            new_list: New list of elements.

        Returns:
            List of elements that are not in old list but are in new_list.
        """
        return list(set(new_list) - set(old_list))

    @staticmethod
    def _run_search_query(url: str) -> list:
        """Run get request and return list of uids found.

        Args:
            url: Url of the query.

        Returns:
            List of UIDs.
        """
        x = requests.get(url)
        if x.status_code != 200:
            _LOGGER.error("Request status != 200. Error. Check your request")
            return []
        try:
            x_result = xmltodict.parse(x.text)["eSearchResult"]
            _LOGGER.info(f"Found elements: {x_result['Count']}")
            _LOGGER.info(f"Additional information: {x_result['TranslationSet']}")
            if isinstance(x_result["IdList"]["Id"], list):
                return x_result["IdList"]["Id"]
            else:
                return [x_result["IdList"]["Id"]]
        except Exception:
            return []

    @staticmethod
    def _create_filter_str(filters: str = None) -> str:
        """Tune filter for url request.

        Args:
            filters: Filter should look like here: https://www.ncbi.nlm.nih.gov/books/NBK3837/#EntrezHelp.Using_the_Advanced_Search_Pag.

        Returns:
            Tuned filter string.
        """
        if filters == "" or filters is None:
            return ""
        return f"+(AND+{filters})"

    def _compose_url(self, date_filter: str = None) -> str:
        """Compose final url by adding date filter.

        Args:
            date_filter: Date filter that has to be used in the query.

        Returns:
            String of final url.
        """
        if date_filter is None:
            date_filter = ""

        return f"{ETOOLS_GEO_GSE_BASE}{self.query_filter_str}{date_filter}{self.query_customized_ending}"

    def generate_file(self, file_path: str, gse_list: list = None):
        """Save the list of GSE accessions stored in this Finder object to a given file.

        Args:
            file_path: Root to the file where gse accessions have to be saved.
            gse_list: List of gse accessions.
        """
        if gse_list is None:
            gse_list = self.last_result
        file_dir = os.path.split(file_path)[0]
        if not os.path.exists(file_dir) and file_dir != "":
            _LOGGER.error(f"Path: '{file_dir}' does not exist! No file will be saved")

        with open(file_path, "w") as fp:
            for item in gse_list:
                fp.write("%s\n" % item)
            _LOGGER.info("File has been saved!")
