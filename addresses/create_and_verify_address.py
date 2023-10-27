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


""" Create DAD addresses """
unitedstates1 = dad_tool.random_address('US_UT')
unitedstates2 = dad_tool.random_address('US_AZ')
unitedkingdom1 = dad_tool.random_address('EU_UK')
unitedkingdom2 = dad_tool.random_address('EU_UK')
canada1 = dad_tool.random_address('CA_BC')
canada2 = dad_tool.random_address('CA_BC')


""" create address with verification """
try:
    address = client.address.create(
        verify=["pickup"],
        street1="13 Adeola Odeku Street",
        street2="",
        city="Lagos",
        state="Lagos State",
        zip="101241",
        country="Nigeria",
        company="John Enterprice",
        name="John Doe",
        phone="5555555555",
        email="test@mail.com",
        residential=False
    )
    print(address)

except easypost.errors.api.api_error.ApiError as e:
    print("   ")
    print(e.http_body)
    print("   ")


""" use dad tool to make new address"""
# try:
#     address = client.address.create(
#         street1=unitedstates2['street1'],
#         street2=unitedstates2['street2'],
#         city=unitedstates2['city'],
#         state=unitedstates2['state'],
#         zip=unitedstates2['zip'],
#         country=unitedstates2['country'],
#         company="EasyPost",
#         phone="415-456-7890",
#         verify=["delivery"],
#     )
#     print(address)

# except easypost.errors.api.api_error.ApiError as e:
#     print("   ")
#     print(e.http_body)
#     print("   ")


