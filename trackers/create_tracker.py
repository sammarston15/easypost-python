""" 
Carrier string representations for Trackers can be found at https://www.easypost.com/docs/api#carrier-tracking-strings

test_tracking_info.JSON updated as of 8/13/2021

"""

import easypost
import os
import json


""" LOAD TEST AND PROD API KEY """
test_key = os.getenv('test_key')
prod_key = os.getenv('prod_key')


""" SET TEST OR PROD API KEY """
# easypost.api_key = test_key
easypost.api_key = prod_key

""" open the tracking info file - NOTE: os.getcwd() will give you a string of the path to the workspace folder, not the folder that the file is in necessarily. See below how I added the trackers folder path in the file name. """
with open(os.path.join(os.getcwd(), 'trackers/test_tracking_info.JSON'), 'r') as f:
  tracking_info = json.load(f)

  tracker = easypost.Tracker.create(
    carrier=tracking_info['carriers'][2]['carrier_str'],
    tracking_code="AXL9530636",
    # carrier="FedEx"
  )

  print(tracker)

