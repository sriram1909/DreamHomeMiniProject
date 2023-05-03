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
    table.delete(*table.get_children())
    sql = "SELECT propertyNo,city,type,rent FROM propertyForRent WHERE propertyNo not in (select propertyNo from lease)"
    myc.execute(sql)
    result = myc.fetchall()
    for row in result:
        table.insert('', 'end', values=row)
    
    mydb.commit()

root = Tk()
root.title("View properties available")
root.geometry('900x520')
root.configure(bg="#DAF5FF")

view_head_label = Label(root, text="View properties available", font=("Arial", 20, "bold"), bg="#DAF5FF", fg="#576CBC")
view_head_label.place(x=300, y=20)

table = ttk.Treeview(root, columns=('Property Number', 'City', 'Type', 'Rent'), show='headings')
table.heading('Property Number', text='Property Number')
table.heading('City', text='City')
table.heading('Type', text='Type')
table.heading('Rent', text='Rent')

table.place(x=45, y=150)

submit_but = Button(root, text="Click Here to view details", width=30, bg="#E66C22", fg="white",font=("Arial", 12), command=populate_table)
submit_but.place(x=47, y=450)
back=Button(root, text="Back", width=10, bg="#595260", fg="white",font=("Arial", 12), command=back).place(x=597, y=450)

root.mainloop()