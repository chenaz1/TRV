from tkinter import *

from tinydb import TinyDB, Query

def register():
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    username = StringVar()
    ID = StringVar()

    Label(screen1, text="Enter Your Details below: ").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="User Name *").pack()
    Entry(screen1, textvariable = username).pack()
    Label(screen1, text="ID *").pack()
    Entry(screen1, textvariable = ID).pack()
    Label(screen1, text="").pack()
    Button(screen1, text="register", width=10, height=1).pack()

def login():
    print("Login")


def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("Trivia")
    Label(text="Trivia", bg="gray", width="300", height="2", font=("Ariel",13)).pack()
    Label(text="").pack()
    Button(text="Login", width="300", height="2", command = login).pack()
    Label(text="").pack()
    Button(text="Register", width="300", height="2",command=register).pack()

    screen.mainloop()

main_screen()

RegUser()
