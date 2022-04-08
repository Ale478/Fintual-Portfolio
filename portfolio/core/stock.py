class PriceNotFoundError(Exception):
    """ Raises an error when price is not found



    Attributes:
        stock_name: represents the name of the stock. 
    """

    def __init__(self, stock_name):
        super().__init__(f"Price for stock {stock_name} not found")


class Stock:
    """ Represents a stock with its historical prices


    Attributes:
        name: represents the name of the stock
        prices: represents the historical prices of the stock
    """

    def __init__(self, name, prices):
        self.name = name
        self.prices = prices

    # Receives a date and returns the price for that date

    def price(self, date):
        """ Returns the share price according to its date.


        Args:
            date {datetime}: date of the stock to query.

        Returns:
            price_stock: price of the queried stock.
        
        Raises:
            raises error when a price is not found
        """
        try:
            price_stock = self.prices[date]
        except KeyError:
            raise PriceNotFoundError(self.name)

        return price_stock
