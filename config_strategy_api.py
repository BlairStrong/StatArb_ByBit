#API link
#https://bybit-exchange.github.io/docs/linear/#t-introduction

#API imports
from pybit import HTTP
from pybit import usdt_perpetual
import time



# CONFIG
mode = "test"
timeframe = 60
kline_limit = 200
z_score_window = 30

#LIVE API DATA
api_key_mainnet = ""
api_secret_mainnet = ""

#TEST API DATA
api_key_testnet = "tSlxIPDxxvzSyi0n3O"
api_secret_testnet = "JHRrUCdt1fdBIAm3IUFuqerJIwRzr3B7HFRe"

#selected API
api_key = api_key_testnet if mode == "test" else api_key_mainnet
api_secret = api_secret_testnet if mode == "test" else api_secret_mainnet

#selected URL
api_url = "https://api-testnet.bybit.com" if mode == "test" else "https://api.bybit.com"

#Session Activation
session_unauth = usdt_perpetual.HTTP(endpoint="https://api-testnet.bybit.com")

#session = HTTP(api_url)
# while True:
#     print(session_unauth.query_kline(
#         symbol="BTCUSDT",
#         interval=1,
#         limit=1,
#         from_time=1581231260
#         ))
#     time.sleep(1)

# #Web socket connection
# subs = [
#     "candle.1.BTCUSDT"
# ]
# ws = WebSocket(
#     "wss://stream-testnet.bybit.com/realtime_public",
#     subscriptions=subs
# )


