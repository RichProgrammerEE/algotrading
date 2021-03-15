import talib
from zipline.api import order_target, record, symbol, order_target_percent

def initialize(context):
    stocklist = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOGL']
    # Insert symbols into context
    context.stocks = [symbol(s) for s in stocklist]
    # Set portfolio weighting
    context.target_pct_per_stock = 1.0 / len(context.stocks)
    # Set the RSI thresholds
    context.LOW_RSI = 30
    context.HIGH_RSI = 70

def handle_data(context, data):
    # Historical data
    prices = data.history(context.stocks, 'price', bar_count=20, frequency='1d')

    rsis = dict()

    # Loop through the stocks
    for stock in context.stocks:
        # Calculate RSI based on 14 day rolling window
        # Execute trade based on prior day
        rsi = talib.RSI(prices[stock], timeperiod=14)[-1]
        rsis[stock] = rsi

        current_position = context.portfolio.positions[stock].amount

        # If the RSI is over 70 and we own shares, time to SELL
        if rsi > context.HIGH_RSI and current_position > 0 and data.can_trade(stock):
            order_target(stock, 0)
        elif rsi < context.LOW_RSI and current_position == 0 and data.can_trade(stock):
            order_target_percent(stock, context.target_pct_per_stock)

    record(fb_rsi=rsis[symbol('FB')],
        amzn_rsi=rsis[symbol('AMZN')],
        aapl_rsi=rsis[symbol('AAPL')],
        nflx_rsi=rsis[symbol('NFLX')],
        googl_rsi=rsis[symbol('GOOGL')])


