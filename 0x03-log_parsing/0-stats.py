#!/usr/bin/python3
"""Log parsing: Script that reads stdin line by line and compute metrics"""

import re
from datetime import datetime
import sys
import signal


# Global variables
size = 0
dict_size_count = {}
list_size_count = []


def validate_line(line):
    """validate the lines from stdin"""
    check_list = []
    split_line = re.split(r' (?=(?:[^"\[\]]*["\[\]][^"\[]*["\]])*[^"\[\]]*$)',
                          line)
    ip_address = validate_ip_address(split_line[0])
    dash = split_line[1] == '-'
    date = validate_date(split_line[2])
    response = split_line[3] == '"GET /projects/260 HTTP/1.1"'
    status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_code = split_line[4] if split_line[4] in status_codes else None
    file_size = validate_file_size(split_line[5])
    check_list.extend([ip_address, dash, date,
                       response, status_code, file_size])
    return check_list


def validate_date(timestamp):
    """validate the timestamp provided"""
    try:
        timestamp = timestamp.strip('[]')
        datetime.fromisoformat(timestamp)
        return True
    except Exception as e:
        return False


def validate_ip_address(address):
    """validate IP address"""
    pattern = re.compile(r'^((25[0-5]|\
        2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|\
            2[0-4]\d|1\d{2}|[1-9]?\d)$')
    return address if pattern.match(address) else None


def validate_file_size(size):
    """validate file size as number"""
    pattern = re.compile(r'^\d+$')
    return int(size) if pattern.match(size) else None


def update_key(status_number):
    """Update the <status>: <number> and prints them"""
    global size
    global dict_size_count

    for status, file_size in status_number:
        size += file_size
        dict_size_count[status] = dict_size_count.get(status, 0) + 1
    status_number.clear()
    print("File size:", size)
    for key, value in sorted(dict_size_count.items()):
        print(f"{key}: {value}")


def interrupt_handler(signum, frame):
    """Handles Signal from Ctrl + C"""
    update_key(list_size_count)
    # The below ensures that all buffered output is written to
    # the terminal before the script exits
    sys.stdout.flush()
    sys.exit(0)


signal.signal(signal.SIGINT, interrupt_handler)

for line in sys.stdin:
    result = validate_line(line.strip())
    if all(result):
        list_size_count.append((result[-2], result[-1]))
    if len(list_size_count) == 10:
        update_key(list_size_count)

# Make sure to update at the end if interrupted
# update_key(list_size_count)
