#!/usr/bin/env python

"""This program can monitor the number of transaction files that a
   Unicorn process has open for access. The transaction files are of the form
   `data/*.yaml`. This program accepts `--warning` and
   `--critical` thresholds for the number of open transaction files.

Usage example:
    python check_beelzebub_open_files.py --warning 10 --critical 20
"""

import os
import sys
import argparse
import fnmatch

def main():
    parser = argparse.ArgumentParser(
        description='monitors the number of transaction files open for access by a Unicorn process')
    parser.add_argument('--warning',
                        help='warning threshold for the number of open transaction files',
                        required=True,
                        type=int,
                        default=10,
                        dest='threshold_warning')
    parser.add_argument('--critical',
                        help='critical threshold for the number of open transaction files',
                        required=True,
                        type=int,
                        default=20,
                        dest='threshold_critical')
    parser.add_argument('--verbose',
                        help='increase verbosity',
                        required=False, 
                        dest='verbose')
    parser.add_argument('--dirpath',
                        help='full path of transaction file directory that the Unicorn process has open for access',
                        required=False,
                        default='/opt/beelzebub/data/',
                        dest='open_files_dirpath')
    parser.add_argument('--pattern',
                        help='pattern string to match the name of the transaction file(s)',
                        required=False,
                        default='*.yaml',
                        dest='open_files_pattern')
    args = parser.parse_args()

    NAG_OK = 0
    NAG_WARN = 1
    NAG_CRIT = 2
    NAG_UNKNWN = 3

    exit_code = NAG_OK

    try:
        # Check /data/*.yaml (most recent time period) rather than /proc/$PID/
        # TODO need to determine correct number of transaction files currently open by beezlebub processes
        # Alternatively use system commands like `lsof` to query open files
        open_files_count = len(fnmatch.filter(os.listdir(args.open_files_dirpath), args.open_files_pattern))

        if args.verbose:
            if open_files_count >= args.threshold_critical:
                print 'Number of files open CRITICAL'
                exit_code = NAG_CRIT
            elif open_files_count >= args.threshold_warning:
                print 'Number of files open WARNING'
                exit_code = NAG_WARN
            else:
                print 'Number of files open OK'
                exit_code = NAG_OK

            print 'Path to open transaction file(s) : {0}'.format(args.open_files_dirpath)
            print 'Filename pattern of open transaction file(s) : {0}'.format(args.open_files_pattern)
            print 'Number of transaction file(s) open: {0}'.format(open_files_count)

            sys.exit(exit_code)

        else:
            if open_files_count >= args.threshold_critical:
                print 'Number of files open CRITICAL'
                exit_code = NAG_CRIT
            elif open_files_count >= args.threshold_warning:
                print 'Number of files open WARNING'
                exit_code = NAG_WARN
            else:
                print 'Number of files open OK'
                exit_code = NAG_OK

            sys.exit(exit_code)

    except Exception, ex:
        if args.verbose:
            print 'CRITICAL: Could not get information on transaction files.\r\nError: {0}'.format(ex)
        else:
            print 'CRITICAL: Could not get information on transaction files'

        sys.exit(NAG_CRIT)

if __name__ == "__main__":
    main()
