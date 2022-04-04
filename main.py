from portfolio.core.portfolio import Portfolio
from portfolio.core.stock import Stock
from datetime import datetime

# Stocks of the form name of the stock and
# a dictionary containing the date and price of the stock.

s1 = Stock("Google", {datetime(2019, 1, 1): 12, datetime(2020, 1, 2): 20})

s2 = Stock("Apple", {datetime(2019, 1, 1): 10, datetime(2020, 1, 2): 19})


def main():

    print(f"\nChoose what you want to do. Options are:\n"
          "\n"
          "\t**************************************************************\n"
          "\t* a. Profit of the Portfolio                                 *\n"
          "\t* b. Annualized Profitability of the Portfolio               *\n"
          "\t* c. All                                                     *\n"
          "\t* q. Quit                                                    *\n"
          "\t**************************************************************\n")
    option = input("\n Please enter your choice: ")

    if ((option == 'a') or (option == 'b') or (option == 'c')
            or (option == 'q')):

        while (option != 'q'):
            try:

                date_entry = input(
                    '\n Please enter a first date in YYYY-MM-DD format: ')
                date1 = datetime.strptime(date_entry, "%Y-%m-%d")

                date_entry = input(
                    '\n Please enter a second date in YYYY-MM-DD format: ')
                date2 = datetime.strptime(date_entry, "%Y-%m-%d")

            except ValueError:
                print(f"Invalid format entered :(, please try again!")
                return

            myPortfolio = Portfolio([s1, s2])
            profit, annualized = myPortfolio.profit(date1, date2)
            txt = "The annualized profitability obtained was  {:.2%}"

            if option == 'a':
                print(f"\n The profit obtained was {profit}")
                option = input("\n Please enter your choice: ")

            elif option == 'b':
                print(f"\n", txt.format(annualized))
                option = input("\n Please enter your choice: ")

            elif option == 'c':
                print(f"\n The profit obtained was {profit}")
                print(f"\n", txt.format(annualized))
                option = input("\n Please enter your choice: ")

    if option == 'q':
        print(f"\n Thanks for use the portfolio :) \n")
        quit()

    else:
        print(f"Invalid option entered :(, please try again!")


main()
