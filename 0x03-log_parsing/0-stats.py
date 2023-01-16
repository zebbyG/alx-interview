#!/usr/bin/python3

import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

for line in sys.stdin:
    try:
        """Extract information from the line"""
        ip_address, date, request, status_code, file_size = line.strip().split(" ")
        status_code = int(status_code)
        file_size = int(file_size)

        """Update statistics"""
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        """Print statistics every 10 lines or on keyboard interruption"""
        if line_count % 10 == 0 or line_count == 1:
            print("Total file size: File size:", total_size)
            for status_code in sorted(status_codes.keys()):
                if status_codes[status_code] > 0:
                    print("{}: {}".format(status_code, status_codes[status_code]))
    except ValueError:
        """Skip line if it doesn't match the input format"""
        pass
