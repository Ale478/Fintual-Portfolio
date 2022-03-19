from portfolio.core.stock import PriceNotFoundError, Stock




class Portfolio:

    def __init__(self, stocks):
        self.stocks = stocks

    # Receives two dates and returns the benefit between those dates

    def profit(self, date_1, date_2):
        profits = 0

        for stock in self.stocks:
            try:
                date1 = stock.price(date_1)
                date2 = stock.price(date_2)
                profits += date1 - date2
            except PriceNotFoundError as e:
                print("\n e")

        return(profits)