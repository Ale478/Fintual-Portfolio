class PriceNotFoundError(Exception):

    def __init__(self, stock_name):
        super().__init__(f"Price for stock {stock_name} not found")


class Stock:

    def __init__(self, name, prices):
        self.name = name
        self.prices = prices

    # Receives a date and returns the price for that date

    def price(self, date):
        try:
            price_stock = self.prices[date]
        except KeyError:
            raise PriceNotFoundError(self.name)

        return price_stock
