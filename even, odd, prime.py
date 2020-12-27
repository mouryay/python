"""
Ask user to input a number and print all the numbers from 1 till that number and then 
find all the even, odd and prime numbers separately.
"""
user_num = int(input("Enter a positive number greater than 1: "))
for i in range(1, user_num + 1):
    print(i)
#Printing Even Numbers
print("\nEven Numbers: ")
for i in range(1, user_num + 1):
    if i % 2 == 0:
        print(i)
#Printing Odd Numbers
print("\nOdd Numbers: ")
for i in range(1, user_num + 1):
    if i % 2 == 1:
        print(i)
#Printing Prime Numbers
print("\nPrime Numbers: ")
i = 2
j = 2
while i in range(2, user_num + 1):
    while j in range(2, i):
        if (i % j == 0):
            break
        else:
            j = j + 1;
    if i == j:
        print (i)
    i = i + 1
    j = 2



