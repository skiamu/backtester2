# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:46:04 2021

@author: skia_
"""
from zipline.api import order, record, symbol
from zipline.finance import commission, slippage
from zipline import run_algorithm
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# def initialize(context):
#     ...

# def handle_data(context, data):
#     order(symbol('AAPL'), 10)
#     record(AAPL=data[symbol('AAPL')].price)

def initialize(context):
    context.asset = symbol("AAPL")

    # Explicitly set the commission/slippage to the "old" value until we can
    # rebuild example data.
    # github.com/quantopian/zipline/blob/master/tests/resources/
    # rebuild_example_data#L105
    context.set_commission(commission.PerShare(cost=0.0075, min_trade_cost=1.0))
    context.set_slippage(slippage.VolumeShareSlippage())


def handle_data(context, data):
    order(context.asset, 10)
    record(AAPL=data.current(context.asset, "price"))




start = pd.Timestamp('2014')
end = pd.Timestamp('2017')

sp500 = web.DataReader('SP500', 'fred', start, end).SP500
benchmark_returns = sp500.pct_change()

result = run_algorithm(start=start.tz_localize('UTC'),
                       end=end.tz_localize('UTC'),
                       initialize=initialize,
                       handle_data=handle_data,
                       capital_base=100000,
                       benchmark_returns=benchmark_returns,
                       bundle='quandl',
                       default_extension = False,
                       data_frequency='daily')