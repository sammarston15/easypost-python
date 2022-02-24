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


""" retrieve address via EasyPost address ID """
address = easypost.Address.retrieve('adr_fc692c2c8f5c11ec99baac1f6bc7b362')


""" retrieve shipment """
shipment = easypost.Shipment.retrieve('shp_574f618892964b339fe03e96f4c2e53d')


""" create pickup """
pickup = easypost.Pickup.create(
  address=address,
  shipment=shipment,
  reference="my-first-pickup",
  min_datetime="2022-02-18 12:00:00",
  max_datetime="2022-02-18 16:00:00",
  is_account_address=False,
  instructions="Special pickup instructions"
)

print(pickup)