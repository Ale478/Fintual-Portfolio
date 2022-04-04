import unittest
from portfolio.core.portfolio import Portfolio
from portfolio.core.stock import Stock
from datetime import datetime


class TestPortfolioProfit(unittest.TestCase):

    def test_profit(self):
        s1 = Stock("Xiaomi", {
            datetime(2020, 10, 6): 10,
            datetime(2021, 4, 9): 20
        })

        s2 = Stock("Lenovo", {
            datetime(2020, 10, 6): 15,
            datetime(2021, 4, 9): 25
        })
        myportfolio = Portfolio([s1, s2])
        date1 = datetime(2020, 10, 6)
        date2 = datetime(2021, 4, 9)
        portfolio, portfolio2 = myportfolio.profit(date1, date2)
        self.assertEquals(portfolio, 20)
        self.assertEquals(portfolio2, 1.5783783783783785)


if __name__ == "__main__":
    unittest.main()
