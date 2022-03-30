from portfolio.core.stock import PriceNotFoundError, Stock




class Portfolio:

    def __init__(self, stocks):
        self.stocks = stocks

    # Receives two dates and returns the benefit between those dates

    def profit(self, date_1, date_2):
        
        profits = 0
        init_value = 0
        final_value = 0
        date_interval = date_2.year - date_1.year 
        annualized_return = 0
        
        for stock in self.stocks:
            try:
                date1 = stock.price(date_1)
                date2 = stock.price(date_2)
                init_value += date1
                final_value += date2
                profits += date2 - date1
                annualized_return = ((final_value/init_value)-1)*(1/date_interval)
            except PriceNotFoundError as e:
                print("\n", e)
            

        

        return(profits, annualized_return)