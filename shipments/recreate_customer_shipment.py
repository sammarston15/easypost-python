import easypost # easypost python client library
import os # allows for access of environment variables in .env file
import json # allows for reading of JSON from misc.JSON file
from prettytable import PrettyTable # allows for formatted table printing in the console
from uuid import uuid4 # use this to generate a random and unique identifier
# import dad_tool # Justin Hammond's Dummy Address Data


""" LOAD TEST AND PROD API KEY """
test_key = os.getenv('TEST_KEY')
prod_key = os.getenv('PROD_KEY')
personal_test_key = os.getenv('PERSONAL_TEST_KEY')


""" SET API KEY """
# client = easypost.EasyPostClient(personal_test_key)
client = easypost.EasyPostClient(test_key)
# client = easypost.EasyPostClient(prod_key)



""" open misc.JSON file """
with open((os.path.join(os.getcwd(),'misc.JSON')), 'r') as f:
  # have python convert the json into a Python Dictionary
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
  # if ship['selected_rate']:
  #   del ship['selected_rate']
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
    
  # converts python dictionary into json
  # print(json.dumps(ship['to_address'], ))

  """ any additional adjustments """
  # ship['options']['dropoff_max_datetime'] = "2022-03-27 10:30:00"
  # ship['options']['label_size'] = "4x6"
  # ship['options']['label_format'] = "PDF"
  # ship['options']['label_resolution'] = "203"
  # ship['options']['label_date'] = "2022-02-28"
  # ship['options']['incoterm'] = "DDP"
  # ship['options']['currency'] = "CAD"
  # ship['options']['billing_account_number'] = "123456789"
  # ship['options']['payment'] = {
  #   "type": "THIRD_PARTY",
  #   "account": "123456789",
  #   "country": "US",
  #   "postal_code": "84043"
  # }
  # ship['options']['duty_payment_account'] = "123456789"
  # ship['options']['duty_payment'] = {
  #   "type": "RECEIVER",
  #   "account": "123456789",
  #   "country": "US",
  #   "postal_code": "84043"
  # }
  # ship['options']['print_custom_1'] = "print_custom_1"
  # ship['options']['print_custom_1_code'] = "TN"
  # ship['options']['print_custom_2'] = "print_custom_2"
  # ship['options']['saturday_delivery'] = True
  # ship['options']['machinable'] = True
  # ship['options']['commercial_invoice_format'] = "PNG"
  # ship['options']['import_federal_tax_id'] = "123412341234"
  # ship['options']['tax_id_expiration_date'] = "2022-12-21 10:30:00"
  # ship['to_address']['name'] = None
  # ship['buyer_address']['company'] = "Example Buyer Address"
  # ship['buyer_address']['name'] = "Example Buyer Address"
  # ship['buyer_address']['federal_tax_id'] = "123456789"
  # address1 = dad_tool.random_address('US_UT')
  # ship['parcel']['predefined_package'] = None
  # ship['to_address']['street1'] = ship['to_address']['company']
  # ship['customs_info']['contents_type'] = "documents"
  # ship['options']['print_custom'] = [
  #   {
  #     "name": "print_custom_1",
  #     "value": "Printed Label Field 1",
  #     "barcode": "false"
  #   },
  #   {
  #     "name": "print_custom_2",
  #     "value": "Printed Label Field 2",
  #     "barcode": "false"
  #   },
  # ]
  


  """ create unique reference ID """
  reference_id = str(uuid4())[:12]

  
  try:
    print("     ")
    print("attempting to create shipment...")
    print("     ")
    print("     ")
    print("     ")

    """ Create/Rate Shipment """
    shipment = client.shipment.create(
      is_return=ship.get('is_return', False),
      to_address=ship['to_address'],
      from_address=ship['from_address'],
      # return_address=ship['return_address'],
      # buyer_address=ship['buyer_address'],
      parcel=ship['parcel'],
      customs_info=ship.get('customs_info', None),
      options=ship['options'],
      carrier_accounts=[os.getenv("USPS")],
      reference=reference_id,
      tax_identifiers=ship.get('tax_identifiers', None)
    )

    """ Print entire shipment JSON """
    print(shipment)
    print("     ")
    print("     ")


    """ Print only shipment ID """
    print(shipment['id'])
    print("     ")
    print("     ")


    """ Print rate_errors if they come back """
    if shipment['messages'] != []:
      # error_table = PrettyTable(field_names=['carrier', 'carrier_account_id', 'type', 'message'])
      # for error in shipment['messages']:
      #   error_table.add_row([error['carrier'], error.get('carrier_account_id', ''), error['type'], error['message']])
      # print(error_table)
      # print("     ")
      # print("     ")
      # print("     ")

      print("=====RATING ERRORS===== ")
      display = []
      for error in shipment['messages']:
        display_error = {
          "carrier": error.get('carrier', ''),
          "carrier_account_id": error.get('carrier_account_id', ''),
          "type": error.get('type', ''),
          "message": error.get('message', ''),
        }
        display.append(display_error)
      print(json.dumps(display, indent=4))
      print("   ")

    else:
      pass


    """ Print table in console with rates that came back """
    if shipment['rates'] != []:
      print("=====AVAILABLE RATES===== ")
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

        # print shipment if buy is successful
        print(bought_shipment)
        print("     ")
        print("==============================")
        print("     ")
        print("shipment: ", bought_shipment['id'])
        print("     ")
        print("label:", bought_shipment['postage_label'].get('label_url', 'no label URL...') if bought_shipment['postage_label'] else 'no postage label object...')
        print("     ")
        print("     ")


      # except easypost.errors.general.easypost_error.EasyPostError as e:
      #   print("ERROR PURCHASING SHIPMENT:")
      #   print(e.message)
      #   print("       ")
      #   print("       ")
      

      # catch raw API errors
      except easypost.errors.api.api_error.ApiError as e:
        print(e.http_body)

      # catch general exceptions
      except Exception as e:
        print(e)

    else:
      print('no rates came back...')
      print(shipment['rates'])
    
  # catch raw API error response  
  except easypost.errors.api.api_error.ApiError as e:
    print("ERROR FETCHING RATES:")
    print(e.http_body)
    print("       ")






    


