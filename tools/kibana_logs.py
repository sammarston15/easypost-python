# THIS TOOL IS NOT DONE!!

import os
import json
from datetime import datetime

def main():
    """
    This tool will take the JSON from a Kibana log you paste into the misc.JSON FILE
    AND PUT NEEDFUL LOG INTORMATION INTO A TXT FILE. YOU CAN THEN TAKE THIS TXT
    FILE AND INCLUDE IT IN YOUR PHAB TASK FOR ENGINEERING.

    """


    """ open misc.JSON file """
    with open((os.path.join(os.getcwd(),'misc.JSON')), 'r') as f:
        # have python convert the json into a Python Dictionary
        data = json.load(f)
        # timestamp = data['_source']['timestamp']
        # new_date = datetime.fromtimestamp(timestamp)
        # print(new_date)
        data = data['_source']['msg']

        """ OUTPUT """
        output = f"""
timestamp:	
2023-03-31 12:03:10.052 +00:00

msg.duration_ms: 
{data['duration_ms']}

msg.request.method:
{data['request']['method']}

msg.request.url:
{data['request']['url']}

msg.request.headers.Host:
{data['request']['headers']['Host']}

msg.request.headers.Referer:
{data['request']['headers']['Referer']}

msg.request.headers.User-Agent:
{data['request']['headers']['User-Agent']}

msg.params_full:
{json.dumps(json.loads(data['params_full']), indent=4)}

msg.response.http_status:
{data['response']['http_status']}

msg.response.body:
{json.dumps(json.loads(data['response']['body']), indent=4)}

msg.user.id:
{data['user']['id']}

"""
        print(output)

        # TODO: enter this info into a txt file so you can upload that to the bug phab task
        

if __name__ == "__main__":
    main()