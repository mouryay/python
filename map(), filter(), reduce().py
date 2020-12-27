""" Problems:
Use only map, filter and reduce. No Loops!
Write a function that:
1. Takes an list with numbers and squares all the numbers and multiplies all the squares. 
2. Takes an list of strings and keeps strings that have vowels 'a' and 'i' in them and removes all others as a new list.
3. Takes an list of lists like this -> [ [3,46,7,8], [4,6,8,10], [6,7,8,8], [24,6]]
    and returns only the list that has even numbers in it.
    so return value will be -> [[4,6,8,10], [24,6]]
4. Takes an list of dictionaries with each dictionary containing a key called 'name' and returns an list with those names.
Example: Input ->  [ {name: "john"},{name: "bob"},{name: "mary"},{name: "doe"}]
         Output -> ["john", "bob", "mary", "doe"]
5. Takes an list of numbers and returns true if all the numbers in the list are even , otherwise returns false. Remember no Loops!
Collapse
"""

#Solutions:

#1
from functools import reduce
def product_of_squares(l1):
    out = reduce(lambda x, y : x * y, list(map(lambda x : x ** 2, l1)))
    print(out)

#2
def a_i(a1):
    b1 = filter(lambda x: 'a' not in x or 'i' not in x, a1)
    print(list(b1))

#3
def even_lists_only(a1):
    def even_or_not(b1):
        if(reduce(lambda x, y: x * y, list(map(lambda x : 1 if x % 2 == 0 else 0, b1)))):
            return(True)
        else:
            return(False)
    a2 = filter(even_or_not, a1)
    print(list(a2))

#4
def values_from_dict(a):
    return(list(map(lambda x : x["name"], a)))

#5    
def even_or_not(a):
    if(reduce(lambda x, y: x * y, list(map(lambda x : 1 if x % 2 == 0 else 0, a)))):
        print(True)
    else:
        print(False)
