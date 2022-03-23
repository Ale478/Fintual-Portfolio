
from portfolio.core.stock import  PriceNotFoundError

def price_not_found():
    raise PriceNotFoundError('Price for stock {stock_name} not found')


def invalid_format(user_input):
    if(user_input):
        raise ValueError('Invalid format entered :(, please try again!')


