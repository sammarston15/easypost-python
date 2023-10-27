import easypost # easypost python client library
import os # allows for access of environment variables in .env file
import json # allows for reading of JSON from misc.JSON file
from prettytable import PrettyTable # allows for formatted table printing in the console
from uuid import uuid4 # use this to generate a random and unique identifier
# import dad_tool # Justin Hammond's Dummy Address Data


""" LOAD TEST AND PROD API KEY """
test_key = os.getenv('TEST_KEY')
prod_key = os.getenv('PROD_KEY')
personal_test_key = os.getenv('PERSONAL_TEST_KEY')


""" SET API KEY """
client = easypost.EasyPostClient(test_key)


try:
    shipment_details = {
        "to_address": {
            "name": "Dr. Steve Brule",
            "street1": "179 N Harbor Dr",
            "city": "Redondo Beach",
            "state": "CA",
            "zip": "90277",
            "country": "US",
            "phone": "4153334444",
            "email": "dr_steve_brule@gmail.com",
        },
        "from_address": {
            "name": "EasyPost",
            "street1": "417 Montgomery Street",
            "street2": "5th Floor",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94104",
            "country": "US",
            "phone": "4153334444",
            "email": "support@easypost.com",
        },
        "parcel": {
            "length": 20.2,
            "width": 10.9,
            "height": 5,
            "weight": 65.9,
        },
    }

    rates = client.beta_rate.retrieve_stateless_rates(**shipment_details)
    print(rates)

except easypost.errors.api.api_error.ApiError as e:
    print("   ")
    print(e.http_body)
    print("   ")