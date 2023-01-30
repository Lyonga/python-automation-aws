# Write a function that accepts a list of dictionaries with employee age and prints out the name and age of the youngest employee
employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

def print_employee_info(employees):
    youngest_employee_age = employees[0]["age"]
    youngest_employee_name = employees[0]["name"]
    for employee in employees:
        if employee["age"] < youngest_employee_age:
            youngest_employee_age = employee["age"]
            youngest_employee_name = employee["name"]

    print(f"name of the youngest employee: {youngest_employee_name}")
    print(f"age of the youngest employee: {youngest_employee_age}")

print_employee_info(employees)

# Write a function that accepts a string and calculates the number of upper case letters and lower case letters
def count_upper_and_lower_letters(string):
    lower_letters = 0
    upper_letters = 0
    for char in list(string):
        if char.islower():
            lower_letters += 1
        elif char.isupper():
            upper_letters += 1
    print(f"number of lower case letters: ", lower_letters)
    print(f"number of upper case letters: ", upper_letters)

count_upper_and_lower_letters("sWWbb137WATbfgdbWb")

# Write a function that prints the even numbers from a provided list
def print_even_numbers(numbers_list):
    for number in numbers_list:
        if number % 2 == 0:
            print(number)

print_even_numbers([0, 3, 9, 10, 2, 13, 120])





#Function in helper module
#For cleaner code, declare these functions in its own helper Module and use them in the main.py file helper.py

def print_employee_info(employees):
    youngest_employee_age = employees[0]["age"]
    youngest_employee_name = employees[0]["name"]
    for employee in employees:
        if employee["age"] < youngest_employee_age:
            youngest_employee_age = employee["age"]
            youngest_employee_name = employee["name"]

    print(f"name of the youngest employee: {youngest_employee_name}")
    print(f"age of the youngest employee: {youngest_employee_age}")

def count_upper_and_lower_letters(string):
    lower_letters = 0
    upper_letters = 0
    for char in list(string):
        if char.islower():
            lower_letters += 1
        elif char.isupper():
            upper_letters += 1
    print(f"number of lower case letters: ", lower_letters)
    print(f"number of upper case letters: ", upper_letters)

def print_even_numbers(numbers_list):
    for number in numbers_list:
        if number % 2 == 0:
            print(number)





from helper import print_employee_info, count_upper_and_lower_letters, print_even_numbers

employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

print_employee_info(employees)

count_upper_and_lower_letters("sWWbb137WATbfgdbWb")

print_even_numbers([0, 3, 9, 10, 2, 13, 120])



