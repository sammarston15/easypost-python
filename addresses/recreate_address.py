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


with open((os.path.join(os.getcwd(),'misc.JSON')), 'r') as f:
    # have python convert the json into a Python Dictionary
    adr = json.load(f)

    # create address with verification
    address = client.address.create(
        # verify=["delivery"],
        name=adr.get('name', None),
        company=adr.get('company', None),
        street1=adr.get('street1', None),
        street2=adr.get('street2', None),
        city=adr.get('city', None),
        state=adr.get('state', None),
        zip=adr.get('zip', None),
        country=adr.get('country', None),
        phone=adr.get('phone', '800-867-5309'),
        carrier_facility=adr.get('carrier_facility', None),
        residential=adr.get('residential', None),
        federal_tax_id=adr.get('federal_tax_id', None),
        state_tax_id=adr.get('state_tax_id', None),
    )
    print(address)