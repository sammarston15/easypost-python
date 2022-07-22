""" TOOL NOT WORKING RIGHT NOW """

import csv
from decimal import ROUND_UP, Decimal

from constants import COUNTRY_NAME_TO_CODE_MAP


def main():

    # the path and name of the file to format
    filename = "in/sam.csv"

    # reads the csv
    raw_data = load_raw_data_from_csv(filename)

    # puts the rates with the country
    empty_list = []
    actual_rates = raw_data[2:]
    
    for index, row in enumerate(raw_data[0]):

        dest_country = raw_data[0][index][:2]
        zone = raw_data[1][index]
        rates = []
        for row1 in actual_rates:
            rates.append(row1[index])

        thing = {
            "origin_country": "US",
            "dest_country": dest_country,
            "zone": zone,
            "rates": rates
        }
        empty_list.append(thing)
        thing = {}


    # puts whole rate card together
    whole_card = ["origin_country,dest_country,weight_oz,zone,service,rate_cents\n"]

    for index, row in enumerate(empty_list):

        for index1, row1 in enumerate(row["rates"]):

            # pounds to ounces
            pounds = index1 + 1
            ounces = (Decimal(pounds) * 16).quantize(Decimal('1.'), rounding=ROUND_UP)

            # cents to dollars
            dollars = convert_to_cents(row1)

            # the total row
            newline = row["origin_country"] + "," + row["dest_country"] + "," + str(ounces) + "," + row["zone"] + "," + "WorldwideEconomyDDP" + "," + str(dollars) + "\n"
            whole_card.append(newline)

            

    # sanity check
    print(whole_card[0])

    # checks that all rates are there
    print("length", len(whole_card))


    # writes to output file
    write_to_file(whole_card, "output.csv")

    print("done")


def write_to_file(file_content, file_name):
    hash_file = open(file_name, 'w')
    hash_file.writelines(file_content)
    hash_file.close()


    

def convert_to_cents(stringhere):
    intnow = float(stringhere)
    cents = (Decimal(stringhere) * 100).quantize(Decimal('1.'), rounding=ROUND_UP)

    return cents



def load_raw_data_from_csv(file_path):
    with open(file_path, newline='') as csv_file:
        reader = csv.reader(csv_file)
        raw_data = [row for row in reader]

    return raw_data




if __name__ == '__main__':
    main()
