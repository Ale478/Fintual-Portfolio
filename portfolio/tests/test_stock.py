import unittest
from portfolio.core.stock import Stock, PriceNotFoundError
from portfolio.tests.testFixtures import price_not_found
from datetime import datetime



class TestPriceError(unittest.TestCase):

    def test_price_not_found(self):
        with self.assertRaises(PriceNotFoundError):
            price_not_found()



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
       # self.assertRaises(PriceNotFoundError,mystock.price(datetime(2019,10,15)))
       # self.assertRaises(PriceNotFoundError,mystock.price(datetime(2022,11,20)))
        


if __name__ == "__main__":
    unittest.main()
    
    