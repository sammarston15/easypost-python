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

""" open the misc.JSON file - NOTE: os.getcwd() will give you a string of the path to the workspace folder, not the folder that the file is in necessarily. """
with open(os.path.join(os.getcwd(), 'misc.JSON'), 'r') as f:
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

    

  """ Get carrier account """
  carriers = [os.getenv('dhl_express')]
  # print(carrier, type(carrier))

  """ any additional adjustments """
  

  """ Create order """
  new_order = easypost.Order.create(
    to_address = order['to_address'],
    from_address = order['from_address'],
    return_address = order['return_address'],
    shipments = order['shipments'],
    is_return = order['is_return'],
    reference = order['reference'],
    # options = order['options'],
    customs_info = order['customs_info'],
    carrier_accounts = carriers
  )
  print(new_order)