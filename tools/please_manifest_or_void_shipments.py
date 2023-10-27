"""
This tool is 98% inspired by Noah Wenzel's tool.

This tool extracts the first ID (shipment ID or canada post shipment ID)
and createds a comma-separated list of those IDs.
"""

# paste the text you copied from the "Please manifest or void these {carrier - typically speedee or canada post} shipments" email
copied_email = """
 146261668796136336 	 9339466367757360 	 2022-11-18T18:28:57 
 890641668796633321 	 9339466368462362 	 2022-11-18T18:37:14 
 321901668796762688 	 9339466368524367 	 2022-11-18T18:39:23 
 890641668796771911 	 9339466368528365 	 2022-11-18T18:39:33 
 411491668797125248 	 9339466368726365 	 2022-11-18T18:45:26 
 411491668797161023 	 9339466368733363 	 2022-11-18T18:46:01 
 411491668797445129 	 9339466369099369 	 2022-11-18T18:50:46 
 589531668798438340 	 9339466370131362 	 2022-11-18T19:07:19 
 146261668798609991 	 9339466369998365 	 2022-11-18T19:10:10 
 321901668798740372 	 9339466370450364 	 2022-11-18T19:12:21 
 146261668799103156 	 9339466370384362 	 2022-11-18T19:18:24 
 890641668800275241 	 9339466371868366 	 2022-11-18T19:37:56 
 589531668800413247 	 9339466371720367 	 2022-11-18T19:40:14 
 411491668800702723 	 9339466372113366 	 2022-11-18T19:45:03 
 146261668800785273 	 9339466372226363 	 2022-11-18T19:46:26 
 589531668801839705 	 9339466373093360 	 2022-11-18T20:04:00 
 411491668802807722 	 9339466373653366 	 2022-11-18T20:20:08 
 411491668804271765 	 9339466374808369 	 2022-11-18T20:44:32 
 411491668805071955 	 9339466374969367 	 2022-11-18T20:57:52 
 411491668805151885 	 9339466375255360 	 2022-11-18T20:59:12 
 589531668805201993 	 9339466375274361 	 2022-11-18T21:00:03 
"""



email = copied_email.split()
print(email)

CPIDs = ''

for i in range (len(email)):

    # get canada post shipment ID
    if i % 3 == 0:
        CPIDs=CPIDs+email[i]+", "

final = CPIDs[:-2] # Remove the extra ', ' that was added in the above loop to the last ID
print(final)

with open('shipment_ids.csv', 'w') as f:
    f.write(final)