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


""" buy shipment """
try:
      shipment = client.shipment.retrieve("shp_...")

      print('attempting to purchase shipment...')
      print("     ")
      print("     ")
      print("     ")

  
      bought_shipment = client.shipment.buy(
        shipment['id'],
        rate=shipment.lowest_rate(),
        # rate=shipment.lowest_rate(['USPS'], ['PriorityMailInternational']),
        # insurance=249.99,
      )

      """ print shipment if buy is successful """
      print(bought_shipment)
      print("     ")
      print("     ")
      print("     ")
      print("shipment: ", bought_shipment['id'])
      print("     ")
      print("label:", bought_shipment['postage_label'].get('label_url', 'no label URL...') if bought_shipment['postage_label'] else 'no postage label object...')
      print("     ")
      print("commercial invoice:\n", bought_shipment['forms'][0].get('form_url', 'no form URL...') if bought_shipment['forms'] else 'no forms object...')
      print("     ")
      print("     ")

except easypost.errors.api.api_error.ApiError as e:
    print("   ")
    print(e.http_body)
    print("   ")

