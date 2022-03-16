import unittest
from portfolio.core.portfolio import Portfolio
from portfolio.core.stock import Stock
from datetime import datetime



class TestStockPrice(unittest.TestCase):
    
    def test_price(self):
        mystock = Stock(
            "Android",
            {
                datetime(2020,10,15): 15,
                datetime(2021,11,20): 25

            }
        )
        stock1 = mystock.price(datetime(2020,10,15))
        stock2 = mystock.price(datetime(2021,11,20))
        self.assertEqual(stock1,15)
        self.assertEqual(stock2,25)


class TestPortfolioProfit(unittest.TestCase):

    def test_profit(self):
        s1 = Stock(
            "Xiaomi",
            {
                datetime(2020,10,6): 10,
                datetime(2021,4,9): 20
                
            }
        )

        s2 = Stock(
            "Lenovo",
            {
                datetime(2020,10,6): 15,
                datetime(2021,4,9): 25
            }
        )
        myportfolio = Portfolio([s1,s2])
        date1 = datetime(2020,10,6)
        date2 = datetime(2021,4,9)
        portfolio = myportfolio.profit(date1,date2)
        self.assertEquals(portfolio,20)


if __name__ == "__main__":
    unittest.main()