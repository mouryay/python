"""
1.	simulate a club ticketing machine, where the person trying to buy the ticket has been authorized 
according to the following conditions, people with the age younger to 21 are not allowed, people with 
age between 21 and 50 are authorized and are under newbies category and people with age beyond 50 are 
not permitted.
"""

age = int(input("Enter your age: "))
if age < 21:
    print("You are too young")
elif age >= 21 and age <= 50:
    print("You are in")
else:
    print("You are too old")