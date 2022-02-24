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


""" Create to_address """
try:
    to_address = easypost.Address.create(
        street1="417 Montgomery Street",
        street2="FLOOR 5",
        city="San Francisco",
        state="CA",
        zip="94104",
        country="US",
        company="EasyPost",
        phone="415-456-7890"
    )
except easypost.Error as e:
    print(e.http_body)


""" Create from_address """
try:
    from_address = easypost.Address.create(
        name = "Dr. Steve Brule",
        street1 = "179 N Harbor Dr",
        street2 = "Redondo Beach",
        city = "San Francisco",
        state = "CA",
        zip = "90277",
        country = "US",
        phone = "310-808-5243"
    )
except easypost.Error as e:
    print(e.http_body)


""" Create order """
try: 
    order = easypost.Order.create(
        to_address=to_address,
        from_address=from_address,
        shipments=[
            {
                "parcel": {
                    "weight": 10.2
                },
                "options": {"label_format":"PDF"}
            },
            {
                "parcel": {
                    "weight": 17.5
                },
                "options": {"label_format":"PDF"}
            }
        ]
    )
except easypost.Error as e:
    print(e.http_body)


""" Buy order """
try:
    order.buy(carrier="FedEx", service="FEDEX_2_DAY")
    print(order)
except easypost.Error as e:
    print(e.http_body)