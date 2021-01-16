#!/usr/bin/env python3

import re
import sys

with open (sys.argv[1], r) as logfile:
    errors = {}
    users = {}
    for line in logfile.readlines():
        error = re.search(r"ERROR ([\w]*) \((\w*)\(", line)
        info = re.search(r"INFO ([\w]*) \[.*\] \((\w*)\(", line)

        if info:
            if users[info[2]] not in users:
                users[info[2]] = []
            users[info[2]][0] += users.get(info[2][0], 0)
        elif error:
            if users[info[2]] not in users:
                users[info[2]] = []
            errors[error] += errors.get(error[1], 0)
            users[info[2]][1] += users.get(info[2][1], 0)
        else:
            continue

    errors.sort(key = lambda x: x[1])
    users.sort(key = lambda x: x[0])
    logfile.close()

with open("error_message.csv", "w") as error_file:
    for line in errors:
        error_file.write(line)
    error_file.close()

with open("user_statistics", "w") as user_file:
    for line in users:
        user_file.write(line)
    user_file.close()
