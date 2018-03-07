#!/usr/bin/env python3
"""
Reads files (tweets_aa, tweets_ab, tweets_ac) and returns the count breakdown in areas for the search keyword
Keep tweets.py and the given files in the same root directory

EXAMPLE:
$ python tweets.py knicks

OUTPUT:
Count results for 'knicks'

In 'tweets_ac':
Bronx 16
Brooklyn 12
Staten Island 11
Manhattan 13
Queens 13
TOTAL: 65

In 'tweets_ab':
Bronx 13
Brooklyn 19
Staten Island 8
Manhattan 58
Queens 21
TOTAL: 119

In 'tweets_aa':
Bronx 20
Brooklyn 31
Staten Island 10
Manhattan 53
Queens 42
TOTAL: 156

GRAND TOTAL: 340
"""

__author__ = "Ridhwaan Shakeel"
__version__ = "0.1.0"

import os
import argparse
from copy import deepcopy

AREAS = ['Brooklyn','Bronx','Manhattan','Queens','Staten Island']

def main(args):

	count = {}
	for area in AREAS:
		count[area] = 0

	results = {}
	for file in ['tweets_aa','tweets_ab','tweets_ac']:
		# each tweets file has a dictionary to track count
		results[file] = deepcopy(count)

		with open(file) as tweets:
			for line in tweets:
				for area in AREAS:
					# if area is valid and has 'knicks' at least once (case-insenstive)
					if line.startswith(area) and args.keyword in line:
						results[file][area] += 1

	# print the breakdown
	print("\nCount results for '{}'".format(args.keyword))
	for file in results:
		print("\nIn '{}': ".format(file))
		for area in results[file]:
			print("{} {}".format(area, results[file][area]))
		print("TOTAL: {}".format( sum(results[file].values())) )
	print ("\nGRAND TOTAL: {}".format( sum(x for counter in results.values() for x in counter.values()) ))



if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument("keyword", help="Keyword to search for i.e. knicks")

	args = parser.parse_args()
	main(args)