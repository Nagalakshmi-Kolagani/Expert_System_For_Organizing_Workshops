from tkinter import *
import sqlite3

root=Tk()
root.geometry('800x800')
root.configure(background='blue')
root.title("Registration for Workshop")


Fullname=StringVar()
Idno=StringVar()
Email=StringVar()
var=IntVar()
c=StringVar()
var1=IntVar()

def show():
    connt=sqlite3.connect('from.db')
    cursor=connt.cursor()
    cursor.execute('SELECT * FROM Student')
    for row in cursor.fetchall():
        print(row)

def max_reg():
    con=sqlite3.connect('from.db')
    cursor=con.cursor()
    cursor.execute('select country ,count(country) from Student group by country order by count(country) desc')
    count=0
    for row in cursor.fetchone():
        if count==0:
            print('The more people participated in workshop is:')
            count=1
        if count==1:
            print(row)

def database():
    name1=Fullname.get()
    idno1=Idno.get()
    email=Email.get()
    gender=var.get()
    country=c.get()
    prog=var1.get()
    conn=sqlite3.connect('From.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student(Fullname TEXT,Idno TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
    cursor.execute('INSERT INTO Student(Fullname,Idno,Email,Gender,country,Programming)VALUES(?,?,?,?,?,?)',(name1,idno1,email,gender,country,prog,))
    conn.commit()
    
dell=StringVar()

def det():
    dee=dell.get()
    connt=sqlite3.connect('from.db')
    cursor=connt.cursor()
    cursor.execute("DELETE FROM Student WHERE Fullname=?",(dee,))
    connt.commit()

label_0=Label(root,text="KLEF WORKSHOPS",width=20,bg='pink',fg='white',font=("bold",20))
label_0.place(x=90,y=53)

label_1=Label(root,text="FullName",width=20,font=("bold",10))
label_1.place(x=80,y=120)

entry_1=Entry(root,textvar=Fullname)
entry_1.place(x=290,y=120)

label_2=Label(root,text="IDNO",width=20,font=("bold",10))
label_2.place(x=80,y=160)

entry_2=Entry(root,textvar=Idno)
entry_2.place(x=290,y=160)

label_3=Label(root,text="Email",width=20,font=("bold",10))
label_3.place(x=80,y=200)

entry_3=Entry(root,textvar=Email)
entry_3.place(x=290,y=200)

label_4=Label(root,text="Gender",width=20,font=("bold",10))
label_4.place(x=80,y=240)

Radiobutton(root,text="Male",padx=5,variable=var,value=1).place(x=290,y=240)

Radiobutton(root,text="Female",padx=20,variable=var,value=2).place(x=350,y=240)

label_5=Label(root,text="workshop",width=20,font=("bold",10))
label_5.place(x=80,y=290)

list1=['WEB','IOT','Distributed computing','Cyber Security','Android','Artificial Intelligence','Data analytics'];

droplist=OptionMenu(root,c,*list1)
droplist.config(width=15)
c.set('select a workshop')
droplist.place(x=290,y=290)

label_4=Label(root,text="Programming Language",width=20,font=("bold",10))
label_4.place(x=80,y=340)

var2=IntVar()
var3=IntVar()

Checkbutton(root,text="java",variable=var1).place(x=290,y=340)

Checkbutton(root,text="python",variable=var2).place(x=350,y=340)

Checkbutton(root,text="C++",variable=var3).place(x=430,y=340)

Button(root,text='Submit',width=25,height=2,bg='green',fg='white',command=database).place(x=180,y=390)

res=Button(root,padx=1,pady=1,text='Show Table',command=show,font=('none 10 bold'))
res.place(x=20,y=420)

res=Button(root,padx=1,pady=1,text='Maximum enrollment workshop',command=max_reg,font=('none 10 bold'))
res.place(x=20,y=480)

labdelete=Label(root,text="Delete:",font=('none,13,bold'))
labdelete.place(x=20,y=540)

endelete=Entry(root,width=20,textvar=dell,font=('none 13 bold'))
endelete.place(x=90,y=540)

butdel=Button(root,padx=2,pady=2,text='Delete',bg='red',fg='white',command=det,font=('none 13 bold'))
butdel.place(x=90,y=580)

root.mainloop()




    
