from portfolio import *
from datetime import datetime



s1 = Stock(
    "Google",
    {
        datetime(2019,1,1): 12,
        datetime(2020, 1, 2): 20,

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

    date_entry = input('Enter a first date in YYYY-MM-DD format ')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime(year, month, day)

    date_entry = input('Enter a second date in YYYY-MM-DD format ')
    year, month, day = map(int, date_entry.split('-'))
    date2 = datetime(year, month, day)

    myPortfolio = Portfolio([s1, s2]) 
    portfolio = myPortfolio.profit(date1, date2)

    print(f"The profit obtained was {portfolio}")


main()