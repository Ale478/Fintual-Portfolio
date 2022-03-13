from collections import *
from datetime import datetime


class Stock:
    
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices
    
    def price(self, date):
        return(self.prices[date])

class Portfolio:

    def __init__(self, stocks):
        self.stocks = stocks

    def profit(self, date_1, date_2):
        profits = 0
        for stock in self.stocks:
            profits += stock.price(date_2) - stock.price(date_1)
        return(profits)



