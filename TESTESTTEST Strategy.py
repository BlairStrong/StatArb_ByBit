from time import sleep
import json
from func_cointegration import extract_close_prices

with open("1_price_list.json") as json_file:
    price_data = json.load(json_file)


def hedge_ratio_blarizonk(ticker_1, ticker_2):
    # Get close prices
    series_1 = extract_close_prices(price_data[ticker_1])
    series_2 = extract_close_prices(price_data[ticker_2])

    print(series_1)
    print(series_2)

    count = 0
    hedge_ratio_list = []
    while count < len(series_1):
        hedge_ratio = series_1[count]/series_2[count]
        print(f"{ticker_1}={series_1[count]}, {ticker_2}={series_2[count]}, Hedge ratio = {hedge_ratio}")
        hedge_ratio_list.append(hedge_ratio)

        print(count)
        count += 1
    hedge_ratio_blarizonk = sum(hedge_ratio_list)/len(hedge_ratio_list)
    print(hedge_ratio_blarizonk)
    return hedge_ratio_blarizonk