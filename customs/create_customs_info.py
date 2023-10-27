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


""" create customs item """
# try:
#   customs_item = client.customs_item.create(
#     description="T-shirt",
#     quantity=1,
#     value=10,
#     weight=5,
#     hs_tariff_number="123456",
#     origin_country="us",
#   )

#   print(customs_item)

# except easypost.errors.api.api_error.ApiError as e:
#   print("   ")
#   print(e.http_body)
#   print("   ")


""" create customs info """
try:
  customs_info = client.customs_info.create(
      eel_pfc="NOEEI 30.37(a)",
      customs_certify=True,
      customs_signer="Steve Brule",
      contents_type="merchandise",
      contents_explanation="",
      restriction_type="none",
      customs_items=[
          {
              "description": "Sweet shirts",
              "quantity": 2,
              "weight": 11,
              "value": 23,
              "hs_tariff_number": "654321",
              "origin_country": "US",
          }
      ],
  )

  print(customs_info)

except easypost.errors.api.api_error.ApiError as e:
  print("   ")
  print(e.http_body)
  print("   ")
