import easypost
import os
from dotenv import load_dotenv
import json


""" LOAD ENVIRONMENT VARIABLES """
load_dotenv()


""" LOAD TEST AND PROD API KEY """
test_key = os.getenv('test_key')
prod_key = os.getenv('prod_key')


""" SET TEST OR PROD API KEY """
easypost.api_key = test_key
# easypost.api_key = prod_key


batch = easypost.Batch.create(shipments=[
  {
    "from_address": {
      "street1": "417 MONTGOMERY ST",
      "street2": "FLOOR 5",
      "city": "SAN FRANCISCO",
      "state": "CA",
      "country": "US",
      "zip": "94104"
    },
    "to_address": {
      "street1": "10231 Ridge Road",
      "street2": "",
      "city": "North Royalton",
      "state": "OH",
      "country": "US",
      "zip": "44133",
      "name": "School of Fine Art"
    },
    "parcel": {
      "length": "1.0",
      "width": "1.0",
      "height": "1.0",
      "weight": "1.0"
    },
    "reference": "1",
    "carrier": "USPS",
    "service": "Express"
  }, 
  {
    "from_address": {
      "street1": "417 MONTGOMERY ST",
      "street2": "FLOOR 5",
      "city": "SAN FRANCISCO",
      "state": "CA",
      "country": "US",
      "zip": "94104"
    },
    "to_address": {
      "street1": "10231 Ridge Road",
      "street2": "",
      "city": "North Royalton",
      "state": "OH",
      "country": "US",
      "zip": "44133",
      "name": "School of Fine Art"
    },
    "parcel": {
      "length": "1.0",
      "width": "1.0",
      "height": "1.0",
      "weight": "1.0"
    },
    "reference": "1",
    "carrier": "USPS",
    "service": "Express"
  },
])
print(batch)