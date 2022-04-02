## Portfolio

## About the project

---

> The following is the implementation of a portfolio class in which the profit between two given dates is returned.


### portfolio.py

In this file is the **class** `Portfolio` which receives a ***list of stocks*** and contains a **method** called `Profit`, this takes as input a ***start date and an end date***, and **returns the difference between the prices** of these dates, this ***difference is the profit obtained between both dates***.

### stock.py 

This file contains a **class** `Stock` which has a **method** called `Price`, which takes as input an ***any date*** and **returns the price for that date**.

In this file there is also a **class** `PriceNotFoundError`, this is the ***error handling*** for when a date is entered that is not in stock.

### main.py

In this file is not only the `main` function that does all the magic, it also contains a simulation of a stock stock composed as follows: 

~~~
s1 = Stock(
            "Google", 
            {
                datetime(2019, 1, 1): 12, 
                datetime(2020, 1, 2): 20
            })
~~~

* A list containing

    * The name of the stock 

    * A dictionary with type `datetime` whose key is the date of the stock and value is the price of that stock.

It also contains a ***menu*** which is composed as follows: 

---
~~~
        Choose what you want to do. Options are:
            
            **************************************************************
            * a. Profit of the Portfolio                                 *
            * b. Annualized Profitability of the Portfolio               *
            * c. All                                                     *
            * q. Quit                                                    *
            **************************************************************
        
        Please enter your choice:
        
~~~
---
* A menu that gives you the options to 

    * Only get the profit between the selected dates

    * Obtain only the profitability between the selected dates

    * Obtain both the profit and the annualized profitability between the selected dates. 

    * And the option to exit the program once you have finished the consultation.

* In addition, each time you select an option and it returns the desired answer, the program is restarted asking you to select a new option.


### tests

In this module you will find the tests of the above mentioned files.

* *test_portfolio.py*

    * This file contains the test case of the `Profit` method which tests the expected result of both the profit and the annualized profitability. 

* *test_stock.py*

    * In this file you can find the test case of the `Stock` method which tests the expected result of the `price` method both from the error handling seen in the `except`.


## Usage

---

To run the project use the command

~~~
python main.py
~~~

To run the tests

~~~
python -m unittest
~~~

