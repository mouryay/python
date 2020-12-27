"""
3.	Get user input and find all the numbers divisible by 3 but not a multiple of 5 
between the range of two numbers given by the user. All the outputs should be comma separated in one line 
"""

start = int(input("Enter a starting number: "))
end = int(input("Enter an Ending number: ")) + 1
#Numbers divisible by 3 but not by 5.
counter = 0
for i in range(start, end):
    if (i % 3 == 0) and (i % 5 != 0):
        if counter > 0:
            print(f", {i}", end = '')
        else:
            print(i, end = '')
        counter = counter + 1