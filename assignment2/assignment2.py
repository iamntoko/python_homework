import csv
import traceback
import sys
import os
import custom_module
from datetime import datetime


# Task 2: Read a CSV File

def read_employees():
    employee_dict = {}
    rows_list = []
    
    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            
            for index, row in enumerate(reader):
                if index == 0:
                    employee_dict["fields"] = row
                else:
                    rows_list.append(row)
                
            employee_dict["rows"] = rows_list
            return employee_dict
    except Exception as e:
        print("An exception occurred.")
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)
        
employees = read_employees()
print(employees)


# Task 3: Find the Column Index

def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")


# Task 4: Find the Employee First Name

def first_name(row_number):
    col_idx = column_index("first_name")
    return employees["rows"][row_number][col_idx]


# Task 5: Find the Employee: a Function in a Function

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches


# Task 6: Find the Employee with a Lambda

def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches


# Task 7: Sort the Rows by last_name Using a Lambda

def sort_by_last_name():
    employees["rows"].sort(key=lambda row: row[column_index("last_name")])
    return employees["rows"]

sort_by_last_name()
print(employees)


# Task 8: Create a dict for an Employee

def employee_dict(row):
    result = {}
    for index, field in enumerate(employees["fields"]):
        if field != "employee_id":
            result[field] = row[index]
    return result

print(employee_dict(employees["rows"][0]))


# Task 9: A dict of dicts, for All Employees

def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        emp_id = row[employee_id_column]
        result[emp_id] = employee_dict(row)
    return result

print(all_employees_dict())


# Task 10: Use the os Module

def get_this_value():
    return os.getenv("THISVALUE")


# Task 11: Creating Your Own Module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("abracadabra")
print(custom_module.secret)


# Task 12: Read minutes1.csv and minutes2.csv

def read_minutes_file(file_path):
    minutes_dict = {}
    rows_list = []
    
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    minutes_dict["fields"] = row
                else:
                    rows_list.append(tuple(row))
                    
            minutes_dict["rows"] = rows_list
            return minutes_dict
    except Exception as e:
        print("An exception occurred.")
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)
        
def read_minutes():
    m1 = read_minutes_file("../csv/minutes1.csv")
    m2 = read_minutes_file("../csv/minutes2.csv")
    return m1, m2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)


# Task 13: Create minutes_set

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)

minutes_set = create_minutes_set()
print(minutes_set)


# Task 14: Convert to datetime

def create_minutes_list():
    minutes_as_list = list(minutes_set)
    converted_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_as_list))
    return converted_list

minutes_list = create_minutes_list()
print(minutes_list)


# Task 15: Write Out Sorted List

def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    
    try:
        with open("./minutes.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            for row in converted_list:
                writer.writerow(row)
        return converted_list
    except Exception as e:
        print("An exception occurred.")
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)
        
print(write_sorted_list())