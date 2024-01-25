#!/usr/bin/python3
""" Module 0-stats.py """


import sys
from collections import defaultdict
import re


def print_statistics(total_size, status_counts):
    """ Helper function that prints the statistics """
    print("File size: {}". format(total_size))
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")
    sys.stdout.flush()


def check_input(line):
    """checks if the line format is valid """
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
    r'\[([^\]]+)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
    match = re.match(pattern, line)
    if match:
        return True
    return False


def main():
    """ The main function runs the code """
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            # Split the line by spaces
            # print("line = {}".format(line))
            line.strip()
            if not check_input(line):
                continue
            parts = line.split(' ')
            # print("parts = {}".format(parts))
            # Check if the line has the expected format
            # if len(parts) == 9 and parts[0].count(".") == 3\
            #         and parts[4] == ("\"GET")\
            #         and parts[5] == '/projects/260'\
            #         and parts[6] == ("HTTP/1.1\"") and parts[7].isdigit()\
            #         and parts[8].isdigit():
            # Extract the status code and file size
            # print("Extracting the data")
            try:
                status_code = int(parts[7])
                file_size = int(parts[8])
                total_size += file_size
                if status_code not in status_counts:
                    status_counts[status_code] = 1
                else:
                    status_counts[status_code] += 1
            except Exception:
                pass

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
        print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
