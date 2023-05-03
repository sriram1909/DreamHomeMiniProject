from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import mysql.connector
mydb = mysql.connector.Connect(
    host='localhost',
    user='root',
    password='pswd',
    database='dreamhome'
)

def back():
    root.destroy()
    os.system("python main.py")

def populate_table():
    myc = mydb.cursor()
    branch_no = branch_no_entry.get()

    table.delete(*table.get_children())
    
    sql = "SELECT staffNo,fName,sex,position,salary FROM staff WHERE branchNo = %s"
    val = (branch_no,)
    myc.execute(sql, val)
    result = myc.fetchall()
    for row in result:
        table.insert('', 'end', values=row)
    
    mydb.commit()

def all_branch():
    myc = mydb.cursor()

    table.delete(*table.get_children())
    
    sql = "SELECT * FROM staff"
    myc.execute(sql)
    result = myc.fetchall()
    for row in result:
        table.insert('', 'end', values=row)
    
    mydb.commit()


root = Tk()
root.title("View staff details")
root.geometry('1290x520')
root.configure(bg="#DAF5FF")

view_head_label = Label(root, text="View Staff Details", font=("Arial", 20, "bold"), bg="#DAF5FF", fg="#576CBC")
view_head_label.place(x=500, y=20)


branch_no_label = Label(root, text="Branch No",bg="#DAF5FF", fg="#394867",font=("Arial", 13))
branch_no_label.place(x=45, y=80)

branch_no_entry = Entry(root, width=30)
branch_no_entry.place(x=145, y=82)

table = ttk.Treeview(root, columns=('Staff Number', 'Employee Name','Sex', 'Position', 'Salary'), show='headings')
table.heading('Staff Number', text='Staff Number')
table.heading('Employee Name', text='Employee Name')
table.heading('Sex', text='Sex')
table.heading('Position', text='Position')
table.heading('Salary', text='Salary')

table.place(x=45, y=200)

submit_but = Button(root, text="Submit", width=10, bg="#3E54AC", fg="white",font=("Arial", 12), command=populate_table)
submit_but.place(x=47, y=130)

submit_but = Button(root, text="All branches staff", width=20, bg="#3E54AC", fg="white",font=("Arial", 12), command=all_branch)
submit_but.place(x=157, y=130)

back=Button(root, text="Back", width=10, bg="#595260", fg="white",font=("Arial", 12), command=back).place(x=597, y=450)

root.mainloop()