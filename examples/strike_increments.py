"""
select out products of type "Option" and figure out strike increments
"""

import sys
from decimal import Decimal
from citytrader.request_client import RequestClient

#   gather user auth input and init RequestClient()
def main():
    client_id = raw_input('Enter your client_id: ')
    client_secret = raw_input('Enter your client_secret: ')
    username = raw_input('Enter your username: ')
    password = raw_input('Enter your password: ')
    rc = RequestClient(server="https://devservices.optionshop.com", client_id=client_id, client_secret=client_secret, username=username, password=password)
    option_products = rc.request(request_type="GET", url="products?instrument_type=Option")["data"]

    sorted_option_products = sorted(option_products, key=lambda k: k['id'])

    json_to_print = {}

    #   get all products that are options
    for option in sorted_option_products:

        # get a small list of options
        instruments = rc.request(request_type="GET", url="instruments?product_group_id=%s&instrument_type=Option&per_page=100" % option["group_id"])

        if instruments['data']:

            # build list of strikes and sort
            strikes = [i["strike"] for i in instruments["data"]]
            strikes.sort()

            # get diff between each list item and filter out 0s
            list_diffs = filter(lambda a: a !=0, [strikes[i+1]-strikes[i] for i in range(len(strikes)-1)])

            # get most common occurrence
            strike_increment = max(set(list_diffs), key=list_diffs.count)

            json_to_print[option["id"]] = strike_increment

            # print results on each pass
            print "id: %s, parent_symbol: %s, strike_increment: %s" % (option["id"], option["parent_symbol"], strike_increment)

    # print json version
    print json_to_print

if __name__ == "__main__":
    main()
