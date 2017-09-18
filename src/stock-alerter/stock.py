import bisect
import collections

PriceEvent = collections.namedtuple("PriceEvent", ["timestamp", "price"])

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = []
        # self.price = None

    # mimics the price property which now no longer exists
    # we've changed it to price_history
    # accessing Stock.price will call this method
    # price can be accessed as an attribute althoug it
    # no longer exists as such
    @property
    def price(self):
        return self.price_history[-1].price \
        if self.price_history else None

    def update(self, timestamp, price):
        if price < 0:
           raise ValueError("price should not be negative")
        bisect.insort_left(self.price_history, PriceEvent(timestamp, price))


    def is_increasing_trend(self):
        return self.price_history[-3].price < \
               self.price_history[-2].price < \
               self.price_history[-1].price
