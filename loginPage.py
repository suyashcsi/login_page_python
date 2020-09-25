from  tkinter import *
from  tkinter import  ttk
from  tkinter import  messagebox

root=Tk()
root.title("Login Page")
l1=ttk.Label(root,text="User Name:")
l1.grid(row=0,column=0)
etUserName=ttk.Entry(root,width=20)
etUserName.grid(row=0,column=1)
l2=ttk.Label(root,text="Password:")
l2.grid(row=1,column=0)
etPassword=ttk.Entry(root,width=20)
etPassword.grid(row=1,column=1)
etPassword.config(show="*")
l3=ttk.Label(root,text="Email:")
l3.grid(row=2,column=0)
etEmail=ttk.Entry(root,width=20)
etEmail.grid(row=2,column=1)
Bulogin=ttk.Button(root,text="Login")
Bulogin.grid(row=3,column=1)

def BuClick():
    print("User name{}, Password: {}" .format (etUserName.get(),etPassword.get()))

Bulogin.config(command=BuClick())

root.mainloop()
