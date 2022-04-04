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

    def test_profit_Error(self):
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
        date2 = datetime(2022, 2, 19)
        portfolio, portfolio2 = myportfolio.profit(date1, date2)
        self.assertEquals(portfolio, 0)


    def test_anualizedReturn(self):
        s1 = Stock("Samsung", {
            datetime(2021, 11, 16): 15,
            datetime(2022, 12, 20): 20
        })

        s2 = Stock("Dell", {
            datetime(2021, 11, 16): 20,
            datetime(2022, 12, 20): 25
        })
        myportfolio = Portfolio([s1, s2])
        date1 = datetime(2021, 11, 16)
        date2 = datetime(2022, 12, 20)
        portfolio, portfolio2 = myportfolio.profit(date1, date2)
        self.assertEquals(portfolio2,0.2613677049767276)


    def test_anualizedReturn_Error(self):
        s1 = Stock("Samsung", {
            datetime(2021, 11, 16): 15,
            datetime(2022, 12, 20): 20
        })

        s2 = Stock("Dell", {
            datetime(2021, 11, 16): 20,
            datetime(2022, 12, 20): 25
        })
        myportfolio = Portfolio([s1, s2])
        date1 = datetime(2020, 2, 6)
        date2 = datetime(2022, 12, 20)
        portfolio, portfolio2 = myportfolio.profit(date1, date2)
        self.assertEquals(portfolio2,0)


if __name__ == "__main__":
    unittest.main()
