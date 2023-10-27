import json
import os



def main():
  """ THIS TOOL TAKES IN ORDER JSON AND PRINTS OUT 
      THE NUMBER OF SHIPMENTS, NUMBER OF CUSTOMS ITEMS AND TOTAL WEIGHT FOR THE ORDER.

      expected output example:
      shp_6f6aa88ae62f41a0a62ff65f7b2003ba - 10 customs_items
      shp_5e840299b1a44acd9821814301ad1581 - 10 customs_items
      shp_a30dfe33839d477482b54487bf55725b - 10 customs_items
      shp_508b574184a54738bce938325cd0c1f0 - 10 customs_items
          
      total weight: 1058.4
      # of shipments: 4
      # of customs items: 79
  """

  with open((os.path.join(os.getcwd(),'misc.JSON')), 'r') as f:
    # have python convert the json into a Python Dictionary
    order = json.load(f)

    total_weight = 0
    total_shipments = 0
    customs_items = 0

    if order['customs_info'] and order['customs_info']['customs_items']:
      customs_items += len(order['customs_info']['customs_items'])
    for shipment in order['shipments']:
      if shipment['customs_info'] != None and len(shipment['customs_items']) > 0:
        customs_items += len(shipment['customs_info']['customs_items'])
      print('weight: ', shipment['parcel']['weight'])
      total_weight += shipment['parcel']['weight']
      total_shipments += 1

      # print each shipment's details
      # print(shipment['id'], f"- {len(shipment['customs_info']['customs_items'] if shipment['customs_info'] != None else [])} customs_items")
    
    # final output
    print("     ")
    print(f"total weight: {total_weight}")
    print(f"# of shipments: {total_shipments}")
    print(f"# of customs items: {customs_items}")


if __name__ == "__main__":
  main()