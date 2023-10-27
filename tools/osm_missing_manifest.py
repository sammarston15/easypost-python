import os
import json


def main():
    """
    This tool will take a list of shipment objects and put together a 
    response to send to OSM for their "missing data file" support tickets.
    """

    with open((os.path.join(os.getcwd(),'misc.JSON')), 'r') as f:
        # have python convert the json into a Python Dictionary
        data = json.load(f)


        for ship in data:
            output = f"{ship.get('tracking_code', '')}{' - ' if ship['id'] else ''}{ship.get('id', '')} - https://easypost-admin.easypo.net/easy_post~shipment/{ship['id']} {f'- no batch' if not ship['batch_id'] else ''}{f', no scanform' if not ship['scan_form'] else ''}"
            print(output)
 


if __name__ == '__main__':
    main()






"""
Example Output:
9274890240785602154472-shp_4eb224ba2b6547c2b7186fa436ca09b2 - https://easypost-admin.easypo.net/easy_post~shipment/shp_4eb224ba2b6547c2b7186fa436ca09b2 - no batch, no scanform
9274890240785602154458-shp_f88c57af9c5f427eb620e1189dfb7540 - https://easypost-admin.easypo.net/easy_post~shipment/shp_f88c57af9c5f427eb620e1189dfb7540 - no batch, no scanform
9274890240785602154434-shp_250e6b72ca2e48009fbe59b8a8448d77 - https://easypost-admin.easypo.net/easy_post~shipment/shp_250e6b72ca2e48009fbe59b8a8448d77 - no batch, no scanform
9261290240785600801211-shp_fd41218494ed415ca4ba0413974bd041 - https://easypost-admin.easypo.net/easy_post~shipment/shp_fd41218494ed415ca4ba0413974bd041 - no batch, no scanform
9274890240785602154465-shp_842e8cf852ce4524813ca2816dffa2c3 - https://easypost-admin.easypo.net/easy_post~shipment/shp_842e8cf852ce4524813ca2816dffa2c3 - no batch, no scanform
9274890240785602154557-shp_9036b0e8a7fd4a6e88a9f898d97680b5 - https://easypost-admin.easypo.net/easy_post~shipment/shp_9036b0e8a7fd4a6e88a9f898d97680b5 - no batch, no scanform
9274890240785602154144-shp_1e46cf876b1e43ffb33ec9c3842d6cd5 - https://easypost-admin.easypo.net/easy_post~shipment/shp_1e46cf876b1e43ffb33ec9c3842d6cd5 - no batch, no scanform
9274890240785602154502-shp_b659e942ad464c60bc4d6fa596ef5964 - https://easypost-admin.easypo.net/easy_post~shipment/shp_b659e942ad464c60bc4d6fa596ef5964 - no batch, no scanform
9261290240785600800993-shp_846a71fee0ce4b3fbb433207b6cb8ba7 - https://easypost-admin.easypo.net/easy_post~shipment/shp_846a71fee0ce4b3fbb433207b6cb8ba7 - no batch, no scanform
9261290240785600801068-shp_b8d1cdf2e03f4be2bb72c41d970aa922 - https://easypost-admin.easypo.net/easy_post~shipment/shp_b8d1cdf2e03f4be2bb72c41d970aa922 - no batch, no scanform

**This would be used for an internal note to find out if the tracking codes in question have been manifested in our sytem. If not, they would need to scanform them since OSM requires this.

"""