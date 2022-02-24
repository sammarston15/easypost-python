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


""" get addresses from dad tool """
address1 = dad_tool.random_address('US_UT')
# print(json.dumps(address1, indent=4))
address2 = dad_tool.random_address('AU_VT')
# print(json.dumps(address2, indent=4))


""" create shipment """
shipment = easypost.Shipment.create(
  from_address = {
    "company": "example from company",
    "name": "example from name",
    "street1": address1['street1'],
    "street2": address1['street2'],
    "city": address1['city'],
    "state": address1['state'],
    "zip": address1['zip'],
    "country": address1['country'],
    "phone": "8008675309"
  },
  to_address = {
    "company": "example to company",
    "name": "example to name",
    "street1": address2['street1'],
    "street2": address2['street2'],
    "city": address2['city'],
    "state": address2['state'],
    "zip": address2['zip'],
    "country": address2['country'],
    "phone": "8008675309"
  },
  parcel={
    "length": 20.2,
    "width": 10.9,
    "height": 5,
    "weight": 65.9
  },
  customs_info = {
    'eel_pfc': 'NOEEI 30.37(a)',
    'customs_certify': True,
    'customs_signer': 'John Doe',
    'contents_type': 'merchandise',
    'customs_items': [
      {
        'contents_type': 'merchandise', 
        'description': 'blue shirt',
        'quantity': 1,
        'value': 11,
        'weight': 6,
        'hs_tariff_number': '610910',
        'origin_country': 'US'
      },
    ]
  },
  carrier_accounts = [os.getenv('dhl_express')],
  service = 'ExpressEasyNonDoc'
)
print('shipment: ')
print(shipment)

""" create pickup """
pickup = easypost.Pickup.create(
  address=shipment['from_address'],
  shipment=shipment,
  reference="my-first-pickup",
  min_datetime="2021-10-13 08:30:00",
  max_datetime="2021-10-14 08:30:00",
  is_account_address=False,
  instructions="example pickup instructions"
)
print('pickup: ')
print(pickup)

""" purchase pickup """
pickup.buy(carrier=pickup['pickup_rates'][0]['carrier'], service=pickup['pickup_rates'][0]['service'])
print('pickup buy attempt: ')
print(pickup)
