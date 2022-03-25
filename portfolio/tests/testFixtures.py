
from portfolio.core.stock import  PriceNotFoundError
from datetime import datetime


def price_not_found():
    raise PriceNotFoundError('Price for stock {stock_name} not found')


def invalid_format():
    raise ValueError('Invalid format entered :(, please try again!')


