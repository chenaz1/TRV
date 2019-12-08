from tkinter import *
from User import *
from tinydb import TinyDB, Query


def reg_user():
    Username_info = UserName.get()
    ID_info = PersonID.get()
    RegUser(Username_info, ID_info)
    Username_entry.delete(0,END)
    ID_entry.delete(0, END)
    Label(screen1, text="Register Sucsessfuly added").pack()


def register():
    global UserName
    global PersonID
    global ID_entry
    global Username_entry
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    UserName = StringVar()
    PersonID = StringVar()

    Label(screen1, text="Enter Your Details below: ").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="User Name *").pack()
    Username_entry = Entry(screen1, textvariable=UserName)
    Username_entry.pack()
    Label(screen1, text="ID *").pack()
    ID_entry = Entry(screen1, textvariable=PersonID)
    ID_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="register", width=10, height=1, command=reg_user).pack()


def login():
    print("Login")


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Trivia")
    Label(text="Trivia", bg="gray", width="300", height="2", font=("Ariel", 13)).pack()
    Label(text="").pack()
    Button(text="Login", width="300", height="2", command=login).pack()
    Label(text="").pack()
    Button(text="Register", width="300", height="2", command=register).pack()

    screen.mainloop()


main_screen()
