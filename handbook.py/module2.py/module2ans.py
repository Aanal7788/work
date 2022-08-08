#Q-1 Write a Python program to check if a number is positive, negative or zero.

# i=int(input("enter your number"))

# if i==0:
#     print(i,"the number is zero")
# elif i>0:
#     print(i,"this is positive number")
# else:
#     print(i,"this is negative number")
# ____________________________________________________________________________________




# Q-2 Write a Python program to get the Factorial number of given number.
# num=int(input("enter ur number for factorial"))
# factorial=1
# if num==0:
#     print("the factorial of 0 is 1")
# elif num<0:
#     print("factorial is not possible for negative number")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print(f"factorial of {num} is: {factorial}")
# ____________________________________________________________________________________________


# Q-3 Write a Python program to get the Fibonacci series of given range.

# n = int(input ("enter a num for fibonacci series:  "))  

# no1 = 0  
# no2 = 1  
# count = 0
  
  
# if n <= 0:  
#     print ("Please enter a positive integer, the given number is not valid")   
# elif n == 1:  
#     print ("The Fibonacci sequence of the numbers up to", n, ": ")  
#     print(no1)    
# else:  
#     print ("The fibonacci sequence of the numbers is: ")  
#     while count < n:  
#         print(f"{no1}")  
#         nth = no1 + no2     
#         no1 = no2  
#         no2 = nth  
#         count += 1
# ____________________________________________________________________________________________

          


# Q-4 how memory is managed in python?
# Python uses the dynamic memory allocation which is managed by the Heap data structure..
# ____________________________________________________________________________________________


# Q-5 What is the purpose continue statement in python?
# the continue statment gives you the option to skip over the part of a loop where an external condition is triggered,but to go on to complete the rest of the loop..
# ____________________________________________________________________________________________

# Q-6Write python program that swap two number with temp variable and without temp variable.

# without temp
# a,b=10,20
# print(b,a)

# # with temp variable
# a=10
# b=20
# temp=a
# a=b
# b=temp
# print(a)
# print(b)
# ____________________________________________________________________________________________


# Q-7 Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

# a=int(input("please enter the number which you want to check even or odd: "))

# if a % 2 == 0:
#     print(f"{a},is an even number..")
# else:
#     print(f"{a}, is an odd number ")
# ____________________________________________________________________________________________


# Q-8 Write a Python program to test whether a passed letter is a vowel or not.

# ch=input("enter a letter which you want to check is vowel or not : ")

# if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" :
#     print(f"{ch} is a vowel")
# else:
#     print(f"{ch} is not a vowel")
# ____________________________________________________________________________________________


# Q-9 Write a Python program to sum of three given integers.However, if two values are equal sum will be zero.
# a= int(input("enter number 1:" ))
# b= int(input("enter number 2:" ))
# c= int(input("enter number 3:" ))

# if a==b or b==c or c==a:
#     print("as the value of two number is same the sum will be 0")
# else:
#     sum=a+b+c
#     print(sum)
# ____________________________________________________________________________________________


# Q-10 Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
# a=int(input("enter a number 1: "))
# b=int(input("enter a number 2: "))
# if a==b or a+b==5 or a-b==5:
#     print("True")
# else:
#     print("False")
# ____________________________________________________________________________________________

# Q-11 Write a python program to sum of the first n positive integers.
# n = int(input("Enter the positive number to sum of it: "))

# sum = (n * (n + 1)) / 2

# print(f"Sum of the first {n} positive number is : {sum}")
# ____________________________________________________________________________________________


# Q-12 Write a Python program to calculate the length of a string.
# str=input("enter a string : ")
# print(len(str))
# ____________________________________________________________________________________________

# Q-13 Write a Python program to count the number of characters (character frequency) in a string

# text = input("Enter the String: ")
# textLen = len(text)
# sum = 0
# for i in range(textLen):
#     sum = sum + 1

# print(f"\nTotal Characters = {sum}")
# print(len(text))
# ____________________________________________________________________________________________

# Q-14 What are negative indexes and why are they used?

# The negative index is used to remove any new-line spaces from the string and allow the string to except the last character that is given as S[:-1].
# negative index shows the index from the end(-1).
# ____________________________________________________________________________________________

# Q-15 Write a Python program to count occurrences of a substring in a string.
# str = input("Enter the string: ")
# substr = input("Enter the word to find how many times it occurs: ") 

# count = str.count(substr)
 
# print(f"Number of occurrences of substring: {count}")
# ____________________________________________________________________________________________

# Q-16 Write a Python program to count the occurrences of each word in a given sentence
# ?????????????????????????????????????????????????????????????????????????????????????????

# Q-17 Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string
# str1 = input("Please Enter First String : ")
# str2 =input("Please Enter Second String : ")

# x = str2[:2] + str1[2:]
# y = str1[:2] + str2[2:]


# print("Your first has become :- ",x)
# print("Your second has become :- ",y)
# ____________________________________________________________________________________________

#  Q-18 Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' 
# insteadif the string length of the given string is less than 3, leave it unchanged

# str = input("Enter the String :")

# if len(str) >= 3:
#     if str.endswith('ing'):
#         print(f"{str.removesuffix('ing')}ly")
#     elif str is not str.endswith('ing'):
#         print(f"{str}ing")
#     else:
#         print(f"{str}")
# else:
#     print(f"{str}")
# ____________________________________________________________________________________________

# Q-19 Write a Python program to find the first appearance of the substring 'not'  and 'poor' froma given string, if 'not' follows the 'poor', replace the whole
# 'not'...'poor'substring with 'good'. Return the resulting string.
# ??????????????????????????????????????????????????????????????????????????

# Q-20 Write a Python function that takes a list of words and returns the length of the longest one.
# str = input("Enter the string:")
# lst= str.split(' ')
# temp = 0

# for i in lst:
#     if temp < len(i):
#         temp = len(i)
#         str1 = lst.index(i)
# print(f"The longest substring in the given string ({str}) is ({lst[str1]}) of which size of sub string is: {temp}")
# _________________________________________________________________________________________________________

# Q-21 Write a Python function to reverses a string if its length is a multiple of 4.
# str=input("enter a string:")

# if(len(str) % 4 == 0):
#     print(f"Reverse string: {str[::-1]}")
# else:
#     print("Reverse can't be possible because string is not multiple of 4")
# _________________________________________________________________________________________________________
# Q-22 Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. Ifthe string length is
# lessthan 2,return instead of the empty string.
# o Sample String:w3resource'
# o Expected Result: 'w3ce'
# o Sample String: 'w3'
# o Expected Result: 'w3w3'
# o Sample String: ' w'
# o Expected Result: Empty String
# ?????????????????????????????????????????????????????????????????????
# _________________________________________________________________________________________________________

# Q-23 Write a Python function to insert a string in the middle of a string.


 

