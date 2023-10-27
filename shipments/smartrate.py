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



""" attempt to fetch smartrates """
try:
    """ retrieve shipment """
    # shipment = client.shipment.retrieve("shp_...")
    shipment = client.shipment.create( # testing for a ticket
            to_address = {
              "name": 'Keebsforall Warehouse',
              "street1": '11718 Folkstone Lane',
              "street2": '',
              "city": 'Toronto',
              "state": 'ON',
              "zip": 'M3J1L6',
              "country": 'Canada',
              "phone": '4245271905',
              "email": 'mhashirhassan22@gmail.com'
            },
            from_address = {
              "street1": "1725 E Broadway",
              "street2": "",
              "city": "Vancouver",
              "state": "BC",
              "zip": "V5N 1V9",
              "country": "CA"
            },
            parcel={
                "weight": 2
            },
            carrier_accounts=[
                {
                    "id": os.getenv('UPS')
                },
                {
                    "id": os.getenv('USPS')
                }
            ]
        )

    print("     ")
    print(f"attempting to get smartrates for {shipment['id']}...")
    print("     ")
    print("     ")
    print("     ")

    """ get smartrates """
    smart_rates = client.shipment.get_smart_rates(shipment['id'])

    print(smart_rates)

except easypost.errors.api.api_error.ApiError as e:
    print("   ")
    print(e.http_body)
    print("   ")


except Exception as e:
    print("ERROR:")
    print(e)