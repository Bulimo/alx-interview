# 0x03-log_parsing

## Requirements

    . Allowed editors: vi, vim, emacs
    . Environment: Ubuntu 20.04 LTS using python3 (version 3.4.3)
    . Files should end with a new line
    . The first line of all files should be exactly #!/usr/bin/python3
    . A README.md file, at the root of the folder of the project, is mandatory
    . Code should be documented
    . Code should use the PEP 8 style (version 1.7.x)
    . Files must be executable


## Task to solve

    Script that reads stdin line by line and computes metrics:
    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
        - Total file size: File size: <total size> (is the sum of all previous <file size>)
        - Number of lines by status code: [code: 200, 301, 400, 401, 403, 404, 405 and 500]
            - format: <status code>: <number>
            - status codes should be printed in ascending order

## Files in folder

    . 0-stats.py - contains solution to the task above

## Authors

	. Eric Bulimo Ubaga

