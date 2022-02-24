import easypost
import os
from dotenv import load_dotenv

# LOAD ENVIRONMENT VARIABLES
load_dotenv()

# SET TEST AND PROD API KEY
test_key = os.getenv('test_key')
prod_key = os.getenv('prod_key')


# USE TEST OR PROD API KEY
# easypost.api_key = test_key
easypost.api_key = prod_key

ca = easypost.CarrierAccount.create(
    type="UspsAccount",
    description="not real usps account",
    reference="",
    credentials={
        "company_name": "python client",
        "address_street": "525 S 850 E",
        "address_city": "Lehi",
        "address_state": "UT",
        "address_zip": "84043",
        "phone": "3858675309"
    }
)