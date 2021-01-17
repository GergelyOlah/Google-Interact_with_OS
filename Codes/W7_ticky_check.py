#!/usr/bin/env python3

import re
import sys
import csv

errors = {}
users = {}

#with open (sys.argv[1], r) as logfile:
with open ("W7_syslog.log", "r") as logfile:

    for line in logfile.readlines():
        error = re.search(r"ERROR ([\w' ]*) .* \((.*)\)", line)
        info = re.search(r"INFO .* \((.*)\)", line)

        if info:
            if info[1] not in users:
                users[info[1]] = [0, 0]
            users[info[1]][0] = users[info[1]][0] + 1

        elif error:
            if error[2] not in users:
                users[error[2]] = [0, 0]     
            users[error[2]][1] = users[error[2]][1] + 1
 
            errors[error[1]] = errors.get(error[1], 0) + 1
        else:
            continue

    errors_sorted = []
    for key, value in sorted(errors.items(), key = lambda x: x[1], reverse = True):
        errors_sorted.append([key, value])
    errors_sorted.insert(0, ["Error", "Count"])

    users_sorted = []
    for key, value in sorted(users.items(), key = lambda x: x[0]):
        users_sorted.append([key, users[key][0], users[key][1]])
    users_sorted.insert(0, ["Username", "INFO", "ERROR"])

    logfile.close()

with open("error_message.csv", "w") as error_file:
    writer_error = csv.writer(error_file)
    writer_error.writerows(errors_sorted)
    error_file.close()

with open("user_statistics.csv", "w") as user_file:
    writer_user = csv.writer(user_file)
    writer_user.writerows(users_sorted)
    user_file.close()
