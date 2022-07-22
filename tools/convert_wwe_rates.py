""" UPS WWE RATE CARD FORMATTER - EXPORT THE EXCEL FILE INTO A CSV THEN USE THIS TOOL """

import csv
from decimal import ROUND_UP, Decimal


COUNTRY_NAME_TO_CODE_MAP = {
    "ARGENTINA": "AR",
    "AUSTRALIA": "AU",
    "AUSTRIA": "AT",
    "BELGIUM": "BE",
    "BRAZIL": "BR",
    "BULGARIA": "BG",
    "CANADA": "CA",
    "CHINA": "CN",
    "CROATIA": "CI",
    "CYPRUS": "CY",
    "CZECH REPUBLIC": "CZ",
    "DENMARK": "DK",
    "ESTONIA": "EE",
    "FINLAND": "FI",
    "FRANCE": "FR",
    "GERMANY": "DE",
    "GIBRALTAR": "GI",
    "GREECE": "GR",
    "HONG KONG": "HK",
    "HUNGARY": "HU",
    "ICELAND": "IS",
    "INDIA": "IN",
    "IRELAND": "IE",
    "ISRAEL": "IL",
    "ITALY": "IT",
    "JAPAN": "JP",
    "KENYA": "KE",
    "LATVIA": "LV",
    "LITHUANIA": "LT",
    "LUXEMBOURG": "LU",
    "MALAYSIA": "MY",
    "MALTA": "MT",
    "MONACO": "MC",
    "MEXICO": "MX",
    "NETHERLANDS": "NL",
    "NEW ZEALAND": "NZ",
    "NIGERIA": "NG",
    "NORWAY": "NO",
    "PAKISTAN": "PK",
    "POLAND": "PL",
    "PORTUGAL": "PT",
    "ROMANIA": "RO",
    "RUSSIA": "RU",
    "SAUDI ARABIA": "SA",
    "SINGAPORE": "SG",
    "SLOVAKIA": "SK",
    "SLOVENIA": "SI",
    "SOUTH AFRICA": "ZA",
    "SOUTH KOREA": "KR",
    "SPAIN**": "ES",
    "SWEDEN": "SE",
    "SWITZERLAND": "CH",
    "TAIWAN": "TW",
    "THAILAND": "TH",
    "TURKEY": "TR",
    "UNITED ARAB EMIRATES": "AE",
    "UNITED KINGDOM": "UK",
    "UNITED STATES": "US",
}

def main():
    desc = """UPSWWE rate formatter"""

    file_name = "/Users/smarston/Downloads/Brilliant Made WW Economy DDP - 04.22 Easypost IT Team Version Monaco added.csv"
    raw_data = load_raw_data_from_csv(file_name)

    empty_list = []

    raw_data.pop(0)

    for index, row in enumerate(raw_data):

        x = row[0].strip()
        dest_country = COUNTRY_NAME_TO_CODE_MAP[x]

        thing = {
            "origin_country": "US",
            "dest_country": dest_country,
            "zone": row[1],
            "1lb": convert_to_cents(row[2]),
            "2lb": convert_to_cents(row[3]),
            "3lb": convert_to_cents(row[4]),
            "4lb": convert_to_cents(row[5]),
            "5lb": convert_to_cents(row[6]),
            "6lb": convert_to_cents(row[7]),
            "7lb": convert_to_cents(row[8]),
            "8lb": convert_to_cents(row[9]),
            "9lb": convert_to_cents(row[10]),
            "10lb": convert_to_cents(row[11])
        }
        empty_list.append(thing)
        thing = {}

    print(empty_list[0:5])


    whole_card = ["origin_country,dest_country,weight_oz,zone,service,rate_cents\n"]

    for index, row in enumerate(empty_list):
        one_row = row["origin_country"] + "," + row["dest_country"] + "," + "16" + "," + row["zone"] + "," + "WorldwideEconomyDDP" + "," + str(row["1lb"]) + "\n"
        two_row = row["origin_country"] + "," + row["dest_country"] + "," + "32" + "," + row["zone"] + "," + "WorldwideEconomyDDP" + "," + str(row["2lb"]) + "\n"
        three_row = row["origin_country"] + "," + row["dest_country"] + "," + "48" + "," + row["zone"] + "," + "WorldwideEconomyDDP" + "," + str(row["3lb"]) + "\n"
        four_row = row["origin_country"] + "," + row["dest_country"] + "," + "64" + "," + row["zone"] + "," + "WorldwideEconomyDDP" + "," + str(row["4lb"]) + "\n"
        five_row = row["origin_country"] + "," + row["dest_country"] + "," + "80" + "," + row["zone"] + "," + "WorldwideEconomyDDP" + "," + str(row["5lb"]) + "\n"
        six_row = row["origin_country"] + "," + row["dest_country"] + "," + "96" + "," + row["zone"] + "," + "WorldwideEconomyDDP" + "," + str(row["6lb"]) + "\n"
        seven_row = row["origin_country"] + "," + row["dest_country"] + "," + "112" + "," + row["zone"] + "," + "WorldwideEconomyDDP" + "," + str(row["7lb"]) + "\n"
        eight_row = row["origin_country"] + "," + row["dest_country"] + "," + "128" + "," + row["zone"] + "," + "WorldwideEconomyDDP" + "," + str(row["8lb"]) + "\n"
        nine_row = row["origin_country"] + "," + row["dest_country"] + "," + "144" + "," + row["zone"] + "," + "WorldwideEconomyDDP" + "," + str(row["9lb"]) + "\n"
        ten_row = row["origin_country"] + "," + row["dest_country"] + "," + "160" + "," + row["zone"] + "," + "WorldwideEconomyDDP" + "," + str(row["10lb"]) + "\n"

        whole_card.append(one_row)
        whole_card.append(two_row)
        whole_card.append(three_row)
        whole_card.append(four_row)
        whole_card.append(five_row)
        whole_card.append(six_row)
        whole_card.append(seven_row)
        whole_card.append(eight_row)
        whole_card.append(nine_row)
        whole_card.append(ten_row)



    print(whole_card[0:20])
    print(len(whole_card))

    # Write reformatted data to file and name the file
    write_to_file(whole_card, "/Users/smarston/Downloads/2501159_rates_20220419_DDP.csv")

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