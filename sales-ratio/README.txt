Assignment  

Instructions:  
- Put sales-ratio.py, requirements.txt, sales_date.csv and product_data.json in the same directory  
- In Terminal, `cd` to the directory containing sales-ratio.py  
- Run `python --version` to check for python 2.7+ or python3  
- Run `pip install -r requirements.txt`  
- Run `python sales-ratio.py sales_data.csv product_data.json`  
- If the csv and json files are not in the same directory, reference the relative path  

I chose Python because it is simple and easy for scripting  
Libraries used: argparse, os, pandas, json. See requirements.txt  

Either load the CSV in a SQLlite database and query programmatically for the top sales ratio, or use a data analysis library.  
I chose Pandas (https://pandas.pydata.org/, NumPy) because it is easy to create and query from a data table out of CSV     

I found the top five product types with the best peak / non-peak sales ratio by putting the sales data into a python dataframe and then selecting peak products which had ship dates between oc  
Then, cross reference the product ids with product_data json to get the product type or name and print them  

Excerpt: "That is, for each product type, we want to find the number of sales during the peak period (which we'll define here as "all orders placed in October, November and December") divided by the number of sales during the non-peak period (orders placed in any other month), and display the five product types with the highest result"   

One assumption was to query for Order_date and not Ship_date because the assignment uses order date in its peak/nonpeak products definition.  
Replacing sales_data.Order_Date with sales_data.Ship_Date will return five different product IDs  

One issue was the product_data.json file provided had incomplete data and missing information such as product name, type, class, packaging on some product ids.   
The missing product ids were: 'CSN1059', 'TRPT3378', 'GRKS8013', 'VVRE4106', 'TRPT4546' 'IRI1672', 'GRKS8012', 'WDLN2941', 'BCMH2001', 'CHMB1696'  
My options were to either alter my solution to omit some information on the top 5 peak/non-peak sales ratios or use a new product_data.json which contains the missing data.  