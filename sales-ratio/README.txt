Assignment
Author: Ridhwaan

To run the program:
- Place the sales-ratio.py program, requirements.txt, sales_date.csv and product_data.json in the same directory ideally
- In Terminal, `cd` to the directory containing sales-ratio.py
- Run `python --version` to ensure that python at least version 2.7+ or python3
- Run `pip install -r requirements.txt` or pip install the packages individually i.e. pip install argparse, os, pandas, json
- Run `python sales-ratio.py sales_data.csv product_data.json`
- If the csv and json files are not in the same directory, reference the relative path for the python argparser

I chose python because it is fast for scripting, not too verbose and has a large data science library  

Either load the CSV in a SQLlite database and query programmatically for the top sales ratio, or use a data analysis library. 
I chose Pandas (https://pandas.pydata.org/, NumPy) because it is versatile, easy to create a sales data table from csv, and features SQL-like methods like select, joins, and filters. Rule of thumb, if it is a one off query: csv module or SQL connection otherwise use pandas  

One assuption was to query for the Order_date and not Ship_date because the assignment uses order date in its peak/nonpeak products definition  
Excerpt: "That is, for each product type, we want to find the number of sales during the peak period (which we'll define here as "all orders placed in October, November and December") divided by the number of sales during the non-peak period (orders placed in any other month), and display the five product types with the highest result" 

I found the top five product types with the best peak / non-peak sales ratio by loading the sales data into a python dataframe and then selecting peak products which had ship dates between oc  
Then, cross reference the product ids with product_data json to get the product type or name and print in python.
Dependencies used: argparse, os, pandas, json. See requirements.txt

TODO: unit tests

One issue in the assignment was the product_data.json file provided (attached) had incomplete data and was missing information (product name, type, class, packaging) on some product ids. The missing product ids were:
'CSN1059', 'TRPT3378', 'GRKS8013', 'VVRE4106', 'TRPT4546' 'IRI1672', 'GRKS8012', 'WDLN2941', 'BCMH2001', 'CHMB1696'
My options were to either alter my submission to omit some information on the top 5 peak/non-peak sales ratios or use a new product_data.json which contains the missing data.
