def calculator(number1, number2, operation):
    # from Python verson 3.10, you can use match-case
    if operation == "plus":
        print(number1 + number2)
    elif operation == "minus":
        print(number1 - number2)
    elif operation == "multiply":
        print(number1 * number2)
    elif operation == "divide":
        print(number1 / number2)
    

number_of_calculations_done = 0 
while True:
    number1 = input("Enter the first number: ")

    if number1 == "exit":
        print("exiting the program")
        print(f"you did {number_of_calculations_done} calculations")
        break

    number2 = input("Enter the second number: ")
    operation = input("What operation do you want to perform on these numbers (plus, minus, multiply, divide): ")

    valid_numbers = number1.isnumeric() and number2.isnumeric()
    valid_operation = operation == "plus" or operation == "minus" or operation == "multiply" or operation == "divide"
    if not valid_numbers:
        print("only numbers allowed") 
    elif not valid_operation:
        print("operation not supported")
    else:
        calculator(int(number1), int(number2), operation)
        number_of_calculations_done += 1

