import tkinter
import random

screen = tkinter.Tk()
screen.title("Rock Paper Scissor")
screen.geometry("500x500")

var_user_choice=tkinter.StringVar()
var_com_choice=tkinter.StringVar()
var_result_choice=tkinter.StringVar()
var_user_won_count=tkinter.IntVar()
var_comp_won_count=tkinter.IntVar()

game_list=["ROCK","PAPER","SCISSOR"]
u_count=0
c_count=0

def myfun(msg):
    var_user_choice.set(msg)
    com = random.choice(game_list)
    var_com_choice.set(com)
    global u_count, c_count

    if msg == com:
        var_result_choice.set("TIE")
    elif msg == "ROCK":
        if com == "SCISSOR":
            var_result_choice.set("USER WON")
            u_count+=1
            
        else:
            var_result_choice.set("COMPUTER WON")
            c_count+=1
    elif msg == "PAPER":
        if com == "ROCK":
            var_result_choice.set("USER WON")
            u_count+=1
        else:
            var_result_choice.set("COMPUTER WON")
            c_count+=1
    elif msg == "SCISSOR":
        if com =="PAPER":
            var_result_choice.set("USER WON")
            u_count+=1
        else:
            var_result_choice.set("COMPUTER WON")
            c_count+=1
    var_comp_won_count.set(c_count)
    var_user_won_count.set(u_count)        


btn = tkinter.Button(screen,text="ROCK",font=('arial',20,'bold'),bg="blue",fg="white",activebackground="black",activeforeground="white",command = lambda:myfun("ROCK"))
btn.place(x=10,y=10)

btn = tkinter.Button(screen,text="PAPER",font=('arial',20,'bold'),bg="blue",fg="white",activebackground="black",activeforeground="white",command = lambda:myfun("PAPER"))
btn.place(x=150,y=10)

btn = tkinter.Button(screen,text="SCISSOR",font=('arial',20,'bold'),bg="blue",fg="white",activebackground="black",activeforeground="white",command = lambda:myfun("SCISSOR"))
btn.place(x=300,y=10)

user = tkinter.Label(screen,text="USER",font=('arial',14,'bold'))
user.place(x=10,y=150)

computer = tkinter.Label(screen,text="COMPUTER",font=('arial',14,'bold'))
computer.place(x=10,y=200)

user= tkinter.Label(screen,textvariable=var_user_choice,font=('arial',14,'bold'))
user.place(x=150,y=150)

computer= tkinter.Label(screen,textvariable=var_com_choice,font=('arial',14,'bold'))
computer.place(x=150,y=200)

btn = tkinter.Button(screen,textvariable=var_result_choice,font=('arial',20,'bold'),bg="blue",fg="white",activebackground="black",activeforeground="white",width="25")
btn.place(x=10,y=400)

user= tkinter.Label(screen,textvariable=var_user_won_count,font=('arial',14,'bold'))
user.place(x=300,y=150)

computer= tkinter.Label(screen,textvariable=var_comp_won_count,font=('arial',14,'bold'))
computer.place(x=300,y=200)

screen.mainloop()