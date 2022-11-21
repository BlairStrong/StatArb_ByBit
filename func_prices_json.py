from func_price_klines import get_price_klines
import json

# Store price histry for all available pairs
def store_price_history(symbols):

    # Get prices and store in DataFrame
    counts_stored = 0
    counts_not_stored = 0
    price_history_dict = {}

    print(f"Symbols to get prices for: {symbols}")
    for sym in symbols:
        symbol_name = sym["name"]
        price_history = get_price_klines(symbol_name)
        if len(price_history) > 0:
            price_history_dict[symbol_name] = price_history
            counts_stored += 1
            print(f"{counts_stored} items stored")
        else:
            counts_not_stored += 1
            print(f"{counts_not_stored} items not stored")

    # Output prices to JSON
    if len(price_history_dict) > 0:
        with open("1_price_list.json", "w") as fp:
            json.dump(price_history_dict, fp, indent=4)
        print("Prices saved successfully.")

    # Return output
    return

