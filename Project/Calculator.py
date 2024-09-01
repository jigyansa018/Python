first = input("Enter first number: ")
operator = input("Enter operator (+, -, *, /, %): ")
second = input("Enter second number: ")

# Convert inputs to integers
first = int(first)
second = int(second)

# Check the operator and perform the corresponding operation
if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid Operation!!")
