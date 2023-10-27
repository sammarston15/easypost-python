import easypost # easypost python client library
import os # allows for access of environment variables in .env file
import json # allows for reading of JSON from misc.JSON file
from prettytable import PrettyTable # allows for formatted table printing in the console
from uuid import uuid4 # use this to generate a random and unique identifier
import dad_tool # Justin Hammond's Dummy Address Data
# import random


""" SET TEST AND PROD API KEY """
test_key = os.getenv('TEST_KEY')
personal_test_key = os.getenv('PERSONAL_TEST_KEY')
prod_key = os.getenv('PROD_KEY')


""" set client with TEST OR PROD api key """
# client = easypost.EasyPostClient(personal_test_key)
client = easypost.EasyPostClient(test_key)
# client = easypost.EasyPostClient(prod_key)


""" Create to_address """
to_address = {
    "street1":"417 Montgomery Street",
    "street2":"FLOOR 5",
    "city":"San Francisco",
    "state":"CA",
    "zip":"94104",
    "country":"US",
    "company":"EasyPost",
    "phone":"415-456-7890"
}

""" Create from_address """
from_address = {
    "name":"Dr. Steve Brule",
    "street1":"179 N Harbor Dr",
    "street2":"Redondo Beach",
    "city":"San Francisco",
    "state":"CA",
    "zip":"90277",
    "country":"US",
    "phone":"310-808-5243"
}


""" Create order """
try: 
    order = client.order.create(
        to_address={"id": "adr_..."},
        from_address={"id": "adr_..."},
        shipments=[
            {
                "parcel": {
                    "predefined_package": "FedExBox",
                    "weight": 10.2,
                }
            },
            {
                "parcel": {
                    "predefined_package": "FedExBox",
                    "weight": 17.5,
                }
            },
        ],
        carrier_accounts=[os.getenv('USPS')],
        reference=str(uuid4())[:12]
    )

    print(order)

except easypost.errors.api.api_error.ApiError as e:
    print("   ")
    print(e.http_body)
    print("   ")


""" buy order """
# try:
#     bought_order = client.order.buy(
#         order.id,
#         carrier="FedEx",
#         service="FEDEX_GROUND",
#     )

#     print(order)

# except easypost.errors.api.api_error.ApiError as e:
#     print("   ")
#     print(e.http_body)
#     print("   ")