"""
Prints City product list in csv format.

Usage:

python examples/products_dump.py client_id client_secret username password > out.csv

"""

import sys
from citytrader.request_client import RequestClient

def main():
    client_id = sys.argv[1]
    client_secret = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]

    rc = RequestClient(server="https://api.optionscity.com", client_id=client_id, client_secret=client_secret, username=username, password=password)

    product_groups = rc.request(request_type="GET", url="productgroups")

    pg_lookup = {}
    for i in product_groups["data"]:
        pg_lookup[i['id']] = i['exchange']

    print "id,group_id,parent_symbol,clearing_symbol,instrument_type,is_weekly,settlement_type,exercise_procedure,expiration_type,display_factor,tick_size,tick_value,base_factor,exchange"
    for product in rc.request(request_type="GET", url="products")['data']:
        print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (product['id'], product['group_id'], product['parent_symbol'], product['clearing_symbol'], product['instrument_type'], product['is_weekly'], product['settlement_type'], product['exercise_procedure'], product['expiration_type'], product['display_factor'], product['tick_size'], product['tick_value'], product['base_factor'], pg_lookup[product['group_id']])



if __name__ == "__main__":
    main()
