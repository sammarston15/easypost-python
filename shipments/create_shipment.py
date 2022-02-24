import easypost
import os
from dotenv import load_dotenv
import dad_tool

# LOAD ENVIRONMENT VARIABLES
load_dotenv()

# SET TEST AND PROD API KEY
test_key = os.getenv('test_key')
prod_key = os.getenv('prod_key')


# USE TEST OR PROD API KEY
easypost.api_key = test_key
# easypost.api_key = prod_key


""" Create DAD addresses """
unitedstates1 = dad_tool.random_address('US_UT')
unitedstates2 = dad_tool.random_address('US_AZ')
unitedkingdom1 = dad_tool.random_address('EU_UK')
unitedkingdom2 = dad_tool.random_address('EU_UK')
canada1 = dad_tool.random_address('CA_BC')
canada2 = dad_tool.random_address('CA_BC')


""" Create to_address """
try:
    to_address = easypost.Address.create(
        street1=unitedstates1['street1'],
        street2=unitedstates1['street2'],
        city=unitedstates1['city'],
        state=unitedstates1['state'],
        zip=unitedstates1['zip'],
        country=unitedstates1['country'],
        company="Example Destination",
        phone="415-456-7890",
        email='toaddress@email.com'
    )
except easypost.Error as e:
    print(e.http_body)


""" Create from_address """
try:
    from_address = easypost.Address.create(
        street1=unitedstates2['street1'],
        street2=unitedstates2['street2'],
        city=unitedstates2['city'],
        state=unitedstates2['state'],
        zip=unitedstates2['zip'],
        country=unitedstates2['country'],
        company="EasyPost",
        phone="415-456-7890",
        email='fromaddress@email.com'
    )
except easypost.Error as e:
    print(e.http_body)

""" Create parcel """
try:
  parcel = easypost.Parcel.create(
    length=9,
    width=6,
    height=2,
    weight=10
  )
except easypost.Error as e:
  print(e.http_body)


# customs_info = easypost.CustomsInfo.create(...)

""" Create shipment """
shipment = easypost.Shipment.create(
  to_address=to_address,
  from_address=from_address,
  parcel=parcel,
  # customs_info=customs_info
  carrier_accounts = [os.getenv('usps')]
)

""" Buy shipment """
# shipment.buy(rate=shipment.lowest_rate())

"""Print shipment to the console """
print(shipment)






# OR in one call

# shipment = easypost.Shipment.create(
#   to_address={
#     "name": 'John Doe',
#     "street1": '415 Brunswick Ave',
#     "city": 'Toronto',
#     "state": 'ON',
#     "zip": '90277',
#     "country": 'CA',
#     "phone": '4153334444',
#     "email": 'johndoe@gmail.com'
#   },
#   from_address={
#     "name": 'EasyPost',
#     "street1": '417 Montgomery Street',
#     "street2": '5th Floor',
#     "city": 'San Francisco',
#     "state": 'CA',
#     "zip": '94104',
#     "country": 'US',
#     "phone": '4153334444',
#     "email": 'support@easypost.com'
#   },
#   parcel={
#     "length": 20.2,
#     "width": 10.9,
#     "height": 5,
#     "weight": 65.9
#   },
#   customs_info = {
#     'eel_pfc': 'NOEEI 30.37(a)',
#     'customs_certify': True,
#     'customs_signer': 'John Doe',
#     'contents_type': 'merchandise',
#     'customs_items': [
#       {
#         'contents_type': 'merchandise', 
#         'description': 'T-shirt',
#         'quantity': 1,
#         'value': 11,
#         'weight': 6,
#         'hs_tariff_number': '610910',
#         'origin_country': 'US'
#       },

#     ]
#   },
  
#   carrier_accounts = [os.getenv('usps')]
# )
# print(shipment)