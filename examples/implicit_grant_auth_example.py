"""


"""
import sys
import requests
from citytrader.auth import get_access_token

def main():
    client_id = sys.argv[1]
    access_token = get_access_token(client_id)
    api_call_headers = {'Authorization': 'Bearer ' + access_token}
    api_call_response = requests.get("https://devapi.optionscity.com/productgroups/2",
                                     headers=api_call_headers, verify=False)
    print api_call_response.text

if __name__ == "__main__":
    main()
