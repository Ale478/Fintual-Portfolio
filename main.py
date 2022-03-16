from portfolio.core.portfolio import Portfolio
from portfolio.core.stock import Stock
from datetime import datetime


# Stocks of the form name of the stock and 
# a dictionary containing the date and price of the stock.

s1 = Stock(
    "Google",
    {
        datetime(2019,1,1): 12,
        datetime(2020, 1, 2): 20

    }
)

s2 = Stock(
    "Apple",
    {
        datetime(2019, 1, 1): 10,
        datetime(2020, 1, 2): 19
    }
)


def main():

    
    date_entry = input('\n Please enter a first date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime(year, month, day)

    date_entry = input('\n Please enter a second date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    date2 = datetime(year, month, day)

    myPortfolio = Portfolio([s1, s2]) 
    portfolio = myPortfolio.profit(date1, date2)

    print(f"\n The profit obtained was {portfolio}")
    print(f"\n Thanks for use the portfolio :) \n")


main()