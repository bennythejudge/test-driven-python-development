
class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = []
        # self.price = None


    def update(self, timestamp, price):
        if price < 0:
           raise ValueError("price should not be negative")
        self.price_history.append(price)

    # mimics the price property which now no longer exists
    # we've changed it to price_history
    # accessing Stock.price will call this method
    # price can be accessed as an attribute althoug it
    # no longer exists as such
    @property
    def price(self):
        return self.price_history[-1] \
        if self.price_history else None

    def is_increasing_trend(self):
        return self.price_history[-3] < \
               self.price_history[-2] < \
               self.price_history[-1]
