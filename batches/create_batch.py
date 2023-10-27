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


""" create unique reference ID"""
reference_id = str(uuid4())[:12]


""" Create batch with existing shipments """
try:
  batch = client.batch.create(
    shipments=[
        {"id": "shp_..."},
        {"id": "shp_..."},
    ],
  )

  print(batch)

except easypost.errors.api.api_error.ApiError as e:
  print("   ")
  print(e.http_body)
  print("   ")


""" Create batch with blanket shipments """
try:
  batch = client.batch.create(
    shipments=[
        {
        "to_address": {
          "name": "Dr. Steve Brule",
          "street1": "179 N Harbor Dr",
          "city": "Redondo Beach",
          "state": "CA",
          "zip": "90277",
          "country": "US",
          "phone": "8573875756",
          "email": "dr_steve_brule@gmail.com"
        },
        "from_address": {
          "name": "EasyPost",
          "street1": "417 Montgomery Street",
          "street2": "5th Floor",
          "city": "San Francisco",
          "state": "CA",
          "zip": "94104",
          "country": "US",
          "phone": "4153334445",
          "email": "support@easypost.com"
        },
        "parcel": {
          "length": "20.2",
          "width": "10.9",
          "height": "5",
          "weight": "65.9"
        },
        "carrier": "USPS",
        "service": "ParcelSelect"
      }
    ],
  )

  print(batch)

except easypost.errors.api.api_error.ApiError as e:
  print("   ")
  print(e.http_body)
  print("   ")

