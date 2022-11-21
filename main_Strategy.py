import pandas as pd
import warnings
import json
from func_cointegration import get_cointegrated_pairs
from func_get_symbols import get_tradeable_symbols
from func_prices_json import store_price_history
from func_plot_trends import plot_trends
warnings.simplefilter(action='ignore', category=FutureWarning)

""" Strategy Code"""

if __name__ == "__main__":

    """STEP 1 and STEP 2 are to collect data. They can be run whenever wanted, but do not need to run consistently. PLEASE uncomment step 1 and step 2 to update the data."""
    #
    # STEP 1 - Get list of symbols
    print("Getting symbols...")
    sym_list = get_tradeable_symbols()
    print("Step 1 complete")

    # STEP 2 - Construct and save price history
    print("Constructing and saving price data to JSON...")
    if len(sym_list) > 0:
        print("List has info:")
        store_price_history(sym_list)
        print("Price history constructed and saved")
    #
    #STEP 3 - Find Cointegrated pairs
    print("Step 3: Calculating co-integration...")
    with open("1_price_list.json") as json_file:
        price_data = json.load(json_file)
        if len(price_data) > 0:
            coint_pairs = get_cointegrated_pairs(price_data)
    print("Co-integration Calculated.")

    #STEP 4 - Plot Trends and Save for Backtesting
    print("Step 4 - Plotting Trends")
    symbol_1 = "BNBUSDT"
    symbol_2 = "APEUSDT"
    with open("1_price_list.json") as json_file:
        price_data = json.load(json_file)
        if len(price_data) > 0:
            plot_trends(symbol_1, symbol_2, price_data)




