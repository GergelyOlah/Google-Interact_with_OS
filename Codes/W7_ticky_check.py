#!/usr/bin/env python3

import re
import sys

#with open (sys.argv[1], r) as logfile:
with open ("W7_logfile.txt", "r") as logfile:
    errors = {}
    users = {}
    for line in logfile.readlines():
        error = re.search(r"ERROR: ([\w ]*) .* \((\w*)\)", line)
        info = re.search(r"INFO: ([\w ]*) .* \((\w*)\)", line)
        print(error)
        print(error[1])
        print(error[2])
        if info:
            if info[2] not in users:
                users[info[2]] = []
            users[info[2]][0] += users.get(info[2][0], 0)
        elif error:
            if error[2] not in users:
                users[error[2]] = []
          #  errors[error[1]] += errors.get(error[1], 0)
            users[error[2]][1] += users.get(error[2][1], 0)
        else:
            continue

    errors_sorted = sorted(errors, key = lambda x: x[1])
    users_sorted = sorted(users, key = lambda x: x[0])
    logfile.close()

with open("error_message.csv", "w") as error_file:
    for line in errors_sorted:
        error_file.write(line)
    error_file.close()

with open("user_statistics", "w") as user_file:
    for line in users_sorted:
        user_file.write(line)
    user_file.close()
