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

    try:

        date_entry = input('\n Please enter a first date in YYYY-MM-DD format: ')
        date1 = datetime.strptime(date_entry, "%Y-%m-%d")

        date_entry = input('\n Please enter a second date in YYYY-MM-DD format: ')
        date2 = datetime.strptime(date_entry, "%Y-%m-%d")
    
    except ValueError:
        print(f"Invalid format entered :(, please try again!")
        return


    myPortfolio = Portfolio([s1, s2]) 
    profit, annualized = myPortfolio.profit(date1, date2)
    txt = "The annualized profitability obtained was  {:.0%}"
    
    

    print(f"\n The profit obtained was {profit}")
    print(f"\n", txt.format(annualized))
    print(f"\n Thanks for use the portfolio :) \n")
    


main()