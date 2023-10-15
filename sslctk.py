from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector
from mysql.connector import Error

def Database():
    global conn, cursor
    conn = mysql.connector.connect( host = "localhost", 
    user = "root",
    passwd = "root",
    database="marks",
    auth_plugin="mysql_native_password")
    cursor = conn.cursor()


def add():
    Database()
    name2=name.get()
    name3=name1.get()
    a=mark1.get()
    b=mark2.get()
    c=mark3.get()
    d=mark4.get()
    e=mark5.get()
   
    if(name2==""or name3=="" or a==""  or b=="" or c=="" or d=="" or e ==""):
        MessageBox.showinfo("VALUES MUST","fill all the blocks")
    a1=int(mark1.get())
    b1=int(mark2.get())
    c1=int(mark3.get())
    d1=int(mark4.get())
    e1=int(mark5.get())  
    if(a1>101 or b1>101 or c1>101 or d1>101 or e1>101 ):
        MessageBox.showerror("INVALID MARKS.","please enter valid marks.")
    else:  
      
      f=a1+b1+c1+d1+e1
      label=Label(top,text="MARKS REGISTERED SUCCESSFULLY ..",font=("Comic Sans MS",20,"bold"),bg="darkOrchid4")
      label.grid(row=9,column=1)
      label9=Label(top,text=f"THE TOTAL MARKS IS : {f}",font="300",bg="bisque")
      label9.grid(row=10,column=1,pady=20)
      percent=(f/500)*100
      label11=Label(top,text=f"TOTAL PERCENTAGE IS : {percent}",font="300",bg="bisque")
      label11.grid(row=11,column=1)
    
      add_user=("INSERT INTO `sslc_marks`(Student_name,roll_no,tamil,english,maths,science,s_science,total_marks,percentage)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)") 
      data_user=(name2,name3,a,b,c,d,e,f,percent)
      cursor.execute(add_user,data_user)
      conn.commit()
      cursor.close()
      conn.close()


top=Tk()
top.geometry("1000x800")
top.title("SSLC MARKS")
top.configure(bg="bisque")
labelm=Label(top,text="SSLC MARKS ..",fg="black",bg="navajowhite2",font= ("monaco", 25, "bold"))
labelm.grid(row=0,column=0,columnspan=80)

label1=Label(top,text="ENTER THE STUDENT  NAME HERE : ",bg="bisque",font=("Copperplate",10,"italic"))
label1.grid(row=1,column=0,pady=25)
label2=Label(text="ENTER THE ROLL NO: ",bg="bisque",font=("Copperplate",10,"italic"))
label2.grid(row=2,column=0)
name=Entry(top)
name.grid(row=1,column=1,padx=60)
name1=Entry(top)
name1.grid(row=2,column=1)
label3=Label(top,text="ENTER THE MARKS HERE : ",font=("monaco",20,"bold"),bg="light goldenrod")
label3.grid(row=3,column=1,pady=30)

#marks label:
label4=Label(top,text="TAMIL  : ",bg="bisque",font=("Copperplate",10,"italic"))
label4.grid(row=4,column=0,pady=20)
mark1=Entry(top)
mark1.grid(row=4,column=1)
label5=Label(text="ENGLISH : ",bg="bisque",font=("Copperplate",10,"italic"))
label5.grid(row=5,column=0)
mark2=Entry(top)
mark2.grid(row=5,column=1)
label6=Label(top,text="MATHS : ",font=("Copperplate",10,"italic"),bg="bisque")
label6.grid(row=6,column=0)
mark3=Entry(top)
mark3.grid(row=6,column=1,pady=20)
label7=Label(top,text="SCIENCE : ",bg="bisque",font=("Copperplate",10,"italic"))
label7.grid(row=7,column=0)
mark4=Entry(top)
mark4.grid(row=7,column=1)
label8=Label(top,text="S.SCIENCE : ",bg="bisque",font=("Copperplate",10,"italic"))
label8.grid(row=8,column=0)
mark5=Entry(top)
mark5.grid(row=8,column=1,pady=20)

button=Button(top,text="TOTAL",command=add,bg="cornsilk2")
button.grid(row=9,column=0)
top.mainloop()
