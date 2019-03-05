#!/usr/bin/env python
import argparse
import os
import pandas 
import json

def main():
    parser = argparse.ArgumentParser(description="Five product types with the best peak / non-peak sales ratio")
    parser.add_argument("sales_data", type=lambda x: validate(parser, x), help="SalesData.csv file")
    parser.add_argument("product_data", type=lambda y: validate(parser, y), help="ProductData.json file")
    args = parser.parse_args()
    sales_data = pandas.read_csv(args.sales_data)
    sales_data.Order_Date = pandas.to_datetime(sales_data.Order_Date, format='%Y-%m-%d %H:%M:%S.%f')
    sales_data.Ship_Date = pandas.to_datetime(sales_data.Ship_Date, format='%Y-%m-%d %H:%M:%S.%f')
    sales_data.sort_values('Product_ID', inplace=True)

    with open(args.product_data) as file:
        product_data = json.load(file)
    '''
    One assuption I made was to query for the Order_date and not Ship_date because the assignment uses order date in its peak/nonpeak products definition.
    Replacing sales_data.Order_Date with sales_data.Ship_Date will return five different product IDs
    '''
    peak_products = sales_data[sales_data.Ship_Date.dt.month.isin([10,11,12])]
    peak_products = peak_products.Product_ID.value_counts().reset_index()
    peak_products.columns = ['Product_ID', 'count']
    peak_products.sort_values('Product_ID', inplace=True)
    #print(peak_products)

    non_peak_products = sales_data[sales_data.Ship_Date.dt.month.between(1,9, inclusive=True)]
    non_peak_products = non_peak_products.Product_ID.value_counts().reset_index()
    non_peak_products.columns = ['Product_ID', 'count']
    non_peak_products.sort_values('Product_ID', inplace=True)
    #print(non_peak_products)
    
    common_products = pandas.merge(peak_products, non_peak_products, on=['Product_ID'])
    common_products.columns = ['Product_ID','peak_frequency', 'non_peak_frequency']
    common_products.reset_index(inplace=True, drop=True)
    common_products['frequency_ratio'] = common_products.peak_frequency / common_products.non_peak_frequency
    
    print(common_products.nlargest(5, ['frequency_ratio']))
    topfive = common_products.nlargest(5, ['frequency_ratio'])['Product_ID'].tolist() 
    print('The top five product types with the best peak / non-peak sales ratio are: \n' + str(topfive))
    
    '''
    One issue I came across in the take home was the product_data.json file provided (attached) had incomplete data and was missing information (product name, type, class, packaging) on some product ids. The missing product ids were:
    'CSN1059', 'TRPT3378', 'GRKS8013', 'VVRE4106', 'TRPT4546' 'IRI1672', 'GRKS8012', 'WDLN2941', 'BCMH2001', 'CHMB1696'
    This issue was a potential blocker in my submission so my options were to either alter my solution to omit some information on the top 5 peak/non-peak sales ratios or use a new product_data.json which contains the missing data.
    '''
    for key in product_data:
        if str(key["Product_Id"]) in topfive:
            print(key["Product_Id"] + ': ' + key["Product_Name"])

def validate(parser, arg):
    arg = os.path.abspath(arg)
    if not os.path.exists(arg):
        parser.error("The file '%s' does not exist. Try again" % arg)
    else:
        return arg

if __name__ == "__main__":
    main()

'''
Sample output:

if Order_Date is used:
    Product_ID  peak_frequency  non_peak_frequency  frequency_ratio
     IRI1672              64                   1             64.0
    GRKS8012              41                   1             41.0
    WDLN2941              30                   1             30.0
    BCMH2001              54                   2             27.0
    CHMB1696              26                   1             26.0

if Ship_Date is used:
    Product_ID  peak_frequency  non_peak_frequency  frequency_ratio
     CSN1059              95                   1             95.0
    TRPT3378              55                   1             55.0
    GRKS8013              39                   1             39.0
    VVRE4106              31                   1             31.0
    TRPT4546              30                   1             30.0
'''