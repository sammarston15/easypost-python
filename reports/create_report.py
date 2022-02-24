import easypost
import os
from dotenv import load_dotenv
import json

""" LOAD ENVIRONMENT VARIABLES """
load_dotenv()


""" LOAD TEST AND PROD API KEY """
test_key = os.getenv('test_key')
prod_key = os.getenv('prod_key')


""" SET TEST OR PROD API KEY """
easypost.api_key = test_key
# easypost.api_key = prod_key 


""" Create Payment log report """
# payment_log_report = easypost.Report.create(
#   start_date="2016-10-01",
#   end_date="2016-10-31",
#   type="payment_log"
# )
# print(payment_log_report)

""" create refund report """
# refund_report = easypost.Report.create(
#   start_date="2016-10-01",
#   end_date="2016-10-31",
#   type="refund"
# )
# print(refund_report)

""" create shipment report """
shipment_report = easypost.Report.create(
  start_date="2021-10-01",
  end_date="2021-10-05",
  type="shipment",
  send_email=True
)
print(shipment_report)

""" create shipment invoice report """
# shipment_invoice_report = easypost.Report.create(
#   start_date="2016-10-01",
#   end_date="2016-10-31",
#   type="shipment_invoice"
# )
# print(shipment_invoice_report)

"""create tracker report """
# tracker_report = easypost.Report.create(
#   start_date="2016-10-01",
#   end_date="2016-10-31",
#   type="tracker"
# )
# print(tracker_report)
