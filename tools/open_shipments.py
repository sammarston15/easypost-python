import json
import webbrowser
import time
import os
import re


def main():
    # open_shipment_from_json_batch()
    open_shipment_from_text()


def open_shipment_from_json_batch():
    """
    TOOL DESCRIPTION:

    This tool will take the shipment IDs from the batch and in a loop, open each of them in admin in a
    new tab every 0.1 seconds.


    You used this tool to put together a csv for whiplash. This file had
    the whiplash package ID (their shipment ID - this was in the `reference` field of the shipment),
    the tracking code, and the EP shipment ID.


    ***Adjust the `if` statement to control which items in the list get opened in the browser. 
    """

    # Open the misc.json file
    with open((os.path.join(os.getcwd(),'misc.JSON')), 'r') as f:

        # convert the json into a Python Dictionary
        batch = json.load(f)

        # enumerate through the shipments in the batch to
        # get the public shipment IDs (this will give you a count and the value)
        for count, value in enumerate(batch["batch_shipments"]):

            # control which items in the list to open in the browser
            if count > 0 and count <= 30:
                webbrowser.open_new_tab(f"https://easypost-admin.easypo.net/easy_post~shipment/{value['shipment_public_id']}")
                print(f"Opened item {count}")
                time.sleep(.1)

                """
                Example console output:
                Opened item 301
                Opened item 302
                Opened item 303
                Opened item 304
                Opened item 305
                Opened item 306
                Opened item 307
                Opened item 308
                Opened item 309
                Opened item 310
                """
            else:
                # do nothing here since we only want to open what is in the `if` statement
                pass


def open_shipment_from_text():
    """
    TOOL DESCRIPTION:

    Opens shipments in admin from a piece of text with shipment IDs 
    """


    # Open the misc.json file
    with open((os.path.join(os.getcwd(),'misc.txt')), 'r') as f:
        # read the contents of misc.txt
        data = f.read()
        
        # get a list of all shipment IDs found using regex
        shipments = re.findall("(shp_(?:[a-z0-9]{32}))", data)

        for shipment in shipments:


            # open the shipments in the browser
            webbrowser.open_new_tab(f"https://easypost-admin.easypo.net/easy_post~shipment/{shipment}")
            print(f"Opened {shipment}")


if __name__ == "__main__":
    main()