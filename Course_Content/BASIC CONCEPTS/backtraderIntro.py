from __future__ import(absolute_import, division, print_function, unicode_literals)

import backtrader as bt

if __name__ == '__main__':

    cerebro = bt.Cerebro()

    print("The starting portfolio value : ", cerebro.broker.getvalue())

    cerebro.run()

    print("Final portfolio value: ", cerebro.broker.getvalue())