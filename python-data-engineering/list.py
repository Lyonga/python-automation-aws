# Print out elements higher than or equal 10
my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
for number in my_list:
    if number >= 10:
        print(number)

# Make a new list with all elements higher than or equal 10 and print it out
my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
my_new_list = []
for number in my_list:
    if number >= 10:
        my_new_list.append(number)
print(my_new_list)

# User input as a number and print a list that contains only those elements from my_list that are higher than the number given by the user.
user_input = input("Enter a number: ")
my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
my_new_list = []
for number in my_list:
    if number > int(user_input):
        my_new_list.append(number)
print(my_new_list)

