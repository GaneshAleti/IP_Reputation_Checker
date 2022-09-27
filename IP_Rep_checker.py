import requests
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--ip", type=str)
parser.add_argument("--api",)
args = parser.parse_args()


ip=args.ip
apikey=args.api
url='https://www.virustotal.com/api/v3/ip_addresses/'+ip
headers={'x-apikey':apikey,}

try:
    response=requests.get(url,headers=headers)
    response_json=json.loads(response.content)
except:
    print("Something wentwrong while making an API call!!!!")
print(response_json)
for item in response_json['data']['attributes']['last_analysis_results']:
    Reason=str(f['data']['attributes']['last_analysis_results'][str(item)]['category'])
    if Reason in list_of_reason:
        print(f"{ip} | {item} | {Reason}\n")
