import unittest, mock, patch
from unittest import result
from portfolio import main
from portfolio.tests.testFixtures import invalid_format


class TestInputDate(unittest.TestCase):

    @patch('builtins.input', return_value="2019/1/1")
    def test_date_invalid(self, mock_input):
        date = main()
       

    """
    def test_input_date(self):        
        with self.assertRaises(ValueError):
            invalid_format(True)
    """
 
    