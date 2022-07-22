""" JSON PRETTY PRINTER TOOL """

import json

# paste your json in the below string
my_code = 	"""
{"carrier":"FedExCrossBorder","carrier_account_id":"ca_d7cacd1a7b67407dbe0e07330cd15c6e","type":"rate_error","message":"shipment.from_address: Only shipments originating from the US are supported. and shipment.customs_info.customs_items.0.value: ensure this value is greater than or equal to 0.01"}
"""

# convert json to python dictionary
loaded_json = json.loads(my_code)

# beautify the json
new_and_improved_json = json.dumps(loaded_json, indent=4)

# print the pretty formatted json
print(new_and_improved_json)