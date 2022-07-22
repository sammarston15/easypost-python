# import easypost
# import os

# # SET TEST AND PROD API KEY
# test_key = os.getenv('TEST_KEY')
# prod_key = os.getenv('PROD_KEY')


# # USE TEST OR PROD API KEY
# # easypost.api_key = test_key
# easypost.api_key = prod_key



import easypost
easypost.api_key = "EZAK73dc10464465457b9a61c19092fa9108wYNFicH6RtoaVx8hdfqtJg"

webhook = easypost.Webhook.create(url="https://easypost-test.free.beeceptor.com")
print(webhook)
