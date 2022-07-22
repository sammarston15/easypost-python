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

""" RETRIEVE SHIPMENT """
shipment = easypost.Shipment.retrieve('shp_cfe44557d8674708992fcee08e1b02eb')

""" PRINT SHIPMENT """
print(shipment)