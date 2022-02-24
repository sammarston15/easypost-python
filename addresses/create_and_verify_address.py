import easypost
import os
import json
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


address1 = dad_tool.random_address('US_UT')

# create address with verification
# address = easypost.Address.create(
#     verify=["delivery"],
#     street1="Unit Pr6 Ik Business Park",
#     street2="Philips Road",
#     city="Blackburn",
#     state="",
#     zip="BB1 5FD",
#     country="GB",
#     company="EasyPost",
#     phone="415-456-7890"
# )
# print(address)

""" use dad tool to make new address"""
address = easypost.Address.create(
    verify=["delivery"],
    street1=address1['street1'],
    street2=address1['street2'],
    city=address1['city'],
    state=address1['state'],
    zip=address1['zip'],
    country=address1['country'],
    company="EasyPost",
    phone="415-456-7890"
)
print(address)

