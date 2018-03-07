### Introduction

This archive contains a program that monitors the number of transaction 
files open (check_beelzebub_open_files.py) and a program that monitors 
the transaction response time for a given time period 
(check_beelzebub_tx_response_time.py). 

Usage examples:
`python check_beelzebub_open_files.py --warning 10 --critical 20`
`python check_beelzebub_tx_response_time.py --time-period 300 --warning 2 --critical 3`

### Instructions
 Get the latest version of Python 2 (not 3), which can be downloaded from 
 https://www.python.org/downloads/
  1a) On Mac OS
  -> brew install python
  -> brew install pip
  1b) On Vagrant (Debian Linux)
  -> sudo apt-get install python-dev build-essential
  -> sudo apt-get install python-pip
  2) cd to the root directory containing the monitoring programs (in Python)
  3) Run  `python check_beelzebub_open_files.py` or 
  `python check_beelzebub_tx_response_time.py` with the necessary arguments
  
#### Assumptions
  a. I assumed that the beelzebub Ruby application and the requester are 
  functional on the Vagrant environment
  b. I assumed that the base path for the beelzebub app is /opt/beelzebub/ in Vagrant
  c. I assumed that the requester runs on demand to simulate requests 
  and is not scheduled on a cron
  d. Writing automation to test the programs would require data driven test 
  cases at the integration level (i.e. mock/read /data/*.yaml and syslog)
  e. The check_beelzebub_tx_response_time.py program has to be run as sudo 
  su root in order to get syslog read permission
  f. For the check_beelzebub_open_files.py program, I assume that to check 
  the number of transaction files the beelzebub processes has open for access 
  are in /opt/beelzebub/data/*.yaml, and not in /proc/$PID/fd/*

#### Choice of programming language
  I picked Python because I have some experience writing automation with it. 
  Python is very powerful for automation tasks like Nagios as it has a lot 
  of useful modules and packages to offer relative to Bash.
