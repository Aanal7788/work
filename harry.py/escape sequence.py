# story="Aanal is good.\nshe is very good"
# print(story)

# \n(newline)   \t(tab)   \'(single quote)   \\(single backslash)

# practice set string

# name = input("enter ur name \n")
# print("good afternoon, " + name)

letter ='''Dear <|name|> ,
greetings from tops tech house.i m happy to tell you about your selection
You are selected!
have a great day ahead!
thanks and regards

date: <|date|>
'''

name=input("enter ur name")
date=input("enter date\n")
letter = letter.replace("<|name|>" , name)
letter = letter.replace("<|date|>" , date)
print(letter)