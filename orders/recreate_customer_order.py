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

""" open the misc.JSON file - NOTE: os.getcwd() will give you a string of the path to the workspace folder, not the folder that the file is in necessarily. """
with open(os.path.join(os.getcwd(), 'misc.JSON'), 'r') as f:
  # convert JSON to Python "Dictionary"
  order = json.load(f)

  """ Delete unnecessary info """
  del order['public_id']
  del order['user']
  del order['user_id']
  del order['mode']
  del order['from_address']['id']
  del order['from_address']['object']
  del order['from_address']['created_at']
  del order['from_address']['updated_at']
  del order['from_address_id']
  del order['to_address']['id']
  del order['to_address']['object']
  del order['to_address']['created_at']
  del order['to_address']['updated_at']
  del order['to_address_id']
  del order['return_address']['id']
  del order['return_address']['object']
  del order['return_address']['created_at']
  del order['return_address']['updated_at']
  del order['return_address_id']
  del order['buyer_address']['id']
  del order['buyer_address']['object']
  del order['buyer_address']['created_at']
  del order['buyer_address']['updated_at']
  del order['buyer_address_id']

  if order['customs_info']:
    del order['customs_info']['id']
    del order['customs_info']['object']
    del order['customs_info']['created_at']
    del order['customs_info']['updated_at']
    del order['customs_info_id']

    for item in order['customs_info']['customs_items']:
      del item['id']
      del item['object']
      del item['created_at']
      del item['updated_at']

    

  for shipment in order['shipments']:
    del shipment['created_at']
    del shipment['messages']
    del shipment['mode']
    del shipment['from_address']['id']
    del shipment['from_address']['object']
    del shipment['from_address']['created_at']
    del shipment['from_address']['updated_at']
    del shipment['parcel']['id']
    del shipment['parcel']['object']
    del shipment['parcel']['created_at']
    del shipment['parcel']['updated_at']
    del shipment['parcel']['mode']
    del shipment['postage_label']
    del shipment['refund_status']
    del shipment['scan_form']
    del shipment['selected_rate']
    del shipment['tracker']
    del shipment['to_address']['id']
    del shipment['to_address']['object']
    del shipment['to_address']['created_at']
    del shipment['to_address']['updated_at']
    del shipment['return_address']['id']
    del shipment['return_address']['object']
    del shipment['return_address']['created_at']
    del shipment['return_address']['updated_at']
    del shipment['buyer_address']['id']
    del shipment['buyer_address']['object']
    del shipment['buyer_address']['created_at']
    del shipment['buyer_address']['updated_at']
    del shipment['_internal']
    del shipment['rates']
    del shipment['forms']
    del shipment['fees']
    del shipment['id']

    if shipment['customs_info']:
      del shipment['customs_info']['id']
      del shipment['customs_info']['object']
      del shipment['customs_info']['created_at']
      del shipment['customs_info']['updated_at']
      for item in shipment['customs_info']['customs_items']:
        del item['id']
        del item['object']
        del item['created_at']
        del item['updated_at']
    

  """ create unique reference ID """
  reference_id = str(uuid4())[:12]
    

  """ any additional adjustments """
  # for shipment in order['shipments']:
    # shipment['options']['print_custom_1'] = "print_custom_1"
    # shipment['options']['print_custom_2'] = "print_custom_2"
    # shipment['options']['print_custom_3'] = "print_custom_3"


""" recreate order """
try:
    new_order = client.order.create(
      to_address = order['to_address'],
      from_address = order['from_address'],
      # return_address = order['return_address'],
      # buyer_address = order['buyer_address'],
      shipments = order['shipments'],
      is_return = order['is_return'],
      reference = reference_id,
      options = order['options'],
      customs_info = order.get('customs_info', None), # this may need to come from the shipment level
      carrier_accounts = [os.getenv('FEDEX')]
    )

    """ Print response to the console """
    print(new_order)
    print("     ")
    print("     ")
    print("     ")
    print(new_order['id'])
    print("     ")
    print("     ")
    print("     ")

except easypost.errors.api.api_error.ApiError as e:
    print("   ")
    print(e.http_body)
    print("   ")


