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
status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
# \b\w+\b for hostname instead of IP e.g rashisky
regex1 = r'\b\w+\b|((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.)'
regex2 = r'{3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\-?\s?'
ip_addr_pattern = regex1 + regex2
hyphen_pattern = re.compile(r'\s?-\s?(?=\[)')
date_pattern = re.compile(r'(?<=\s-\s)(\[.*\])|(?<=-)(\[.*\])')
method_pattern = re.compile(r'(?<=\]\s)"GET /projects/260 HTTP/1.1"')
size_pattern = re.compile(r'\d+$')
code = re.compile(r'(?<="GET \/projects\/260 HTTP\/1.1"\s)\d{3}(?!$)')


def validate_line(line):
    """validate the lines from stdin"""
    ip_address = validate_ip_address(line)
    hyphen = validate_hyphen(line)
    date = validate_date(line)
    response_header = validate_resp_method(line)
    status_code = validate_status_code(line)
    file_size = validate_file_size(line)
    # print("---------------------------------")
    # print([ip_address, hyphen, date, response_header,
    #             status_code, file_size])
    # print("---------------------------------")
    if status_codes:
        return [ip_address, hyphen, date, response_header,
                status_code, file_size]
    return [ip_address, hyphen, date, response_header, file_size]


def validate_date(arg):
    """validate the timestamp"""
    timestamp = date_pattern.search(arg)
    if timestamp:
        try:
            timestamp = timestamp.group().strip('[]')
            datetime.fromisoformat(timestamp)
            return True
        except Exception:
            return False
    return False


def validate_ip_address(address):
    """validate IP address"""
    pattern = re.compile(r'{}'.format(ip_addr_pattern))

    return True if pattern.match(address) else None


def validate_resp_method(resp_method):
    """validate response header"""

    return True if method_pattern.search(resp_method) else False


def validate_file_size(file_size):
    """validate file size"""
    size = size_pattern.search(file_size)

    return int(size.group()) if size else False


def validate_status_code(status_code):
    """validate status code"""
    status = code.search(status_code)
    if status and status.group() in status_codes:
        return status.group()
    return 'Unknown'


def validate_hyphen(hyphen):
    """validate the hyphen"""

    return True if hyphen_pattern.search(hyphen) else False


def update_key(status_number):
    """Update the <status>: <number> and prints them"""
    global size
    global dict_size_count

    for status, file_size in status_number:
        size += file_size
        if status != 'Unknown':
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

# Left over files when list_size_count is less than 10
if len(list_size_count) < 10:
    update_key(list_size_count)
