import easypost
import os

# SET TEST AND PROD API KEY
test_key = os.getenv('TEST_KEY')
prod_key = os.getenv('PROD_KEY')


# USE TEST OR PROD API KEY
# easypost.api_key = test_key
easypost.api_key = prod_key

try:
    user = easypost.User.retrieve("user_73dc10464465457b9a61c19092fa9108")
    user.delete()
except easypost.Error as e:
    print(e.http_body)