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


""" retrieve pickup via EasyPost pickup ID """
pickup = easypost.Pickup.retrieve("pickup_5d30888ca4dd4481a0df47ed662f1e6a")

""" buy pickup """
pickup.buy(carrier="DHLExpress", service="ExpressPickup")

print(pickup)