#Q 1- What is List? How will you reverse a list?
# A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
#  Each element or value that is inside of a list is called an item.
#   lists are defined by having values between square brackets [ ] .

# in python list can be reversed by .reverse() methods
# __________________________________________________________________________

# Q 2- How will you remove last object from a list?
# list pop() is an inbuilt function in Python that removes and returns the last value from the List or the given index value.

# ______________________________________________________________________________
# Q-3 Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?
# lst=[2, 33, 222, 14, 25]
# print(lst[-1])
# ________________________________________________________________________________________

# Q-4  Differentiate between append () and extend () methods?

# append() adds a single element to the end of the list. 
# extend() can add multiple individual elements to the end of the list.
# ________________________________________________________________________________________
# Q-5 Write a Python function to get the largest number, smallest num and sum of all from a list.
# lst=[5,33,295,74,7788]
# print("largest number = ",max(lst))
# print("smallest number =",min(lst))
# print("sum = ",sum(lst))
# __________________________________________________________________________
# Q-6 How will you compare two lists?
# lst1=[1, 2, 3, 4]
# lst2=[4, 5, 6, 7]
# if lst1 == lst2:
#     print("both list are same")
# else:
#     print("both list are different")
# # __________________________________________________________________________
# Q-7 Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given
# list of strings.
# string = ['abc', 'xyz', 'aba', '1221', 'mnm', '787']
# count = 0

# for word in string:
#     if len(word) > 1 and word[0] == word[-1]:
#       count += 1
# print(f"Number of string where the first and last character are same: {count}")
# __________________________________________________________________________
# Q-8 Write a Python program to remove duplicates from a list.
# lst=[1,2,3,4,1,3,6,5,4,7,2]
# dup_lst=[]
# for i in lst:
    # if i not in dup_lst:
        # dup_lst.append(i)
# lst=dup_lst
# print(f"after removing duplicate from list : {lst}")
# __________________________________________________________________________
# Q-9 Write a Python program to check a list is empty or not.
# lst=[1,2,3]
# if not lst:
    # print("list is empty")
# else:
    # print("list is not empty")
# __________________________________________________________________________
# Q-10 Write a Python function that takes two lists and returns true if they have at least one common member.
# lst1=[1,2,3,4,5]
# lst2=[5,56,7,8,9]
# for i in lst1:
#     for x in lst2:
#         if i==x:
#             print("True")
#         else:
#             print("False")
#  __________________________________________________________________________
# Q-11 Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.
# lst = list()
# for i in range(1,30):
# 		lst.append(i**2)
# print(f"({lst[:5]} {lst[-5:]})")
# __________________________________________________________________________
# Q-12 Write a Python function that takes a list and returns a new list with unique elements of the first list.
# lst = [1,2,2,3,3,3,4,4,5]
# lst1 = []

# for i in lst:
#     if i not in lst1:
#         lst1.append(i)
# print(f"Unique list: {lst1}")
# __________________________________________________________________________
# Q-13 Write a Python program to convert a list of characters into a string.
# lst=['a','a','n','a','l']
# str=''.join(lst)
# print(str)
# __________________________________________________________________________
# Q-14 Write a Python program to select an item randomly from a list.
# import random

# color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
# print(f"Random color: {random.choice(color_list)}")
# __________________________________________________________________________
# Q-15 Write a Python program to find the second smallest number in a list.
# list_of_numbers = [2, 1, 9, 8, 6, 3, 1, 0, 4, 5]
# temp_lst = list_of_numbers.copy()
# temp_lst.sort()
# print("SecondSmallest:",(temp_lst[1]))
# __________________________________________________________________________
# Q-16 Write a Python program to get unique values from a list
# lst=[1,2,4,3,2,1,4,5]
# unique_lst=[]
# for i in lst:
#     if i not in unique_lst:
#         unique_lst.append(i)
# print("unique list=",unique_lst)
# __________________________________________________________________________
# Q-17 Write a Python program to check whether a list contains a sub list
# __________________________________________________________________________
# Q-18 Write a Python program to split a list into different variables.
# __________________________________________________________________________
# Q-19 What is tuple? Difference between list and tuple.
# A tuple is a collection which is ordered and unchangeable.

# > Lists
# 1) Lists are mutable.
# 2) Implication of iterations is Time-consuming
# 3) The list is better for performing operations, such as insertion and deletion.
# 4) Lists consume more memory
# 5) Lists have several built-in methods

# > Tuple
# 1) Tuples are immutable
# 2) The implication of iterations is comparatively Faster
# 3) Tuple data type is appropriate for accessing the elements
# 4) Tuple consume less memory as compared to the list
# 5) Tuple does not have many built-in methods.
# __________________________________________________________________________
# Q-20 Write a Python program to create a tuple with different data types.
# tpl=("aanal",123,45.77,True)
# print(tpl)
# __________________________________________________________________________
# Q-21 Write a Python program to create a tuple with numbers.
# tpl=(1,2,3,4,5)
# print(tpl)
# __________________________________________________________________________
# Q-22 Write a Python program to convert a tuple to a string.
# tpl=('a','a','n','a','l')
# str=''.join(tpl)
# print(str)
# __________________________________________________________________________
# Q-23 Write a Python program to check whether an element exists within a tuple.
# tpl=('a','b',3,7)
# print('a' in tpl)
# print(4 in tpl)
# __________________________________________________________________________
# Q-24 Write a Python program to find the length of a tuple.
# tpl=(1,2,3,4,5)
# print(len(tpl))
# __________________________________________________________________________
# Q-25 ,Write a Python program to convert a list to a tuple.
# lst=['a','a','n','a','l']
# tpl=set(lst)
# print(tpl)
# __________________________________________________________________________
# Q-26 Write a Python program to reverse a tuple.
# tpl=('a','a','n','a','l')
# result=reversed(tpl)
# result=tuple(result)
# print(result)
# __________________________________________________________________________
# Q-27 Write a Python program to replace last value of tuples in a list.
# l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# print([t[:-1] + (100,) for t in l])
# __________________________________________________________________________

# Q-28 Write a Python program to find the repeated items of a tuple.
# Q-29 Write a Python program to remove an empty tuple(s) from a list of tuples.
# Q-30 Write a Python program to unzip a list of tuples into individual lists.
# Q-31 Write a Python program to convert a list of tuples into a dictionary.
# Q-32 How will you create a dictionary using tuples in python?
# Q-33 Write a Python script to sort (ascending and descending) a dictionary by value.
# Q-34 Write a Python script to concatenate following dictionaries to create a new one.
# Q-35 Write a Python script to check if a given key already exists in a dictionary.
# Q-36 How Do You Traverse Through A Dictionary Object In Python?
# Q-37 How Do You Check The Presence Of A Key In A Dictionary?
# Q-38 Write a Python script to print a dictionary where the keys are numbers between 1 and 15.
# Q-39 Write a Python program to check multiple keys exists in a dictionary
# Q-40 Write a Python script to merge two Python dictionaries
# Q-41 Write a Python program to map two lists into a dictionary
# Q-42 Write a Python program to combine two dictionary adding values for common keys.
#     d1 = {'a': 100, 'b': 200, 'c':300}
#      d2 = {'a': 300, 'b': 200,’d’:400}
#      Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).
# Q-43 Write a Python program to print all unique values in a dictionary.
# Q-44 Why Do You Use the Zip () Method in Python?
# Q-45 Write a Python program to create and display all combinations of letters,selecting each letter from a different key in a dictionary.
#      Sample data: {'1': ['a','b'], '2': ['c','d']}
#        Expected Output: ac ad bc bd
# Q-46 Write a Python program to find the highest 3 values in a dictionary
# Q-47 Write a Python program to combine values in python list of dictionaries.
#       Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
#        Expected Output: Counter ({'item1': 1150, 'item2': 300})
# Q-48 Write a Python program to create a dictionary from a string.
#    Note: Track the count of the letters from the string. Sample string: 'w3resource'
#    Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
# Q-49 Write a Python function to calculate the factorial of a number (a nonnegative integer)
# Q-50 Write a Python function to check whether a number is in a given range
# Q-51 Write a Python function to check whether a number is perfect or not.
# Q-52 Write a Python function that checks whether a passed string is palindrome or not
# Q-53 How do you perform pattern matching in Python? Explain
# Q-54 What is lambda function in python? What we call a function which is incomplete version of a function?
# Q-55 How Many Basic Types Of Functions Are Available In Python?
# Q-56 How can you pick a random item from a list or tuple?
# Q-57 How can you pick a random item from a range?
# Q-58 How can you get a random number in python?
# Q-59 How will you set the starting value in generating random numbers?
# Q-60 How will you randomizes the items of a list in place?
# Q-61 Write a Python program to read a random line from a file.
# Q-62 Write a Python program to convert degree to radian
# Q-63 Write a Python program to calculate the area of a trapezoid
# Q-64 Write a Python program to calculate the area of a parallelogram
# Q-65 Write a Python program to calculate surface volume and area of a cylinder
# Q-66 Write a Python program to returns sum of all divisors of a number
# Q-67 Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.