"""
Interval: 60, D
from: integer from timestap in seconds
limit: Max size of 200
"""

from config_strategy_api import session_unauth
from config_strategy_api import timeframe
from config_strategy_api import kline_limit
import datetime
import time

#Get Start time << the below is listing a set of option for if we choose to do either 60 mins (hourly) or Daily. we could also add if statements to accomodate all the other different time periods.
time_start_date = 0
if timeframe == 1:
    time_start_date = datetime.datetime.now() - datetime.timedelta(minutes=kline_limit)
if timeframe == 60:
    time_start_date = datetime.datetime.now() - datetime.timedelta(hours=kline_limit)
if timeframe == "D":
    time_start_date = datetime.datetime.now() - datetime.timedelta(days=kline_limit)
time_start_seconds = int(time_start_date.timestamp())

#Get historical prices (klines)
def get_price_klines(symbol):

    #get prices
    prices = session_unauth.query_mark_price_kline(
        symbol = symbol,
        interval = timeframe,
        limit = kline_limit,
        from_time = time_start_seconds
    )

    #manage API calls
    time.sleep(0.15)

    #return output
    if len(prices["result"]) != kline_limit:
        return []    # << if there is not 200 entry in this deictionary, (result is a standard dict component in each item of data) then we assume there is not 200 days (or whatever period you are using) worth of data and we want to avoid using this.
    return prices["result"]

