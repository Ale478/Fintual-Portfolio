from portfolio.core.stock import PriceNotFoundError


class Portfolio:
    """ Represents a person's portfolio along with their stocks.

    Provides profits and annualized returns based on 
    a given period of dates
    
    Attributes:
        stocks: represents the stocks in a portfolio.
    """

    def __init__(self, stocks):
        self.stocks = stocks

    # Receives two dates and returns the benefit between those dates

    def profit(self, date_1, date_2):
        """ Returns the annual profit and return.
        

        Args:
            date_1 {datetime}: start date.
            date_2 {datetime}: end date

        Returns:
            profits: profit between the two dates
            annualized_return: annualized return between the two dates 
        
        """
        profits = 0
        init_value = 0
        final_value = 0
        date_diff = (date_2 - date_1).days
        annualized_return = 0

        for stock in self.stocks:
            try:
                date1 = stock.price(date_1)
                date2 = stock.price(date_2)
                init_value += date1
                final_value += date2
                profits += date2 - date1
            except PriceNotFoundError as e:
                print("\n", e)
        try:
            annualized_return = (
                        (final_value / init_value) - 1) * (365 / date_diff)
        except ZeroDivisionError as e:
            print("\n", e)

        return (profits, annualized_return)
