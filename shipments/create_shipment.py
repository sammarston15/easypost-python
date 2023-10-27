import easypost # easypost python client library
import os # allows for access of environment variables in .env file
import json # allows for reading of JSON from misc.JSON file
from prettytable import PrettyTable # allows for formatted table printing in the console
from uuid import uuid4 # use this to generate a random and unique identifier
import dad_tool # Justin Hammond's Dummy Address Data
# import random
import string


# SET TEST AND PROD API KEY
test_key = os.getenv('TEST_KEY')
personal_test_key = os.getenv('PERSONAL_TEST_KEY')
prod_key = os.getenv('PROD_KEY')
rick = os.getenv('RICK_CARTER_PROD_KEY')



# USE TEST OR PROD API KEY
# client = easypost.EasyPostClient(personal_test_key)
client = easypost.EasyPostClient(test_key)
# client = easypost.EasyPostClient(prod_key)


""" Create DAD addresses """
unitedstates1 = dad_tool.random_address('US_UT')
unitedstates2 = dad_tool.random_address('US_AZ')
unitedkingdom1 = dad_tool.random_address('EU_UK')
unitedkingdom2 = dad_tool.random_address('EU_UK')
canada1 = dad_tool.random_address('CA_BC')
canada2 = dad_tool.random_address('CA_BC')


""" create unique reference ID"""
reference_id = str(uuid4())[:12]


""" Create to_address """
to_address = {
    "street1": canada1['street1'],
    "street2": canada1['street2'],
    "city": canada1['city'],
    "state": canada1['state'],
    "zip": canada1['zip'],
    "country": canada1['country'],
    "company": "Example Destination",
    "phone": "415-456-7890",
    "email": 'toaddress@email.com',
    "residential": True
}


""" Create from_address """
from_address = {
    "street1": unitedstates1['street1'],
    "street2": unitedstates1['street2'],
    "city": unitedstates1['city'],
    "state": unitedstates1['state'],
    "zip": unitedstates1['zip'],
    "country": unitedstates1['country'],
    "company": "Example Origin",
    "phone": "415-456-7890",
    "email": 'fromaddress@email.com'
}


""" Create parcel """
parcel = {
  "length": 9,
  "width": 6,
  "height": 2,
  "weight": 65,
  # "predefined_package": "Letter"
}


""" create customs info """
customs_info = {
  "contents_explanation": "contents_explanation",
  "contents_type": "merchandise",
  "customs_certify": True,
  "customs_signer": "Fulfillment Center",
  "eel_pfc": "NOEEI 30.37(a)",
  "non_delivery_option": "return",
  "restriction_comments": None,
  "restriction_type": "none",
  "declaration": "does \n work",
  "customs_items": [
    {
      # "description": ''.join(['a' for _ in range(250)]), # description character limit testing
      "description": "very blue shirt", # regular description
      "hs_tariff_number": None,
      "origin_country": "US",
      "quantity": 4,
      "value": "1.0",
      "weight": 16,
      "code": "1234",
      "mode": "production",
      "manufacturer": None,
      "currency": None,
      "eccn": None,
      "printed_commodity_identifier": None
    }
  ]
}


""" create options object """
options = {
  "print_custom_1": "print_custom_1",
  # "print_custom_2": "print_custom_2",
  # "saturday_delivery": True,
  # "special_rates_eligibility": "USPS.MEDIAMAIL",
  # "delivery_confirmation": "SIGNATURE",
  # "import_federal_tax_id": "123412341234",
  # "tax_id_expiration_date": "2022-10-21 10:30:00",
  # "currency": "EUR",
  # "freight_charge": "0.00",
  # "label_format": "PDF",
  # "label_size": "4x6",
  # "date_advance": 1,
  # "hazmat": "LITHIUM",
  # "certified_mail": True,
  # "return_receipt": True,
  # "payment": {
  #   "type": "THIRD_PARTY",
  #   "account": "123456789",
  #   "country": "US",
  #   "postal_code": "85730"
  # },
  # "customs_unit_of_measurement": "BOX"

}


""" Create shipment """
try:
  print("     ")
  print("attempting to create shipment...")
  print("     ")
  print("     ")
  print("     ")

  shipment = client.shipment.create(
    # is_return=True,
    # to_address={
    #   "street1": "5033 N Larkwood Ln",
    #   "street2": "",
    #   "city": "Lehi",
    #   "state": "Utah",
    #   "zip": "84043",
    #   "country": "US",
    #   "company": "Example ToCompany",
    #   "name": "Example ToName"
    #   "phone": "415-456-7890",
    #   "email": 'toaddress@email.com',
    #   "residential": True
    # }, 
    to_address=to_address,
    from_address=from_address,
    parcel=parcel,
    options=options,
    customs_info=customs_info,
    carrier_accounts=[os.getenv('UPS')],
    # service="MediaMail",
    reference=reference_id,
    # with_carbon_offset=True,
  )

  """ Print entire shipment JSON """
  print(shipment)
  print("     ")
  print("     ")
  print("     ")

  """ Print only shipment ID """
  print(shipment['id'])
  print("     ")
  print("     ")
  print("     ")

  """ Print rate_errors if they come back """
  if shipment['messages'] != []:
    error_table = PrettyTable(field_names=['carrier', 'carrier_account_id', 'type', 'message'])
    for error in shipment['messages']:
      error_table.add_row([error['carrier'], error.get('carrier_account_id', ""), error['type'], error['message']])
    print(error_table)
    print("     ")
    print("     ")
    print("     ")
  else:
    pass

  """ Print table in console with rates that came back """
  if shipment['rates'] != []:
    rate_table = PrettyTable(field_names=['Carrier', 'Service', 'Rate'])
    for rate in shipment['rates']:
      rate_table.add_row([rate['carrier'], rate['service'], rate['rate']])
    print(rate_table)
    print("     ")
    print("     ")
    print("     ")




    """ Buy Shipment if rates are returned """
    try:
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
      print("ERROR PURCHASING SHIPMENT:")
      print(f"{json.dumps(json.loads(e.http_body), indent=2)}")
      print("       ")
      print("       ")
      print("       ")
    

    except Exception as e:
      print(e)

  else:
    pass

except easypost.errors.api.api_error.ApiError as e:
  print("ERROR CREATING SHIPMENT:")
  print(e.http_body)
  print("       ")
  print("       ")
  print("       ")

except easypost.errors.api.invalid_request_error.InvalidRequestError as e:
  print("ERROR CREATING SHIPMENT:")
  # print(e)
  print(e.message)
  print(e.errors if e.errors else "no work")









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