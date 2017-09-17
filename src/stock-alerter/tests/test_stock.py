import unittest
from stock import Stock
from datetime import datetime


class StockTest(unittest.TestCase):

    def setUp(self):
        self.goog = Stock('GOOG')

    def test_price_of_a_new_stock_class_should_be_None(self):
        # stock = Stock("GOOG")
        self.assertIsNone(self.goog.price)

    def test_stock_update(self):
        """An Update should set the price on the stock object
        We will be using the `datetime` module for the timestamp
        """
        # goog = Stock("GOOG")
        self.goog.update(datetime(2017, 9, 6), price=10)
        self.assertEqual(10, self.goog.price)

    def test_negative_price_should_throw_ValueError(self):
        # goog = Stock("GOOG")
        # try:
        #     goog.update(datetime(2017, 9, 6), -1)
        # except ValueError:
        #     return
        # self.assertRaises(ValueError, goog.update, datetime(2017, 9, 6), -1)
        #self.fail("ValueError was not raised")
        with self.assertRaises(ValueError):
            self.goog.update(datetime(2017, 9, 6), -1)

    def test_stock_price_should_give_the_latest_price(self):
        # goog = Stock('GOOGLE')
        self.goog.update(datetime(2017, 9, 6), price=10)
        self.goog.update(datetime(2017, 9, 7), price=8.4)
        self.assertAlmostEqual(8.4, self.goog.price, delta=0.0001)


class StockTrendTest(unittest.TestCase):
    def setUp(self):
        self.goog = Stock('GOOG')

    # a helper method
    def given_a_series_of_prices(self, prices):
        timestamps = [datetime(2014, 2, 11), datetime(2014, 2, 12), \
                      datetime(2014, 2, 13), datetime(2014, 2, 14)]
        for timestamp, price in zip(timestamps, prices):
            self.goog.update(timestamp, price)

    def test_increasing_trend_is_true_if_price_increase_for_3_updates(self):
        self.given_a_series_of_prices([8, 10, 12])
        self.assertTrue(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_decreases(self):
        self.given_a_series_of_prices([12, 10, 8])
        self.assertFalse(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_equal(self):
        self.given_a_series_of_prices([1, 1, 1])
        self.assertFalse(self.goog.is_increasing_trend())


if __name__ == "__main__":
    unittest.main()
