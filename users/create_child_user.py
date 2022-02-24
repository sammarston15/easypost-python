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

try:
  user = easypost.User.create(
    name = 'example child account'
  )
  print(user)
except easypost.Error as e:
  print(e.http_body)