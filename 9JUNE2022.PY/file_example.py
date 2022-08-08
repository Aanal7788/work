"""
r : read mode
w : write mode
a : append mode

"""
import os

# # f = open("C:\\Users\\Harsang\\Desktop\\python\\django_project02\\myenv\\9JUNE2022.PY\\example.txt","r")
# f = open(r"C:\Users\Harsang\Desktop\python\django_project02\myenv\9JUNE2022.PY\example.txt","r")
# l1=f.readlines()
# print(l1)
# print(l1[2])  #--->particular line display
# print("no. of lines in file: ",len(l1))#number of lines display
# print(l1[-1]) #last line display

# # print(f.read())
# # print(f.readline())

# f=open(r"C:\Users\Harsang\Desktop\python\django_project02\myenv\9JUNE2022.PY\myfile_example.txt","a")
# f.write("\n my file practicle")
# f.write("\n this file is created by me \n hello all")
# f.write("\n my name is aanal")
# f.close()

# create blank file

# f = open(r"C:\Users\Harsang\Desktop\python\django_project02\myenv\9JUNE2022.PY\myblankfile.txt","x")

# create folder

if os.path.exists(r"C:\Users\Harsang\Desktop\python\django_project02\myenv\9JUNE2022.PY\MYFOLDER"):
    print("folder already exist")
else:
    os.mkdir(r"C:\Users\Harsang\Desktop\python\django_project02\myenv\9JUNE2022.PY\MYFOLDER")
    print("created folder")