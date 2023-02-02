from ebaysdk.trading import Connection


if __name__ == '__main__':
    api = Connection(config_file="ebay.yaml", domain="api.sandbox.ebay.com", debug=True)
    request = {
        "Item": {
            "Title": "Soundtrack - House (Hausu) Exclusive LP",
            "Country": "US",
            "Location": "US",
            "Site": "US",
            "PictureDetails": "//cdn.shopify.com/s/files/1/0882/5118/products/Mickie-Yoshino-Hausu-Exclusive-Color-Vinyl-LP-2606903_large.jpg?v=166629649", 
            "ConditionID": "1000",
            "PaymentMethods": "CashOnPickup",
            "PrimaryCategory": {"CategoryID": "176985"},
            "Description": "Arthor",
            "ListingDuration": "Days_10",
            "StartPrice": "34.99",
            "Currency": "USD",
            "ReturnPolicy": {
                "ReturnsAcceptedOption": "ReturnsNotAccepted",
                # "RefundOption": "MoneyBack",
                # "ReturnsWithinOption": "Days_30",
                # "Description": "If you are not satisfied, return the keyboard.",
                # "ShippingCostPaidByOption": "Buyer"
            },
            "ShippingDetails": {
                "ShippingServiceOptions": {
                    "FreeShipping": "True",
                    "ShippingService": "USPSMedia"
                }
            },
            "DispatchTimeMax": "3",
            "ItemSpecifics": { 
                "NameValueList": [ 
                    {"Name": "Artist", "Value": "Mickie Yoshino"}, 
                    {"Name": "Release Title", "Value": "Soundtrack - House (Hausu) Exclusive LP"},
                    {"Name": "Format", "Value": "Vinyl"}
                    ] }
        }
    }

    # Verify add item to test first
    api.execute("AddItem", request)