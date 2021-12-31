
import requests
import json
import urllib3
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'Host': 'api.getsendit.com',
    'Content-Length': '354',
    'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="92"',
    'App-Id': 'c2ad997f-1bf2-4f2c-b5fd-83926e8f3c65',
    'App-Version': '1.0',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Origin': 'https://web.getsendit.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://web.getsendit.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}


def main(json_payload,instance_number):
    rqs = 0

    while True:
        try:
            response = requests.post('https://api.getsendit.com/v1/posts',
            headers=headers, data=json_payload, verify=False,timeout=0.9)
            if (response.json()['status'] == 'success'):
                rqs = rqs + 1
                print(f'\033[92m'+f'[*] REQUEST SUCCESS | instance: {instance_number}')
            else:
                print(f"\033[91m[*]NETWORK ERROR| instance: {instance_number}")
        except:
            print(f"\033[91m[*]UNKNOWN ERROR | instance: {instance_number}")
