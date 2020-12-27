""" Problems:
1.	Define a function that can convert an integer into a string and print it in console.
2.	Define a function that can convert an integer into a string and print it in console.
3.	Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
4.	Define a function that can accept two strings as input and concatenate them and then print it in console.
5.	Define a function that can accept two strings as input and print the string with maximum length in console. If two string have the same length, then the function should print both the string line by line.
6.	Define a function that can accept an integer number as input and print the “It is an even number” if the number is even, otherwise print “It is an odd number”.
7.	Define function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
8.	Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should print the values only. Hint: Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
9.	Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.
10.	Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
11.	Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list. Hint: Use list.append() to add values into a list. Use [n1:n2] to slice a list (read how to slice, its simple)
12.	Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (both included).
13.	With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. Hint: Use [n1:n2] notation to get a slice from a tuple.
14.	Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
15.	Write a program which can filter even numbers in a list by using function. The list is [1,2,3,4,5,6,7,8,9,10]. Hint: Use filter() to filter some elements in a list. Use lambda to define anonymous function.
16.	Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]. Hint: Use map() to generate a list. Use lambda to define anonymous functions.
17.	Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
18.	Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
19.	Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
"""

#1
def print_int_as_str(a):
    b = str(a)
    print(b)

#2
def print_str_as_int(a):
    b = int(a)
    print(b)

#3
def sum(a, b):
    sum = int(a) + int(b)
    print(sum)

#4
def str_concat(a, b):
    print (a + b)

#5
def longer_str(a, b):
    if len(a) > len(b):
        print(a)
    elif len(a) < len(b):
        print(b)
    else:
        print(a)
        print(b)

#6
def even_odd(a):
    if a % 2 == 0:
        print("It is an even number.")
    else:
        print("It is an odd number.")

#7
def dict_of_squares(a, b):
    d = {}
    for i in range(a, b + 1):
        d.update({i : i ** 2})
        print(d)

#8
def dict_of_squares_valuesonly(a, b):
    d = {}
    for i in range(a, b + 1):
        d.update({i : i ** 2})
    for x in d.values():
        print(x)

#9
def dict_of_squares_keysonly(a, b):
    d = {}
    for i in range(a, b + 1):
        d.update({i : i ** 2})
    for x in d.keys():
        print(x)

#10
def list_of_squares(a, b):
    list = []
    for i in range(a, b + 1):
        list.append(i ** 2)
    print(list)

#11
def list_of_squares_5(a, b):
    list = []
    for i in range(a, b + 1):
        list.append(i ** 2)
    print(list[0 : 5])

#12
def list_of_squares_t(a, b):
    list = []
    for i in range(a, b + 1):
        list.append(i ** 2)
    print(tuple(list))

#13
def print_in_twolines(a):
    half_length = int(len(a)/2)
    print(half_length)
    print(a[:half_length])
    print(a[half_length:])

#14
def even_from_tuple(a):
    list = []
    for i in a:
        if i % 2 == 0:
            list.append(i)
    print(tuple(list))

#15
def filter_even_from_list(a):
    b = filter(lambda x: x % 2 == 0, a)
    print(list(b))

#16
def map_squares(a):
    b = map(lambda x : x ** 2, a)
    print(list(b))

#17
def squares_of_even(a):
    b = map(lambda x : x ** 2, list(filter(lambda y : y % 2 == 0, a)))
    print(list(b))

#18
def filter_even(a):
    b = list(filter(lambda x: x % 2 == 0, a))
    print(b)

#19
def map_squares(a):
    b = map(lambda x : x ** 2, a)
    print(list(b))
