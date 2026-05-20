def simple_strategy(price):
    if price > 50000:
        return "SELL"
    else:
        return "BUY"