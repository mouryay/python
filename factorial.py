"""
Get user input to find the factorial of the number, given by the user. The output should be on a single line.
"""

user_num = int(input("Enter a number: "))
if user_num < 0:
    print("Factorial of a negative number is not defined.")
elif user_num == 0:
    print("Factorial of 0 is 1.")
else:
    factorial = 1
    for i in range (1, user_num + 1):
        factorial = factorial * i
    print(f"Factorial of {user_num} is {factorial}")
