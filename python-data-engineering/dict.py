# Update the job to Software Engineer
employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

employee["job"] = "Software Engineer"
print(employee)

# Remove the age key from the dictionary
employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

employee.pop("age")
print(employee)

# Loop through the dictionary and print the key:value pairs one by one
employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

for key, value in employee.items():
  print(f"{key}:{value}")





#Working with Multiple Dictionarires
# Merge these two Python dictionaries into 1 new dictionary
dict_one = {'a': 100, 'b': 400} 
dict_two = {'x': 300, 'y': 200}

dict_merged = dict_one.copy()
dict_merged.update(dict_two) 
print(dict_merged)

# Sum up all the values in the new dictionary and print it out
dict_one = {'a': 100, 'b': 400} 
dict_two = {'x': 300, 'y': 200}

dict_merged = dict_one.copy()
dict_merged.update(dict_two) 

sum_of_values = 0
for value in dict_merged.values():
    sum_of_values = sum_of_values + value
print(sum_of_values)

# Print the max and minimum values of the dictionary
dict_one = {'a': 100, 'b': 400} 
dict_two = {'x': 300, 'y': 200}

dict_merged = dict_one.copy()
dict_merged.update(dict_two)

merged_values = []
for value in dict_merged.values():
    merged_values.append(value)

merged_values.sort()
print(f"min value: {merged_values[0]}")
print(f"max value: {merged_values[len(merged_values)-1]}")



