from __future__ import(absolute_import, division, print_function, unicode_literals)
from datetime import datetime
from os import close

import backtrader as bt
from datetime import datetime

if __name__ == '__main__':

    cerebro = bt.Cerebro()

    datapath = "Course_Content/DATA/Nifty-1D.csv"

    data = bt.feeds.GenericCSVData(
        dataname = datapath,
        fromdate = datetime(2011,1,1),
        todate = datetime(2018,1,1),
        datetime = 0,
        timeframe = bt.TimeFrame.Days,
        compression = 1,
        dtformat = ('%Y-%m-%d'),
        open = 1,
        high = 2,
        low = 3,
        close = 4,
        volume = None,
        openinterest = None,
        reverse = False,
        header = 0
    )

    cerebro.adddata(data)
    cerebro.broker.setcash(1000000)

    print("The starting portfolio value : ", cerebro.broker.getvalue())

    cerebro.run()

    print("Final portfolio value: ", cerebro.broker.getvalue())
