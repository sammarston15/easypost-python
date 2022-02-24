""" WORK IN PROGRESS - NOT WORKING YET """

import json

""" paste json here """

old_json = 	{"shipment":{"options":{"incoterm":"DAP","label_format":"zpl","payment":{"type":"THIRD_PARTY","account":"781188832","postal_code":"38120","country":"US"},"print_custom_1":"2815710038253","print_custom_1_code":"PO","peel_and_return":false,"commercial_invoice_letterhead":"IMAGE_2","commercial_invoice_signature":"IMAGE_1"},"from_address":{"company":"HIGH POINT DESIGN","street1":"161 Enterprise Road","street2":"","city":"Johnstown","state":"NY","zip":"12095","phone":"+12123542400"},"to_address":{"company":"Katey Zemen","street1":"615 W Winona Ave","street2":"","city":"Warsaw","state":"IN","zip":"46580","country":"USA","phone":"2123542400","residential":true},"parcel":{"length":12.0,"width":9.0,"height":3.0,"weight":18.4},"carrier_accounts":[{"id":"ca_d13ee600acb4427599f7430ddc1ee9f4","created_at":null,"updated_at":null,"type":null,"description":null,"reference":null,"readable":null,"credentials":null,"test_credentials":null}],"service":"FEDEX_GROUND"},"format":"json","controller":"shipments","action":"create"}


""" make json pretty below """
new_and_improved_json = json.dumps(old_json, indent=4)

print(new_and_improved_json)