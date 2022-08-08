# a=36
# b=15

# print("the reminder of a\b is",a%b)


# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# avg=(a+b)/2
# print("the avg of a and b is",avg)


# a=34
# b="aanal"
# print(a,b)



# name="Harry"
# print(name[3])
# print(name[0:3])
# print(name[1:4])
# print(name[:4])
# print(name[2:])
# print(name[-4:-1])


# list and tuples practice

# f1=input("enter fruit no 1: ")
# f2=input("enter fruit no 2: ")
# f3=input("enter fruit no 3: ")
# f4=input("enter fruit no 4: ")
# f5=input("enter fruit no 5: ")
# f6=input("enter fruit no 6: ")
# f7=input("enter fruit no 7: ")
# myfruitlist = [f1, f2, f3, f4, f5, f6, f7]
# print(myfruitlist)


# pr_02
# m1=int(input("enter marks for student no 1: "))
# m2=int(input("enter marks for student no 2: "))
# m3=int(input("enter marks for student no 3: "))
# m4=int(input("enter marks for student no 4: "))
# m5=int(input("enter marks for student no 5: "))
# m6=int(input("enter marks for student no 6: "))
# mylist = [m1, m2, m3, m4, m5, m6]
# mylist.sort()
# print(mylist)


# pr_03

# tuple change test
# a=(2, 4, 5, 3, 2)
# a[0] =45

# pr_04

# a=[2, 4, 5, 7]
# print(a[0] + a[1]+ a[2]+a[3]) or
# print(sum(a))

# pr_05

# a=(7, 0, 8, 0, 0, 9)
# print(a.count(0))


##dict &set practice

# pr_01
# mydict = {
#     "pankha": "fan",
#     "dabba":"box",
#     "vastu":"item"
# }
# print("ur options are:",mydict.keys())
# a = input("enter the hindi word\n")
# # print("the meaning of your word is:",mydict[a])
# #below line will not throw an error if the key is not present in the dictionary
# print("the meaning of your word is:", mydict.get(a))

#pr_02
# num1 = int(input("enter num 1 : "))
# num2 = int(input("enter num 2 : "))
# num3 = int(input("enter num 3 : "))
# num4 = int(input("enter num 4 : "))
# num5 = int(input("enter num 5 : "))
# num6 = int(input("enter num 6 : "))
# num7 = int(input("enter num 7 : "))
# num8 = int(input("enter num 8 : "))
# s={num1,num2,num3,num4,num5,num6,num7,num8}
# print(s)

#pr_03
# s={18 , "18"}
# print(s)

#pr_04
# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(s)
# print(len(s))

# pr_06
# favlang={}
# a=input("enter your favourite language dharti: ")
# b=input("enter your favourite language pooja: ")
# c=input("enter your favourite language jui: ")
# d=input("enter your favourite language jalpa: ")
# favlang["dharti"] = a
# favlang["pooja"] = b
# favlang["jui"] = c
# favlang["jalpa"] = d
# print(favlang)


#if_else_practice set
# pr_01

# 

# pr_02
# sub1 = int(input("enter ur marks: "))
# sub2 = int(input("enter ur marks: "))
# sub3 = int(input("enter ur marks: "))
# if (sub1<33 or sub2<33 or sub3<33):
#     print("you are fail due to less than 33% in one subject")

# elif (sub1+sub2+sub3)/3 <40:
#     print("yor are fail due to less than 40% in total")

# else:
#     print("congratulations!..you passed the exam")

# pr_03
# text = input("enter the text:")
# if("make a lot of money"in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# else:
#     spam = False

# if spam == True:
#     print("this text is spam")
# else:
#     print("this text is not spam")


# pr_05
# names =["aanal","pooja","dharti","jui","preya","dhyana"]
# name=input("enter your name to check: ")
# if name in names:
#     print("your name is present in the list")
# else:
#     print("your name is not present in the list")
    
# pr_06
# marks=int(input("enter ur marks: "))
# if marks>=90:
#     grade="Ex"
# elif marks>=80:
#     grade="A"
# elif marks>=70:
#     grade="B"
# elif marks>=60:
#     grade="C"
# elif marks>=50:
#     grade="D"
# else:
#     grade="FAIL"
# print("your grade is", grade)



