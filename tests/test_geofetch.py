from geofetch.geofetch import parse_accessions


def test_accessions():
	parse_accessions("GSE12345", None)
	assert(True)

