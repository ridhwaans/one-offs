### Introduction
check_beelzebub_open_files.py - monitors the number of transaction files that the Unicorn process has open for access  
check_beelzebub_tx_response_time.py - monitors the transaction response time for a given time period  

Usage examples:  
`python check_beelzebub_open_files.py --warning 10 --critical 20`  
`python check_beelzebub_tx_response_time.py --time-period 300 --warning 2 --critical 3`  

### Instructions
  1) Setup Vagrant and start the Vagrant test environment using the provided Vagrantfile  
  2) Start Beelzebub and the requester in the virtual machine  
  3) `cd` to the directory containing the monitoring programs  
  4) Run `python check_beelzebub_open_files.py` or `python check_beelzebub_tx_response_time.py` with provided arguments  
  
#### Assumptions
  1) Default path is `/opt/beelzebub/` in the provided Vagrantfile  
  2) Assume the requester that simulates requests is run on demand and is not scheduled on a cron  
  3) Requires data driven test cases at the integration level (i.e. mock/read `/data/*.yaml` and syslog)  
  4) Assume the transaction files are located in `/opt/beelzebub/data/*.yaml` and not in `/proc/$PID/fd/*`  
  5) The `check_beelzebub_tx_response_time.py` program has to be run as `sudo su root` to get syslog read permission  

#### Choice of programming language
Python because it is simple and easy for scripting
