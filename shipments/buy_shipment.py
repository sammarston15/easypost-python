import easypost
import os
from dotenv import load_dotenv

# LOAD ENVIRONMENT VARIABLES
load_dotenv()

# SET TEST AND PROD API KEY
test_key = os.getenv('test_key')
prod_key = os.getenv('prod_key')


# USE TEST OR PROD API KEY
easypost.api_key = test_key
# easypost.api_key = prod_key

######################################

""" Retrieve the shipment """
shipment = easypost.Shipment.retrieve("shp_140b741cee2649dea85bf3d6a213ae7b")


""" buy lowest rate | this example is from https://www.easypost.com/docs/api#buy-a-shipment """
# shipment.buy(rate=shipment.lowest_rate())
# print(shipment)


""" buy service and carrier | this example is from https://www.easypost.com/getting-started/python#buy-shipment-python-curl-ruby-python-php-java-c-sharp-node-js """
# shipment.buy(rate=shipment.lowest_rate(carriers=['USPS'], services=['First']))
# print(shipment)


""" buy a specific rate via rate ID | this example also comes from https://www.easypost.com/getting-started/python#buy-shipment-python-curl-ruby-python-php-java-c-sharp-node-js """
shipment.buy(rate={'id': 'rate_a1d3d9c1ce4643b69356abbbf90026cc'})
print(shipment)

