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


test_tracking_codes = {
  "pre_transit": "EZ1000000001",
  "in_transit": "EZ2000000002",
  "out_for_delivery": "EZ3000000003",
  "delivered": "EZ4000000004",
  "return_to_sender": "EZ5000000005",
  "failure": "EZ6000000006",
  "unknown": "EZ7000000007"
}

""" create a tracker """
try:
  tracker = client.tracker.create(
    # tracking_code=test_tracking_codes['out_for_delivery'],
    tracking_code="EZ1000000001",
    carrier="USPS",
  )

  print(tracker)

except easypost.errors.api.api_error.ApiError as e:
  print("   ")
  print(e.http_body)
  print("   ")
