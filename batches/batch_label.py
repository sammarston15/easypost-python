import easypost
import os
import json
# import dad_tool


""" LOAD TEST AND PROD API KEY """
test_key = os.getenv('TEST_KEY')
prod_key = os.getenv('PROD_KEY')


""" SET TEST OR PROD API KEY """
# easypost.api_key = test_key
easypost.api_key = prod_key 



batch = easypost.Batch.retrieve('batch_501824e5535f4b0d89e4458ee5372aca')
# batch.label(file_format = 'pdf')
print(batch)
