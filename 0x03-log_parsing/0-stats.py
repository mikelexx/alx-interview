#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>]
"GET /projects/260 HTTP/1.1" <status code> <file size>
(if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all
previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer,
don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
Warning: In this sample, you will have random value -
it’s normal to not have the same output
"""

import sys

if __name__ == '__main__':

    def print_lines(file_size: int, code_dict: dict) -> None:
        """
        prints the statistics of the lines read so far
        """
        print("File size: {:d}".format(file_size))
        for k, v in sorted(code_dict.items()):
            if v:
                print("{}: {}".format(k, v))

    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    size, count = 0, 0
    code_dict = {k: 0 for k in codes}

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                code = data[-2]
                if code in code_dict:
                    code_dict[code] += 1
            except BaseException:
                pass
            try:
                size += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_lines(size, code_dict)
        print_lines(size, code_dict)
    except KeyboardInterrupt:
        print_lines(size, code_dict)
        raise
