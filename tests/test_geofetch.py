from geofetch import parse_accessions
import pytest


@pytest.mark.skip("Not implemented")
def test_accessions():
    parse_accessions("GSE12345", None)
    assert True
