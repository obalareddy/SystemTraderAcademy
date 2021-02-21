from datetime import date

import talib as ta
import numpy as nm
#import backtrader

print("Yayyyy")

close_price = nm.random.random(100)
print(close_price)

print(ta.SMA(close_price, timeperiod=20))
