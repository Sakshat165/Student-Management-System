from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if Utext.get()=='' or Ptext.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif Utext.get()=="admin" and Ptext.get()=='admin':
        window.destroy()
        import sms
        
    else:
        messagebox.showerror('Error','Please enter correct credentials')


window=Tk()
window.title('Student Management System')
window.geometry('500x500+0+0')
window.resizable(0,0)
photo = PhotoImage(file = "students.png")
window.config(bg='gray20')
photo = PhotoImage(file = "students.png")
window.iconphoto(False,photo)
#window.iconphoto(False,photo)
# bgimg=ImageTk.PhotoImage(file='bg3.jpg')

# bglabel=Label(window,image=bgimg)
# bglabel.place(x=0,y=0)


loginFrame=Frame(window,background='gray20',bd=20)
loginFrame.place(x=0,y=50)

logo=PhotoImage(file='Logo.png')
ulogo=PhotoImage(file='user.png')
plogo=PhotoImage(file='padlock.png')

logolabel=Label(loginFrame,image=logo)
logolabel.grid(row=0,column=0,columnspan=2)

usernameLabel=Button(loginFrame,image=ulogo,text='Username',compound=LEFT,font=('times new roman',20,'bold'),background='gray20',bd=5)
passLabel=Button(loginFrame,image=plogo,text='Password',compound=LEFT,font=('times new roman',20,'bold'),background='gray20',bd=5)
usernameLabel.grid(row=1,column=0)
passLabel.grid(row=2,column=0)

Utext=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5)
Utext.grid(row=1,column=1,pady=10,padx=20)
Ptext=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,show="*")
Ptext.grid(row=2,column=1,pady=10,padx=20)

lbutton=Button(loginFrame,text='Login',font=('times new roman',15,'bold'),background='gray20',activebackground='cornflowerblue',cursor='hand2',bd=5,command=login)
lbutton.grid(row=3,column=0,columnspan=2,pady=10)



window.mainloop()