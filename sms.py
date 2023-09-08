from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox
import pymysql

def view1():
        global fftable
        stable.destroy()
        rightFrame=Frame(root)
        rightFrame.place(x=300,y=80,width=850,height=600)

        scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
        scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

        fftable=ttk.Treeview(rightFrame,columns=('Id','Fees'),xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
        scrollBarX.config(command=fftable.xview)
        scrollBarY.config(command=fftable.yview)
        scrollBarX.pack(side=BOTTOM,fill=X)
        scrollBarY.pack(side=RIGHT,fill=Y)
        fftable.pack(fill=BOTH,expand=1)

        fftable.heading('Id',text='Id')
        fftable.heading('Fees',text='Fees')

def view():
    global stable
    rightFrame=Frame(root)
    rightFrame.place(x=300,y=80,width=850,height=600)

    scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL,background='gray20')
    scrollBarY=Scrollbar(rightFrame,orient=VERTICAL,background='gray20')

    stable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time'),xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
    scrollBarX.config(command=stable.xview,bg='gray20')
    scrollBarY.config(command=stable.yview,bg='gray20')
    scrollBarX.pack(side=BOTTOM,fill=X)
    scrollBarY.pack(side=RIGHT,fill=Y)
    stable.pack(fill=BOTH,expand=1)

    stable.heading('Id',text='Id')
    stable.heading('Name',text='Name')
    stable.heading('Mobile',text='Mobile')
    stable.heading('Email',text='Email')
    stable.heading('Address',text='Address')
    stable.heading('Gender',text='Gender')
    stable.heading('DOB',text='DOB')
    stable.heading('Added Date',text='Added Date')
    stable.heading('Added Time',text='Added Time')
    stable.config(show='headings')

def exit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass
    
def fees():
        def de():
                index=fftable.focus()
                content=fftable.item(index)
                id=content['values'][0]
                query='delete from fees where id=%s'
                mycursor.execute(query,id)
                con.commit()
                s()


        def u():
            query='update fees set fees=%s where id=%s'
            mycursor.execute(query,(feef.get(),idf.get()))
            con.commit()
            addwindow.destroy()
            s()
            

        def s():
            view1()
            query='select * from fees'
            mycursor.execute(query)
            fftable.delete(*fftable.get_children())
            d=mycursor.fetchall()
            for data in d:
                fftable.insert('',END,values=data)
                addwindow.destroy()


        def f():
                view1()
                
                if idf.get()=='' or feef.get()=='':
                    messagebox.showerror('Error',"Please fill all the fields",parent=addwindow)
                else:
                    date=time.strftime('%d/%m/%Y')
                    ctime=time.strftime('%I:%M:%S %p')
                    try:
                        query='insert into fees values(%s,%s)'
                        mycursor.execute(query,(idf.get(),feef.get()))
                        con.commit()
                        result=messagebox.askyesno('Confirm','Sure to clean fields',parent=addwindow)
                        if result:
                            idf.delete(0,END)
                            feef.delete(0,END)
                            
                        else:
                            pass

                    except:
                        messagebox.showerror('Error','Duplicate ID',parent=addwindow)
                        return

                    

                    query='select * from fees'
                    mycursor.execute(query)
                    fd=mycursor.fetchall()
                    fftable.delete(*fftable.get_children())
                    for data in fd:
                        dl=list(data)
                        fftable.insert('',END,values=dl)
        

        
        
        addwindow=Toplevel()
        addwindow.geometry('430x180+0+0')
        addwindow.title='Fees'
        idlabel=Label(addwindow,text='Id',font=('times new roman',20,'bold'))
        idlabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
        idf=Entry(addwindow,font=('roman',15,'bold'),width=24)
        idf.grid(row=0,column=1,pady=15,padx=10)


        feelabel=Label(addwindow,text='Amount',font=('times new roman',20,'bold'))
        feelabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
        feef=Entry(addwindow,font=('roman',15,'bold'),width=24)
        feef.grid(row=1,column=1,pady=15,padx=10)

        sbutton=ttk.Button(addwindow,text='New',command=f)
        sbutton.place(x=15,y=135)
        sbutton=ttk.Button(addwindow,text='Show',command=s)
        sbutton.place(x=120,y=135)
        sbutton=ttk.Button(addwindow,text='Update',command=u)
        sbutton.place(x=330,y=135)
        sbutton=ttk.Button(addwindow,text='Delete',command=de)
        sbutton.place(x=220,y=135)
        index=fftable.focus()
        content=fftable.item(index)
        d=content['values']
        idf.insert(0,d[0])
        feef.insert(0,d[1])

def update():
    
    #view()
    def up():
        query='update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,addeddate=%s,addedtime=%s where id=%s'
        mycursor.execute(query,(namef.get(),mobilef.get(),emailf.get(),addf.get(),gf.get(),df.get(),date,ctime,idf.get()))
        con.commit()
        updatewindow.destroy()
        show()

    updatewindow=Toplevel()
    updatewindow.title='Search Student'
    idlabel=Label(updatewindow,text='Id',font=('times new roman',20,'bold'))
    idlabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idf=Entry(updatewindow,font=('roman',15,'bold'),width=24)
    idf.grid(row=0,column=1,pady=15,padx=10)


    namelabel=Label(updatewindow,text='Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    namef=Entry(updatewindow,font=('roman',15,'bold'),width=24)
    namef.grid(row=1,column=1,pady=15,padx=10)

    mobilelabel=Label(updatewindow,text='Mobile',font=('times new roman',20,'bold'))
    mobilelabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    mobilef=Entry(updatewindow,font=('roman',15,'bold'),width=24)
    mobilef.grid(row=2,column=1,pady=15,padx=10)


    emaillabel=Label(updatewindow,text='Email',font=('times new roman',20,'bold'))
    emaillabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailf=Entry(updatewindow,font=('roman',15,'bold'),width=24)
    emailf.grid(row=3,column=1,pady=15,padx=10)


    addlabel=Label(updatewindow,text='Address',font=('times new roman',20,'bold'))
    addlabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addf=Entry(updatewindow,font=('roman',15,'bold'),width=24)
    addf.grid(row=4,column=1,pady=15,padx=10)

    glabel=Label(updatewindow,text='Gender',font=('times new roman',20,'bold'))
    glabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    gf=Entry(updatewindow,font=('roman',15,'bold'),width=24)
    gf.grid(row=5,column=1,pady=15,padx=10)


    dlabel=Label(updatewindow,text='D.O.B',font=('times new roman',20,'bold'))
    dlabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    df=Entry(updatewindow,font=('roman',15,'bold'),width=24)
    df.grid(row=6,column=1,pady=15,padx=10)

    sbutton=ttk.Button(updatewindow,text='Update Student',command=up)
    sbutton.grid(row=7,columnspan=2)

    index=stable.focus()
    content=stable.item(index)
    d=content['values']
    idf.insert(0,d[0])
    namef.insert(0,d[1])
    mobilef.insert(0,d[2])
    emailf.insert(0,d[3])
    addf.insert(0,d[4])
    gf.insert(0,d[5])
    df.insert(0,d[6])


def delete():
    
    index=stable.focus()
    content=stable.item(index)
    id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,id)
    con.commit()
    query='select * from student'
    mycursor.execute(query)
    stable.delete(*stable.get_children())
    d=mycursor.fetchall()
    for data in d:
        stable.insert('',END,values=data)

    
def show():
    view()
    query='select * from student'
    mycursor.execute(query)
    stable.delete(*stable.get_children())
    d=mycursor.fetchall()
    for data in d:
        stable.insert('',END,values=data)

   

def search():
    def s():
        query='select * from student where id=%s or name=%s or address=%s or gender=%s '
        mycursor.execute(query,(idf.get(),namef.get(),addf.get(),gf.get()))
        stable.delete(*stable.get_children())
        fd=mycursor.fetchall()
        for data in fd:
            d=list(data)
            stable.insert('',END,values=d)

    searchwindow=Toplevel()
    searchwindow.title='Search Student'
    idlabel=Label(searchwindow,text='Id',font=('times new roman',20,'bold'))
    idlabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idf=Entry(searchwindow,font=('roman',15,'bold'),width=24)
    idf.grid(row=0,column=1,pady=15,padx=10)


    namelabel=Label(searchwindow,text='Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    namef=Entry(searchwindow,font=('roman',15,'bold'),width=24)
    namef.grid(row=1,column=1,pady=15,padx=10)

    mobilelabel=Label(searchwindow,text='Mobile',font=('times new roman',20,'bold'))
    mobilelabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    mobilef=Entry(searchwindow,font=('roman',15,'bold'),width=24)
    mobilef.grid(row=2,column=1,pady=15,padx=10)


    emaillabel=Label(searchwindow,text='Email',font=('times new roman',20,'bold'))
    emaillabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailf=Entry(searchwindow,font=('roman',15,'bold'),width=24)
    emailf.grid(row=3,column=1,pady=15,padx=10)


    addlabel=Label(searchwindow,text='Address',font=('times new roman',20,'bold'))
    addlabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addf=Entry(searchwindow,font=('roman',15,'bold'),width=24)
    addf.grid(row=4,column=1,pady=15,padx=10)

    glabel=Label(searchwindow,text='Gender',font=('times new roman',20,'bold'))
    glabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    gf=Entry(searchwindow,font=('roman',15,'bold'),width=24)
    gf.grid(row=5,column=1,pady=15,padx=10)


    dlabel=Label(searchwindow,text='D.O.B',font=('times new roman',20,'bold'))
    dlabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    df=Entry(searchwindow,font=('roman',15,'bold'),width=24)
    df.grid(row=6,column=1,pady=15,padx=10)

    sbutton=ttk.Button(searchwindow,text='Search Student',command=s)
    sbutton.grid(row=7,columnspan=2)



def add():
    view()
    def adds():
        if idf.get()=='' or namef.get()=='' or mobilef.get()=='' or emailf.get()=='' or addf.get()=='' or gf.get()=='' or df.get()=='':
            messagebox.showerror('Error',"Please fill all the fields",parent=addwindow)
        else:
            date=time.strftime('%d/%m/%Y')
            ctime=time.strftime('%I:%M:%S %p')
            try:
                query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(idf.get(),namef.get(),mobilef.get(),emailf.get(),addf.get(),gf.get(),df.get(),date,ctime))
                con.commit()
                result=messagebox.askyesno('Confirm','Sure to clean fields',parent=addwindow)
                if result:
                    idf.delete(0,END)
                    namef.delete(0,END)
                    emailf.delete(0,END)
                    mobilef.delete(0,END)
                    addf.delete(0,END)
                    gf.delete(0,END)
                    df.delete(0,END)
                else:
                    pass

            except:
                messagebox.showerror('Error','Duplicate ID',parent=addwindow)
                return

            

            query='select * from student'
            mycursor.execute(query)
            fd=mycursor.fetchall()
            stable.delete(*stable.get_children())
            for data in fd:
                dl=list(data)
                stable.insert('',END,values=dl)

        
        
    addwindow=Toplevel()
    addwindow.title='Add Student'
    idlabel=Label(addwindow,text='Id',font=('times new roman',20,'bold'))
    idlabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idf=Entry(addwindow,font=('roman',15,'bold'),width=24)
    idf.grid(row=0,column=1,pady=15,padx=10)


    namelabel=Label(addwindow,text='Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    namef=Entry(addwindow,font=('roman',15,'bold'),width=24)
    namef.grid(row=1,column=1,pady=15,padx=10)

    mobilelabel=Label(addwindow,text='Mobile',font=('times new roman',20,'bold'))
    mobilelabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    mobilef=Entry(addwindow,font=('roman',15,'bold'),width=24)
    mobilef.grid(row=2,column=1,pady=15,padx=10)


    emaillabel=Label(addwindow,text='Email',font=('times new roman',20,'bold'))
    emaillabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailf=Entry(addwindow,font=('roman',15,'bold'),width=24)
    emailf.grid(row=3,column=1,pady=15,padx=10)


    addlabel=Label(addwindow,text='Address',font=('times new roman',20,'bold'))
    addlabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addf=Entry(addwindow,font=('roman',15,'bold'),width=24)
    addf.grid(row=4,column=1,pady=15,padx=10)

    glabel=Label(addwindow,text='Gender',font=('times new roman',20,'bold'))
    glabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    gf=Entry(addwindow,font=('roman',15,'bold'),width=24)
    gf.grid(row=5,column=1,pady=15,padx=10)


    dlabel=Label(addwindow,text='D.O.B',font=('times new roman',20,'bold'))
    dlabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    df=Entry(addwindow,font=('roman',15,'bold'),width=24)
    df.grid(row=6,column=1,pady=15,padx=10)

    addbutton=ttk.Button(addwindow,text='Add Student',command=adds)
    addbutton.grid(row=7,columnspan=2)
    

def connect():
    
    def connect1():
        global mycursor,con
        try:
            #con=pymysql.connect(host=hostf.get(),user=uf.get(),password=pf.get())
            con=pymysql.connect(host='localhost',user='root',password='sakshat')
            mycursor=con.cursor()
            
        except:
            messagebox.showerror('Error','Invalid Details',parent=cwindow)
            return
        try:
            query='create database student'
            mycursor.execute(query)
            query='use student'
            mycursor.execute(query)
            query='create table student(id int,name varchar(20),mobile varchar(20),email varchar(20),address varchar(20),gender varchar(20),dob varchar(20),addeddate varchar(20),addedtime varchar(20))'
            mycursor.execute(query)
        except:
            query='use student'
            mycursor.execute(query)
        messagebox.showinfo('Success','Database Connection is Successful')
        cwindow.destroy()










    cwindow=Toplevel()
    cwindow.geometry('470x250+730+230')
    cwindow.title('Database Connection')
    cwindow.resizable(0,0)
    cwindow.grab_set()

    hostname=Label(cwindow,text="Host Name",font=('arial',20,'bold'))
    hostname.grid(row=0,column=0,padx=20)
    hostf=Entry(cwindow,font=('roman',15,'bold'),bd=2)
    hostf.grid(row=0,column=1,padx=40,pady=20)

    uname=Label(cwindow,text="UserName",font=('arial',20,'bold'))
    uname.grid(row=1,column=0,padx=20)
    uf=Entry(cwindow,font=('roman',15,'bold'),bd=2)
    uf.grid(row=1,column=1,padx=40,pady=20)

    pname=Label(cwindow,text="Password",font=('arial',20,'bold'))
    pname.grid(row=3,column=0,padx=20)
    pf=Entry(cwindow,font=('roman',15,'bold'),bd=2,show="*")
    pf.grid(row=3,column=1,padx=40,pady=20)

    cbutton=ttk.Button(cwindow,text="Connect",command=connect1)
    cbutton.grid(row=4,column=0,columnspan=2)

count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(100,slider)


def clock():
    global date,ctime
    date=time.strftime('%d/%m/%Y')
    ctime=time.strftime('%I:%M:%S %p')
    datetimelabel.config(text=f'   Date: {date}\nTime: {ctime}')
    datetimelabel.after(1000,clock)

root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('equilux')
root.geometry('1174x680+0+0')
root.title('Student Management System')
root.resizable(0,0)
photo = PhotoImage(file = "students.png")
root.iconphoto(False,photo)
root.config(bg='gray20')

datetimelabel=Label(root,text="hello",font=('times new roman',18,'bold'),background='gray20',fg='gray50')
datetimelabel.place(x=5,y=5)
clock()
s='Student Management System'
sliderLabel=Label(root,text=s,font=('times new roman',25,'bold'),width=30,background='gray20',fg='gray50')
sliderLabel.place(x=300,y=0)
slider()

cbutton=ttk.Button(root,text='Connect database',command=connect)
cbutton.place(x=980,y=1)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80)
leftFrame.config(bg='gray20')

logo=PhotoImage(file='students.png')
logolabel=Label(leftFrame,image=logo)
logolabel.grid(row=0,column=0)
logolabel.config(bg='gray20')

sbutton=ttk.Button(leftFrame,text='Add Student',command=add)
sbutton.grid(row=1,column=0,pady=20)

s1button=ttk.Button(leftFrame,text='Search Student',command=search)
s1button.grid(row=2,column=0,pady=20)

s2button=ttk.Button(leftFrame,text='Delete Student',command=delete)
s2button.grid(row=3,column=0,pady=20)

s3button=ttk.Button(leftFrame,text='Update Student',command=update)
s3button.grid(row=4,column=0,pady=20)

s4button=ttk.Button(leftFrame,text='Show Student',command=show)
s4button.grid(row=5,column=0,pady=20)

s5button=ttk.Button(leftFrame,text='Fees',command=fees)
s5button.grid(row=6,column=0,pady=20)

s6button=ttk.Button(leftFrame,text='Exit',command=exit)
s6button.grid(row=7,column=0,pady=20)
view()
root.mainloop()
