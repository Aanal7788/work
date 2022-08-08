i=1
for i in range(1,10):
    if i<=5:
        print(i,"small than equal to 5")
    else:
        print(i,"larger than 5")

number=23
running=True

while running:
    guess=int(input("enter ur number:"))
    if guess==number:
        print("success")
        running=False
    elif guess<number:
        print("lower than number")
    elif guess>number:
        print("higher then number")
    else:
        print("sorry")
else:
    print("the whileloop is over")
print("done")


for i in range(1,7):
    for j in range(i):
        print(i,end='')
    print()


i=0
j=0
while i<7:
    j=0
    while j<i:
        print(i,end='')
        j=j+1
    i=i+1
    print()