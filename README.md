# Portfolio

## About the project

---

> The following is the implementation of a portfolio class in which profit and annualized return is returned between two given dates.

---

## Installation

To install the project, just run :

~~~
git clone https://github.com/Ale478/Fintual-Portfolio.git
~~~
---

### Example Usage

~~~
from portfolio.core.portfolio import Portfolio
from portfolio.core.stock import Stock
from datetime import datetime

# Create a list of stocks

s1 = Stock("Google", {datetime(2019, 1, 1): 12, datetime(2020, 1, 2): 20})
s2 = Stock("Apple", {datetime(2019, 1, 1): 10, datetime(2020, 1, 2): 19})

# Define the date period

date1 = datetime(2019, 1, 1)
date2 = datetime(2020, 1, 2)


# Create the portfolio 

myPortfolio = Portfolio([s1, s2])

# We call the portfolio methods with the date period

profit, annualized = myPortfolio.profit(date1, date2)
txt = "{:.0%}"

print(f"\n {profit}")
print(f"\n", txt.format(annualized))
~~~

The project has a small program that, when executed by doing.

~~~
python main.py
~~~

It displays the following menu :

---
~~~
        Choose what you want to do. The options are:
            
            **************************************************************
            * a. Portfolio Return                                        * 
            * b. Annualized Portfolio Return                             * 
            * c. All                                                     *
            * q. Exit                                                    *
            **************************************************************
        
        Please enter your choice:
        
~~~

Then you choose an option and enter the date period to query

---

### Bonus Track


For the bonus track we added to the `Profit` method the return of the ***annualized profitability***, this was implemented using the following [formula](https://economipedia.com/definiciones/rentabilidad-anual.html), this can be found in the above mentioned portfolio.py file

~~~
            annualized_return = (
                (end_value / initial_value) - 1) * (365 / difference_date).
~~~

* Both the `initial_value` and `end_value` are the sum of the start and end date prices respectively.

    * It should be noted that although the formula indicates *division by the number of years*, the same is done but expressed in days to take into account the months and days of difference between one year and another. 

---

### Tests


To run the tests :

~~~
python -m unittest
~~~