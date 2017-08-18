"""


"""
import sys
import requests
from citytrader.auth import get_access_token

def main():
    client_id = sys.argv[1]
    url = sys.argv[2]
    access_token = get_access_token(client_id, env="devapi")
    api_call_headers = {'Authorization': 'Bearer ' + access_token}
    api_call_response = requests.get(url, headers=api_call_headers, verify=False)
    print api_call_response.text

if __name__ == "__main__":
    main()
