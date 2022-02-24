import easypost
import os
from dotenv import load_dotenv
import json
import dad_tool

""" LOAD ENVIRONMENT VARIABLES """
load_dotenv()


""" LOAD TEST AND PROD API KEY """
test_key = os.getenv('test_key')
prod_key = os.getenv('prod_key')


""" SET TEST OR PROD API KEY """
easypost.api_key = test_key
# easypost.api_key = prod_key 


""" open misc.JSON file """
with open((os.path.join(os.getcwd(),'misc.JSON')), 'r') as f:
  ship = json.load(f)

  # DELETE UNNESSESSARY INFORMATION
  if ship['created_at']:
    del ship['created_at']
  if ship['messages']:
    del ship['messages']
  if ship['status']:
    del ship['status']
  if ship['tracking_code']:
    del ship['tracking_code']
  if ship['updated_at']:
    del ship['updated_at']
  if ship['batch_id']:
    del ship['batch_id']
  if ship['batch_status']:
    del ship['batch_status']
  if ship['batch_message']:
    del ship['batch_message']
  if ship['from_address']['id']:
    del ship['from_address']['id']
  if ship['from_address']['created_at']:
    del ship['from_address']['created_at']
  if ship['from_address']['updated_at']:
    del ship['from_address']['updated_at']
  if ship['parcel']['id']:
    del ship['parcel']['id']
  if ship['parcel']['created_at']:
    del ship['parcel']['created_at']
  if ship['parcel']['updated_at']:
    del ship['parcel']['updated_at']
  if ship['to_address']['id']:
    del ship['to_address']['id']
  if ship['to_address']['created_at']:
    del ship['to_address']['created_at']
  if ship['to_address']['updated_at']:
    del ship['to_address']['updated_at']
  if ship['return_address']['id']:
    del ship['return_address']['id']
  if ship['return_address']['created_at']:
    del ship['return_address']['created_at']
  if ship['return_address']['updated_at']:
    del ship['return_address']['updated_at']
  if ship['buyer_address']['id']:
    del ship['buyer_address']['id']
  if ship['buyer_address']['created_at']:
    del ship['buyer_address']['created_at']
  if ship['buyer_address']['updated_at']:
    del ship['buyer_address']['updated_at']
  if ship['rates']:
    del ship['rates']
  if ship['id']:
    del ship['id']
  if ship['order_id']:
    del ship['order_id']
  if ship['postage_label']:
    del ship['postage_label']
  if ship['tracker']:
    del ship['tracker']
  if ship['selected_rate']:
    del ship['selected_rate']
  if ship['scan_form']:
    del ship['scan_form']
  if ship['refund_status']:
    del ship['refund_status']
  if ship['mode']:
    del ship['mode']

  if ship['customs_info']:
    if ship['customs_info']['id']:
      del ship['customs_info']['id']
    if ship['customs_info']['created_at']:
      del ship['customs_info']['created_at']
    if ship['customs_info']['updated_at']:
      del ship['customs_info']['updated_at']
    for customs_item in ship['customs_info']['customs_items']:
      del customs_item['id']
      del customs_item['mode']
      del customs_item['created_at']
      del customs_item['updated_at']
    

  # print(json.dumps(ship['to_address'], ))

  """ any additional adjustments """
  # ship['options']['incoterm'] = "DDU"
  # ship['options']['label_format'] = "PDF"
  # ship['options']['label_date'] = "2022-02-28"
  # ship['to_address']['residential'] = False
  # ship['from_address']['company'] = "EasyPost"
  # address1 = dad_tool.random_address('US_UT')

  """ Set shipment object """
  shipment = easypost.Shipment.create(
    to_address=ship['to_address'],
    from_address=ship['from_address'],
    # from_address=address1,
    parcel=ship['parcel'],
    customs_info=ship['customs_info'],
    options=ship['options'],
    is_return=ship['is_return'],
    carrier_accounts=[os.getenv('fedex')]
  )

""" Buy Shipment """
shipment.buy(rate=shipment.lowest_rate())

""" Print shipment """
print(shipment)