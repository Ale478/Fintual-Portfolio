class Stock:
    
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices
    
    # Receives a date and returns the price for that date

    def price(self, date):
        return(self.prices[date])