from ebaysdk.trading import Connection


if __name__ == '__main__':
    api = Connection(config_file="ebay.yaml", domain="api.sandbox.ebay.com", debug=True)
    request = {
        # "AdminEndedItemsOnly": False,
        # "CategoryID": "176985",
        # "EndTimeFrom": "08/04/2022 01:37 AM",
        # "EndTimeTo": "08/07/2022 01:37 AM",
        # "GranularityLevel"
        # "IncludeVariations"
        # "IncludeWatchCount"
        # "MotorsDealerUsers"
        # "Pagination"
        # "SKUArray"
        # "Sort"
        "StartTimeFrom": "2022-08-04T21:59:59.005Z",
        "StartTimeTo": "2022-08-08T04:16:59.005Z",
    }

    api.execute("GetSellerList", request)