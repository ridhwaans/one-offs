#!/usr/bin/env python3
"""
Append a TMDB MovieID to the names of all recursive files in a directory
"""

import requests
import os
import argparse
import PTN
import re

def main(args):
    """ Main entry point of the app """
    i = 0
    print("hello world")
    print(args.arg)
    for subdir, dirs, files in os.walk(args.arg):
        for file in files:
            m = re.search(r'\d+(.mp4)$', file)
            # if the string ends in digits m will be a Match object, or None otherwise.
            if m is None:
                i = i + 1
                filepath = subdir + os.sep + file
                print (filepath)
                info = PTN.parse(file)
                params = {'api_key': '<api_key>', 'query': info['title'].replace(" Directors Cut", ""), 'year': info["year"]}
                print i, ' request: ', params['year'], params['query']
                resp = requests.get('https://api.themoviedb.org/3/search/movie', params=params)
                response = resp.json()
                print i, ' response: ', str(response['results'][0]['id']), response['results'][0]['original_title']
                new_filepath = filepath.replace('.mp4', "." + str(response['results'][0]['id']) + ".mp4")
                print new_filepath
                os.rename(filepath, new_filepath)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("arg", help="Required positional argument")

    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--flag", action="store_true", default=False)

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-n", "--name", action="store", dest="name")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)