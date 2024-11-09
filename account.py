import MetaTrader5 as mt5
import pandas as pd
if not mt5.initialize(login=143894, server="EGMSecurities-Demo",password="Gods_child57"):
    print("initialize() failed, error code =",mt5.last_error())
    quit()
# display data on connection status, server name and trading account
print(mt5.terminal_info())
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": 'EURUSD',
    "volume": 0.01,
    "type": mt5.ORDER_TYPE_SELL,
    "price": mt5.symbol_info_tick('EURUSD').ask,
    "comment": "Quantra Market Buy Order",
}
order_result = mt5.order_send(request)
if order_result.retcode != mt5.TRADE_RETCODE_DONE:
    print("Error placing order: ", order_result.comment)
else:
    print("Order placed successfully, order ticket:", order_result.order)