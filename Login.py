from tkinter import *
from User import *
from tinydb import TinyDB, Query


def NoUser():
    global screen3
    screen3 = Toplevel(screen2)
    screen3.title("")
    screen.geometry("150x100")
    Button(screen3, text="Try Again", command = delete).pack()
    login()



def delete():
    screen3.destroy()

def delete1(): #Delete Login Second Screen
    screen2.destroy()

def reg_user():
    """
    func' that gets users id and name and adds to the database
    :return:
    """
    Username_info = UserName.get()
    ID_info = PersonID.get()
    RegUser(Username_info, ID_info)
    Username_entry.delete(0,END)
    ID_entry.delete(0, END)
    Label(screen1, text="Register Sucsessfuly added").pack()

def login_ver():
    User1 = UserNameVerify.get()
    ID1 = IDVerify.get()

    UserVerify_entry.delete(0,END)
    IDVerify_entry.delete(0, END)
    if checkUser(User1, ID1):
        """""""#login_Sucess()"""
    else:
        NoUser()
        delete1()


def login():
    """
    Log in Screen
    :return:
    """
    global screen2
    global UserNameVerify
    global IDVerify
    global UserVerify_entry
    global IDVerify_entry
    screen2 = Toplevel(screen)
    screen2.title("Login Trivia")
    screen2.geometry("300x250")
    Label(screen2, text="Enter Your Details below: ").pack()
    Label(screen2, text="").pack()

    UserNameVerify = StringVar()
    IDVerify = StringVar()

    Label(screen2 , text="User Name *").pack()
    UserVerify_entry = Entry(screen2, textvariable=UserNameVerify)
    UserVerify_entry.pack()
    Label(screen2, text="ID *").pack()
    IDVerify_entry = Entry(screen2, textvariable=IDVerify)
    IDVerify_entry.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Log in", width=10, height=1, command = login_ver).pack()

def register():
    """
    Register screen
    :return:
    """
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

def main_screen():
    """
    Main screen the from there i choose wheather i want to register or log in
    :return:
    """
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
