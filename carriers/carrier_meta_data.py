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
# client = easypost.EasyPostClient(test_key)
client = easypost.EasyPostClient(prod_key)


try:

    # Request all metadata for all carriers
    carrier_metadata = client.carrier_metadata.retrieve()

    # Request specific metadata for specific carriers
    carrier_metadata = client.carrier_metadata.retrieve(
        carriers=["usps"],
        types=["service_levels", "predefined_packages"],
    )

    print(carrier_metadata)

except easypost.errors.api.api_error.ApiError as e:
    print("   ")
    print(e.http_body)
    print("   ")
