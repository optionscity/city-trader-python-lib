# city-trader-python-lib
A python library for working with OptionsCity Software's City Trader REST API.

#### Getting started
1. Make sure you have python 2.7 or greater installed
2. Run: "python setup.py install" to make city-trader-python-lib available globally

#### The following examples assume you have a City Trader API:
1. dev username and password
2. dev client_id and client_secret

#### Initialize client and retrieve new token
```python
from citytrader.request_client import RequestClient
rc = RequestClient(server="https://devservices.optionshop.com", client_id="<client_id>", client_secret="<client_secret>", username="<username>", password="<password>")
```

#### Retrieve all orders
```python
all_orders = rc.request(request_type="GET", url="orders")
```

#### Retrieve single order
```python
single_order = rc.request(request_type="GET", url="orders/<order_id>")
```

#### Retrieve all product groups
```python
all_productgroups = rc.request(request_type="GET", url="productgroups")
```

#### Retrieve all instruments
```python
all_instruments = rc.request(request_type="GET", url="instruments")
```

#### Retrieve market data for a single instrument
```python
md_message = rc.request(request_type="GET", url="marketdata?instrument_ids=<instrument_id>")
```

#### Retrieve market data for multiple instruments
```python
md_messages = rc.request(request_type="GET", url="marketdata?instrument_ids=<instrument_id_1>&instrument_ids=<instrument_id_2>")
```

#### Retrieve market data for just Last and High prices
```python
md_messages_just_last_and_high = rc.request(request_type="GET", url="marketdata?instrument_ids=<instrument_id_1>&instrument_ids=<instrument_id_2>&sides=Last&sides=High")
```

#### Submit a day limit order
```python
order_results = rc.request(request_type="POST", url="orderactions", data={"acct_id": <account_id>, "action_type": "LimitOrderSub", "instrument_id": <instrument_id>, "limit_price": <limit_price>, "quantity": <quantity>, "side": <side>, "time_in_force": "Day"})
```
