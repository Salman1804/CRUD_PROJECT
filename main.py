#import email
from tkinter import *
import tkinter.messagebox as MessageBox
import pymysql
#from requests import delete

root=Tk()
root.geometry("600x300")
root.title("CRUD OPRATIONS WITH TKINTER AND MYSQL")

id=Label(root,text="Enter ID        :",font=('Arial',10,'bold'))
id.place(x=20,y=30)


name=Label(root,text="Enter NAME  :",font=('Arial',10,'bold'))
name.place(x=20,y=60)

email=Label(root,text="Enter EMAIL :",font=('Arial',10,'bold'))
email.place(x=20,y=90)
e_id=Entry()
e_id.place(x=150,y=30)

e_name=Entry()
e_name.place(x=150,y=60)

e_email=Entry()
e_email.place(x=150,y=90)


def insert():
    id=e_id.get()
    name=e_name.get()
    mail=e_email.get()
    if(id=="" or name=="" or mail==""):
        MessageBox.showinfo("INSERT STATUS","ALL FIELDS ARE REQUIRED")
    else:
        con=pymysql.connect(host="localhost", user="root", password="root", database="mydb2")
        cur=con.cursor()
        query=("insert into student values ('"+ id +"','"+ name +"','"+ mail +"')")
        cur.execute(query) 
        cur.execute("commit")
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_email.delete(0,'end')
        show()
        
        MessageBox.showinfo("INSERT STATUS","DATA INSERTED SUCESSFULLY")
        con.close()   




def update():
    id=e_id.get()
    name=e_name.get()
    mail=e_email.get()
    if(id=="" or name=="" or mail==""):
        MessageBox.showinfo("UPDATE STATUS","ALL FIELDS ARE REQUIRED")
    else:
        con=pymysql.connect(host="localhost", user="root", password="root", database="mydb2")
        cur=con.cursor()
        query1=("update student set name='"+ name +"', email='"+ mail +"'where id='"+ id +"'")
        cur.execute(query1) 
        cur.execute("commit")
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_email.delete(0,'end')
        show()
       
        MessageBox.showinfo("INSERT STATUS","DATA UPDATED SUCESSFULLY")
        con.close()

def delete():
    id=e_id.get()
    name=e_name.get()
    mail=e_email.get()
    if(id=="" or name==""):
        MessageBox.showinfo("DELETE STATUS","ID IS COMPULSORY FOR DELETE")
    else:
        con=pymysql.connect(host="localhost", user="root", password="root", database="mydb2")
        cur=con.cursor()
        query2=("delete from student where id='"+ id +"'")
        cur.execute(query2) 
        cur.execute("commit")
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_email.delete(0,'end')
        show()
        
        MessageBox.showinfo("INSERT STATUS","DATA DELETED SUCESSFULLY")
        con.close() 

def get():
    id=e_id.get()
    name=e_name.get()
    mail=e_email.get()
    if(id==""):
        MessageBox.showinfo("FETCH STATUS","ID IS COMPULSORY FOR DISPLAY_DATA")
    else:
        con=pymysql.connect(host="localhost", user="root", password="root", database="mydb2")
        cur=con.cursor()
        query3=("select * from student where id='"+ id +"'")
        cur.execute(query3)
        rows=cur.fetchall()
        for row in rows:
            e_name.insert(0,row[1])
            e_email.insert(0,row[2])         
        
        con.close()

def show():
    con=pymysql.connect(host="localhost",user="root",password="root",database="mydb2")
    cur=con.cursor()
    query4=("select * from student ")
    cur.execute(query4)
    rows=cur.fetchall()
    list.delete(0,list.size())
    for row in rows:
        insertdata=str(row[0])+'    '+row[1]
        list.insert(list.size()+1, insertdata)
    con.close()


insert=Button(root,text="INSERT",font=('verdana',10,'bold italic'),bg="green",bd=5,command=insert)
insert.place(x=20,y=140)


update=Button(root,text="UPDATE",font=('verdana',10,'bold italic'),bg="yellow",bd=5,command=update)
update.place(x=100,y=140)

delete=Button(root,text="DELETE",font=('verdana',10,'bold italic'),bg="red",bd=5,command=delete)
delete.place(x=185,y=140)

get=Button(root,text="GET",font=('verdana',10,'bold italic'),bg="orange",bd=5,command=get)
get.place(x=265,y=140)


list=Listbox(root,font=('verdana',10,'bold italic'),bd=5)
list.place(x=350,y=30)
show()

root.mainloop()