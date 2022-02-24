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

# customs_item = easypost.CustomsItem.create(
#   description='T-shirt',
#   quantity=1,
#   value=10,
#   weight=5,
#   hs_tariff_number='123456',
#   origin_country='us'
# )
# print(customs_item)

customs_info = easypost.CustomsInfo.create(
  eel_pfc='NOEEI 30.37(a)',
  customs_certify=True,
  customs_signer='Steve Brule',
  contents_type='merchandise',
  contents_explanation='',
  restriction_type='none',
  restriction_comments='',
  non_delivery_option='abandon',
  customs_items=['cstitem_daa0ccbca7b242cd8694aee0ce4939d2']
)
print(customs_info)