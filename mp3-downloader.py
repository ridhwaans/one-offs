#!/usr/bin/env python3
"""
foobar
"""

__author__ = "Ridhwaan Shakeel"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import urllib2, urllib
import sys

def main(args):
    """ Main entry point of the app """
    print("hello world")
    print(sys.argv[1])
    x = urllib.request.urlopen(args[1])

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("url", help="Input url")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)