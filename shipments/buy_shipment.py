import easypost
import os


# SET TEST AND PROD API KEY
test_key = os.getenv('test_key')
prod_key = os.getenv('prod_key')


# USE TEST OR PROD API KEY
easypost.api_key = test_key
# easypost.api_key = prod_key

######################################

""" Retrieve the shipment """
shipment = easypost.Shipment.retrieve("shp_b1888c690ef34f3fa31c0e6096b95dd4")


""" buy lowest rate | this example is from https://www.easypost.com/docs/api#buy-a-shipment """
# shipment.buy(rate=shipment.lowest_rate())
# print(shipment)


""" buy service and carrier | this example is from https://www.easypost.com/getting-started/python#buy-shipment-python-curl-ruby-python-php-java-c-sharp-node-js """
# shipment.buy(rate=shipment.lowest_rate(carriers=['USPS'], services=['First']))
# print(shipment)


""" buy a specific rate via rate ID | this example also comes from https://www.easypost.com/getting-started/python#buy-shipment-python-curl-ruby-python-php-java-c-sharp-node-js """
shipment.buy(rate={'id': 'rate_62d2135118f3445aba911d1ff0d8e1ba'})
print(shipment)

