Assignment
Author: Ridhwaan

To run the program:
- Place the sales-ratio.py program, requirements.txt, sales_date.csv and product_data.json in the same directory ideally
- In Terminal, `cd` to the directory containing sales-ratio.py
- Run `python --version` to ensure that python at least version 2.7+ or python3
- Run `pip install -r requirements.txt` or pip install the packages individually i.e. pip install argparse, os, pandas, json
- Run `python sales-ratio.py sales_data.csv product_data.json`
- If the csv and json files are not in the same directory, reference the relative path for the python argparser

I decided to implement the solution in python because it is a ideal language for scripting automation, not too verbose and has a lot of strong backend and frontend packages.

My options were to load the CSV in a SQLlite database and query programmatically for the top sales ratio in python SQL connection, or use a csv python package like the pandas python module. As a rule of thumb, if it is a one off query: csv module or SQL otherwise use pandas
One reason I chose pandas (https://pandas.pydata.org/, NumPy) because it is powerful for data analysis and more versatile than SQL in ways. It feature SQL-like methods so I was easily able to create a sales data table from csv, and run select, joins, and filter clauses as needed. So the tradeoff was not explicitly using a sql db connection

For this assignment, one assuption I made was to query for the Order_date and not Ship_date because the assignment uses order date in its peak/nonpeak products definition, it could be negligible
excerpt: "That is, for each product type, we want to find the number of sales during the peak period (which we'll define here as "all orders placed in October, November and December") divided by the number of sales during the non-peak period (orders placed in any other month), and display the five product types with the highest result" 

I found the top five product types with the best peak / non-peak sales ratio by first getting the file via input and loading the sales data into a python dataframe, which is a table. I then selected the peak products which had ship dates between oc

At the end, I would cross reference the product ids with product_data json in python to get the product type or name and print the answer.

My python solution is a standalone script which is easy to move around or integrate, and can be attached to a cronjob or jenkins to run on a schedule.
Dependencies used: argparse, os, pandas, json. Provided requirements.txt

Due to time constraints, I did not fully create the unit tests suite as the sample product data csv and json files provided are good enough. I would have planned to create a set of data driven tests which would take in good and bad data (malformed edge cases, null or missing)

One issue I came across in the take home was  The product_data.json file provided (attached) had incomplete data and was missing information (product name, type, class, packaging) on some product ids. The missing product ids were:
'CSN1059', 'TRPT3378', 'GRKS8013', 'VVRE4106', 'TRPT4546' 'IRI1672', 'GRKS8012', 'WDLN2941', 'BCMH2001', 'CHMB1696'
This issue was a potential blocker in my submission so my options were to either alter my solution to omit some information on the top 5 peak/non-peak sales ratios or use a new product_data.json which contains the missing data.
