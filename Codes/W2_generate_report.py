#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
    raw_file = open(csv_file_location, "r")

    csv.register_dialect("empDialect", skipinitialspace = True, strict = True)
    employee_file = csv.DictReader(raw_file, dialect = "empDialect")

    employee_list = []
    for data in employee_file:
        employee_list.append(data)

    return employee_list

employee_list = read_employees("/home/student-01-cead9c8fe350/data/employees.csv")
#print(employee_list)

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data["Department"])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

dictionary = process_data(employee_list)
#print(dictionary)

def write_report(dictionary, report_file):
    with open (report_file, "w") as f:
        for k in sorted(dictionary):
            f.write(str(k)+":"+str(dictionary[k])+"\n")
    f.close()

write_report(dictionary,"/home/student-01-cead9c8fe350/test_report.txt")

