def percentage(marks):
    p = ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p
    
marks=[45,78,86,77]
# percentage1 = (sum(marks)/400)*100
percentage1=percentage(marks)
marks2=[75,98,88,78]
# percentage2=((marks2[0]+marks2[1]+marks2[2]+marks2[3])/400)*100
percentage2 = percentage(marks2)

print(percentage1,percentage2)