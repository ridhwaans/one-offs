#!/usr/bin/env python3
"""
foobar
"""
__version__ = "0.1.0"

import argparse
import urllib2, urllib
import sys

def main(args):
    # entry point
    print("hello world")
    print(sys.argv[1])
    x = urllib.request.urlopen(args[1])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("url", help="Input url")

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)