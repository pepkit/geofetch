from geofetch import Geofetcher


if __name__ == "__main__":
    # Create a Geofetcher instance
    geofetcher = Geofetcher(
        "GSE15805", "./test/", "./test/", just_metadata=True, processed=True
    )

    # Fetch the data
    data = geofetcher.fetch_all("GSE15805")

    # Print the fetched data
    print(data)
