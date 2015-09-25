"""
Poll for market data every 1 second and print bid/ask in blue/red
"""

import sys
import threading
from citytrader.request_client import RequestClient
from citytrader.helpers import price_to_decimal

#   gather user auth input and init RequestClient()
def main():
    client_id = raw_input('Enter your client_id: ')
    client_secret = raw_input('Enter your client_secret: ')
    username = raw_input('Enter your username: ')
    password = raw_input('Enter your password: ')
    rc = RequestClient(server="https://devservices.optionshop.com", client_id=client_id, client_secret=client_secret, username=username, password=password)
    instrument_id = raw_input('Enter instrument_id: ')

    instrument = rc.request(request_type="GET", url="instruments/%s" % instrument_id)
    product = rc.request(request_type="GET", url="products/%s" % instrument["data"]["product_id"])
    display_factor = product["data"]["display_factor"]
    base_factor = product["data"]["base_factor"]

    sys.stdout.write("\x1b]2;" + instrument["data"]["name"] + " market data poller" + "\x07")
    print '\033[1;34m' + '%8s' % 'Bid' + '\033[1;m', '\033[1;31m' + '%20s' % 'Ask' + '\033[1;m', '\033[0m'

    poll_md(rc, instrument_id, display_factor, base_factor)


#   print md
def poll_md(rc, instrument_id, display_factor, base_factor):
    threading.Timer(1.0, poll_md, [rc, instrument_id, display_factor, base_factor]).start()
    md_message = rc.request(request_type="GET", url="marketdata?instrument_ids=%s" % instrument_id)

    buy_price = None
    buy_quantity = None
    sell_price = None
    sell_quantity = None
    for i in md_message["data"]:
        if i['side'] == "Buy":
            buy_price = price_to_decimal(i['price'], display_factor, base_factor)
            buy_quantity = i['quantity']
        elif i['side'] == "Sell":
            sell_price = price_to_decimal(i['price'], display_factor, base_factor)
            sell_quantity = i['quantity']

    if buy_price and sell_price:
        bid_str = "%s @ %s" % (buy_quantity, buy_price)
        ask_str = "%s @ %s" % (sell_quantity, sell_price)

        print '\033[1;34m' + bid_str + '\033[1;m', '\033[1;31m' + '%20s' % ask_str + '\033[1;m', '\033[0m'

if __name__ == "__main__":
    main()
