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

""" retrieve the shipment"""
shipment = easypost.Shipment.retrieve("shp_...")

""" convert the label format """
shipment.label(file_format="ZPL")