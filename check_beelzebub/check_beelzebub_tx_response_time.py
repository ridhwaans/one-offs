#!/usr/bin/env python

"""This program can monitor the transaction response time for a given
   time period. If the average transaction response time exceeds a given
   threshold over that time period, the program will alert. This program
   accepts `--warning` and `--critical` threshold arguments for the
   average response time in seconds, and a `--time-period` argument that
   specifies the time window to analyze in seconds. The program has to be
   run as sudo su root in order to get syslog read permission.

Usage example:
    python check_beelzebub_tx_response_time.py --time-period 300 --warning 2 --critical 3
"""

import os
import re
import sys
import time
import datetime
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='script that runs and monitors the number of transaction files that the Unicorn process has open for access.')
    parser.add_argument('--warning',
                        help='warning threshold for transaction average response time in seconds',
                        required=True,
                        type=int,
                        default=2,
                        dest='threshold_warning')
    parser.add_argument('--critical',
                        help='critical threshold for transaction average response time in seconds',
                        required=True,
                        type=int,
                        default=3,
                        dest='threshold_critical')
    parser.add_argument('--time-period',
                        help='time window to analyze transaction response time in seconds',
                        required=True,
                        type=int,
                        default=300,
                        dest='time_period')
    parser.add_argument('--logfile',
                        help='full path to the log containing transaction start times and completion times',
                        required=False,
                        default='/var/log/syslog',
                        dest='log_file')
    args = parser.parse_args()

    NAG_OK = 0
    NAG_WARN = 1
    NAG_CRIT = 2
    NAG_UNKNWN = 3

    exit_code = NAG_OK

    i = 0
    completed_requests = {}
    response_time_total = 0
    total_requests = 0
    first_timestamp = 0

    try:
        for line in readlines_reverse(args.log_file):
            # use regex to parse the log line delimited by spaces
            match = re.findall(r"^([a-zA-Z]{3}\s[0-9]{2}\s([0-9]{2}(\:|))+).*\s([0-9]+)\s(started|completed)$", line)

            if len(match) > 0:
                status = match[0][4]
                # use arbitrary year
                date_time = "2017 " + match[0][0]
                request_id = match[0][3]
                # process timestamp from datetime
                timestamp = datetime.datetime.strptime(date_time, "%Y %b %d %H:%M:%S").timetuple()

                # skip request if transaction response time exceeds time period
                if first_timestamp > 0:
                    timedelta = int(time.mktime(first_timestamp)) - int(time.mktime(timestamp))
                    if timedelta > args.time_period:
                        break

                # getting only first timestamp
                if i == 0:
                    first_timestamp = timestamp
                    i = 1

                if status == "completed":
                    # add request id and timestamp to the dictionary
                    completed_requests[request_id] = int(time.mktime(timestamp))

                elif status == "started":
                    # see if request id is already in dictionary
                    if request_id in completed_requests:
                        response_time_total += completed_requests[request_id] - int(time.mktime(timestamp))
                        # lets now remove this key
                        del completed_requests[request_id]
                        # and increment total requests number
                        total_requests += 1

        average_response_time = response_time_total/total_requests

        if average_response_time >= args.threshold_critical:
            print 'Average response time CRITICAL: {0} s'.format(average_response_time)
            exit_code = NAG_CRIT
        elif average_response_time >= args.threshold_warning:
            print 'Average response time WARNING: {0} s'.format(average_response_time)
            exit_code = NAG_WARN
        elif average_response_time == 0:
            print 'Average response time UNKNOWN: {0} s'.format(average_response_time)
            exit_code = NAG_UNKNWN
        else:
            print 'Average response time OK: {0} s'.format(average_response_time)
            exit_code = NAG_OK

        sys.exit(exit_code)

    except Exception, ex:
        print 'CRITICAL: Could not get information on transaction response time(s).\r\nError: {0}'.format(ex)
        sys.exit(NAG_CRIT)


def readlines_reverse(filename):
    """Reads file from the end to the top
    :param filename: file to read
    :return: list
    """
    with open(filename) as qfile:
        qfile.seek(0, os.SEEK_END)
        position = qfile.tell()
        line = ''
        while position >= 0:
            qfile.seek(position)
            next_char = qfile.read(1)
            if next_char == "\n":
                yield line[::-1]
                line = ''
            else:
                line += next_char
            position -= 1
        yield line[::-1]


if __name__ == "__main__":
    main()
