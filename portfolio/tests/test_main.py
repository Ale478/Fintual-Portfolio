import unittest, mock
from portfolio import main
from datetime import datetime
from portfolio.core.stock import Stock
from portfolio.tests.testFixtures import invalid_format


class TestInputDate(unittest.TestCase):
    
    def test_input_date(self):        
        with self.assertRaises(ValueError):
            invalid_format(True)

