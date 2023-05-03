from tkinter import *
from PIL import ImageTk,Image
import os
import mysql.connector
root = Tk()
root.geometry('800x800')
root.title('Dream Home')
root.iconbitmap('Image Location')
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="passwd",
  database="dreamhome"
)

def staff_view():
    root.destroy()
    os.system("python staffview.py")

def property_view():
    root.destroy()
    os.system("python propertyview.py")

def feedback_view():
    root.destroy()
    os.system("python commentsview.py")

def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    propertyForRent_indicate.config(bg='#c3c3c3')
    staff_indicate.config(bg='#c3c3c3')
    clientRegistration_indicate.config(bg='#c3c3c3')
    private_owner_indicate.config(bg = '#c3c3c3')
    lease_indicate.config(bg='#c3c3c3')
    feedback_indicate.config(bg = '#c3c3c3')
def indicate(lb,page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page()

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()
def property_button():
    def insert_property():
        propertyNo = propertyNo_entry.get()
        street = street_entry.get()
        city = city_entry.get()
        postcode = postcode_entry.get()
        type = type_entry.get()
        rooms = rooms_entry.get()
        rent = rent_entry.get()
        ownerNo = ownerNo_entry.get()
        staffNo = staffNo_entry.get()
        branchNo = branchNo_entry.get()

        mycursor = mydb.cursor()
        sql = "INSERT INTO propertyforrent (propertyNo, street, city, postcode, type, rooms, rent, ownerNo, staffNo, branchNo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (propertyNo, street, city, postcode, type, rooms, rent, ownerNo, staffNo, branchNo)
        mycursor.execute(sql, val)
        mydb.commit()

        propertyNo_entry.delete(0,END)
        street_entry.delete(0,END)
        city_entry.delete(0,END)
        postcode_entry.delete(0,END)
        type_entry.delete(0,END)
        rooms_entry.delete(0,END)
        rent_entry.delete(0,END)
        ownerNo_entry.delete(0,END)
        staffNo_entry.delete(0,END)
        branchNo_entry.delete(0,END)

        success_label.config(text="Record inserted successfully.")
        print(mycursor.rowcount, "record inserted.")
    property_frame=Frame(main_frame)
    header_label = Label(main_frame, text="Insert property details", font=("Arial", 18,"bold"), bg="#a8defb", fg="black")
    header_label.pack(pady=20)

    # Create form
    form_frame = Frame(main_frame, padx=20, pady=10, bg="#a8defb")
    form_frame.pack()

    propertyNo_label = Label(form_frame, text="Property Number", font=("Arial", 14), bg="#a8defb", fg="black")
    propertyNo_label.grid(row=0, column=0, padx=10, pady=10)

    propertyNo_entry = Entry(form_frame, font=("Arial", 14))
    propertyNo_entry.grid(row=0, column=1, padx=10, pady=10)

    street_label = Label(form_frame, text="Street", font=("Arial", 14), bg="#a8defb", fg="black")
    street_label.grid(row=1, column=0, padx=10, pady=10)

    street_entry = Entry(form_frame, font=("Arial", 14))
    street_entry.grid(row=1, column=1, padx=10, pady=10)

    city_label = Label(form_frame, text="City", font=("Arial", 14), bg="#a8defb", fg="black")
    city_label.grid(row=2, column=0, padx=10, pady=10)

    city_entry = Entry(form_frame, font=("Arial", 14))
    city_entry.grid(row=2, column=1, padx=10, pady=10)

    postcode_label = Label(form_frame, text="Postcode", font=("Arial", 14), bg="#a8defb", fg="black")
    postcode_label.grid(row=3, column=0, padx=10, pady=10)

    postcode_entry = Entry(form_frame, font=("Arial", 14))
    postcode_entry.grid(row=3, column=1, padx=10, pady=10)

    type_label = Label(form_frame, text="Type", font=("Arial", 14), bg="#a8defb", fg="black")
    type_label.grid(row=4, column=0, padx=10, pady=10)

    type_entry = Entry(form_frame, font=("Arial", 14))
    type_entry.grid(row=4, column=1, padx=10, pady=10)

    rooms_label = Label(form_frame, text="Rooms", font=("Arial", 14), bg="#a8defb", fg="black")
    rooms_label.grid(row=5, column=0, padx=10, pady=10)

    rooms_entry = Entry(form_frame, font=("Arial", 14))
    rooms_entry.grid(row=5, column=1, padx=10, pady=10)

    rent_label = Label(form_frame, text="Rent", font=("Arial", 14), bg="#a8defb", fg="black")
    rent_label.grid(row=6, column=0, padx=10, pady=10)

    rent_entry = Entry(form_frame, font=("Arial", 14))
    rent_entry.grid(row=6, column=1, padx=10, pady=10)

    ownerNo_label = Label(form_frame, text="Owner Number", font=("Arial", 14), bg="#a8defb", fg="black")
    ownerNo_label.grid(row=7, column=0, padx=10, pady=10)

    ownerNo_entry = Entry(form_frame, font=("Arial", 14))
    ownerNo_entry.grid(row=7, column=1, padx=10, pady=10)

    staffNo_label = Label(form_frame, text="Staff Number", font=("Arial", 14), bg="#a8defb", fg="black")
    staffNo_label.grid(row=8, column=0, padx=10, pady=10)

    staffNo_entry = Entry(form_frame, font=("Arial", 14))
    staffNo_entry.grid(row=8, column=1, padx=10, pady=10)

    branchNo_label = Label(form_frame, text="Branch Number", font=("Arial", 14), bg="#a8defb", fg="black")
    branchNo_label.grid(row=9, column=0, padx=10, pady=10)

    branchNo_entry = Entry(form_frame, font=("Arial", 14))
    branchNo_entry.grid(row=9, column=1, padx=10, pady=10)

    submit_button = Button(main_frame, text="Submit", command=insert_property,bg="green", fg="black", font=("Arial", 16),
                           pady=10, padx=20)
    submit_button.pack(pady=20)

    success_label = Label(main_frame, fg="#4CAF50", font=("Arial", 14), bg="#a8defb")
    success_label.pack()

    property_frame.pack(pady=20)


def home_button():
    home_frame = Frame(main_frame)

    form_frame = Frame(main_frame, padx=20, pady=10, bg="#a8defb")

    my_img = Image.open("logo.jpg")
    my_img = my_img.resize((400, 400), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(my_img)
    img_label = Label(form_frame, image=my_img)
    img_label.image = my_img  # keep a reference to the image to prevent garbage collection
    img_label.grid(row=0, column=0, columnspan=2, pady=20)

    sview_label = Label(form_frame, text="To view staff details", font=("Arial", 16), bg="#a8defb", fg="#000000")
    sview_label.grid(row=2, column=0, pady=20, padx=10)
    s_view_but = Button(form_frame, text="Click Here", width=10, bg="#3E54AC", fg="white", font=("Arial", 12), command=staff_view)
    s_view_but.grid(row=2, column=1, pady=20, padx=10)

    pview_label = Label(form_frame, text="To view properties available", font=("Arial", 16), bg="#a8defb", fg="#000000")
    pview_label.grid(row=3, column=0, pady=20, padx=10)
    pview_but = Button(form_frame, text="Click Here", width=10, bg="#3E54AC", fg="white", font=("Arial", 12), command=property_view)
    pview_but.grid(row=3, column=1, pady=20, padx=10)

    view_label = Label(form_frame, text="View Property feedbacks", font=("Arial", 16), bg="#a8defb", fg="#000000")
    view_label.grid(row=4, column=0, pady=20, padx=10)
    view_but = Button(form_frame, text="Click Here", width=10, bg="#3E54AC", fg="white", font=("Arial", 12), command=feedback_view)
    view_but.grid(row=4, column=1, pady=20, padx=10)

    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    home_frame.pack()



def staff_button():
    def insert_staff():
        staffNo = staffNo_entry.get()
        fName = fName_entry.get()
        position = position_entry.get()
        sex = sex_entry.get()
        telephone = telephone_entry.get()
        Dob = Dob_entry.get()
        salary = salary_entry.get()
        branchNo = branchNo_entry.get()

        mycursor = mydb.cursor()
        sql = "INSERT INTO staff(staffNo,fName,position,sex,telephone,DOB,salary,branchNo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (staffNo, fName, position, sex, telephone, Dob, salary, branchNo)
        mycursor.execute(sql, val)
        mydb.commit()

        staffNo_entry.delete(0,END)
        fName_entry.delete(0,END)
        position_entry.delete(0,END)
        sex_entry.delete(0,END)
        telephone_entry.delete(0,END)
        Dob_entry.delete(0,END)
        salary_entry.delete(0,END)
        branchNo_entry.delete(0,END)

        success_label.config(text="Record inserted successfully.")
        print(mycursor.rowcount, "record inserted.")

    staff_frame = Frame(main_frame,bg="#a8defb")
    header_label = Label(staff_frame, text="Enter staff details", font=("Arial", 18,"bold"), bg="#a8defb", fg="black")
    header_label.pack(pady=20)

    # Create form
    form_frame = Frame(staff_frame, padx=20, pady=10, bg="#a8defb")
    form_frame.pack()

    staffNo_label = Label(form_frame, text="Staff Number", font=("Arial", 14), bg="#a8defb", fg="black")
    staffNo_label.grid(row=0, column=0, padx=10, pady=10)

    staffNo_entry = Entry(form_frame, font=("Arial", 14))
    staffNo_entry.grid(row=0, column=1, padx=10, pady=10)

    fName_label = Label(form_frame, text="Name", font=("Arial", 14), bg="#a8defb", fg="black")
    fName_label.grid(row=1, column=0, padx=10, pady=10)

    fName_entry = Entry(form_frame, font=("Arial", 14))
    fName_entry.grid(row=1, column=1, padx=10, pady=10)

    position_label = Label(form_frame, text="Position", font=("Arial", 14), bg="#a8defb", fg="black")
    position_label.grid(row=2, column=0, padx=10, pady=10)

    position_entry = Entry(form_frame, font=("Arial", 14))
    position_entry.grid(row=2, column=1, padx=10, pady=10)

    sex_label = Label(form_frame, text="Sex", font=("Arial", 14), bg="#a8defb", fg="black")
    sex_label.grid(row=3, column=0, padx=10, pady=10)

    sex_entry = Entry(form_frame, font=("Arial", 14))
    sex_entry.grid(row=3, column=1, padx=10, pady=10)

    telephone_label = Label(form_frame, text="Telephone", font=("Arial", 14), bg="#a8defb", fg="black")
    telephone_label.grid(row=4, column=0, padx=10, pady=10)

    telephone_entry = Entry(form_frame, font=("Arial", 14))
    telephone_entry.grid(row=4, column=1, padx=10, pady=10)

    Dob_label = Label(form_frame, text="Date of Birth", font=("Arial", 14), bg="#a8defb", fg="black")
    Dob_label.grid(row=5, column=0, padx=10, pady=1)
    Dob_entry = Entry(form_frame, font=("Arial", 14))
    Dob_entry.grid(row=5, column=1, padx=10, pady=10)

    salary_label = Label(form_frame, text="Salary", font=("Arial", 14), bg="#a8defb", fg="black")
    salary_label.grid(row=6, column=0, padx=10, pady=1)
    salary_entry = Entry(form_frame, font=("Arial", 14))
    salary_entry.grid(row=6, column=1, padx=10, pady=10)

    branchNo_label = Label(form_frame, text="Branch number", font=("Arial", 14), bg="#a8defb", fg="black")
    branchNo_label.grid(row=7, column=0, padx=10, pady=1)
    branchNo_entry = Entry(form_frame, font=("Arial", 14))
    branchNo_entry.grid(row=7, column=1, padx=10, pady=10)

    submit_button = Button(staff_frame, text="Submit", command=insert_staff, bg="#4CAF50", fg="black", font=("Arial", 16),
                           pady=10, padx=20)
    submit_button.pack(pady=20)

    # Create success label
    success_label = Label(staff_frame, fg="black", font=("Arial", 14), bg="#a8defb")
    success_label.pack()

    staff_frame.pack(pady=20)


def client_registration_button():
    def insert_property():
        clientNo = clientNo_entry.get()
        fName = fName_entry.get()
        branchNo = branchNo_entry.get()
        baddress = baddress_entry.get()
        regBy = regBy_entry.get()
        regDate = regDate_entry.get()
        type = type_entry.get()
        maxRent = maxRent_entry.get()

        mycursor = mydb.cursor()
        sql = "INSERT INTO clientregistration (clientNo, fName, branchNo, baddress, regBy , regDate, type, maxRent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (clientNo, fName, branchNo, baddress, regBy, regDate, type, maxRent)
        mycursor.execute(sql, val)
        mydb.commit()

        clientNo_entry.delete(0,END)
        fName_entry.delete(0,END)
        branchNo_entry.delete(0,END)
        baddress_entry.delete(0,END)
        regBy_entry.delete(0,END)
        regDate_entry.delete(0,END)
        type_entry.delete(0,END)
        maxRent_entry.delete(0,END)

        success_label.config(text="Record inserted successfully.")
        print(mycursor.rowcount, "record inserted.")
    client_registration_frame = Frame(main_frame,bg="#a8defb")
    header_label = Label(client_registration_frame, text="Insert into clientregistration Table", font=("Arial", 18,"bold"),bg="#a8defb")
    header_label.pack(pady=20)

    # Create form
    form_frame = Frame(client_registration_frame, padx=20, pady=10,bg="#a8defb")
    form_frame.pack()

    clientNo_label = Label(form_frame, text="Client Number", font=("Arial", 14),bg="#a8defb")
    clientNo_label.grid(row=0, column=0, padx=10, pady=10)

    clientNo_entry = Entry(form_frame, font=("Arial", 14))
    clientNo_entry.grid(row=0, column=1, padx=10, pady=10)

    fName_label = Label(form_frame, text="Full name", font=("Arial", 14),bg="#a8defb")
    fName_label.grid(row=1, column=0, padx=10, pady=10)

    fName_entry = Entry(form_frame, font=("Arial", 14))
    fName_entry.grid(row=1, column=1, padx=10, pady=10)

    branchNo_label = Label(form_frame, text="Branch Number", font=("Arial", 14),bg="#a8defb")
    branchNo_label.grid(row=2, column=0, padx=10, pady=10)

    branchNo_entry = Entry(form_frame, font=("Arial", 14))
    branchNo_entry.grid(row=2, column=1, padx=10, pady=10)

    baddress_label = Label(form_frame, text="Branch address", font=("Arial", 14),bg="#a8defb")
    baddress_label.grid(row=3, column=0, padx=10, pady=10)

    baddress_entry = Entry(form_frame, font=("Arial", 14))
    baddress_entry.grid(row=3, column=1, padx=10, pady=10)

    regBy_label = Label(form_frame, text="staff ID", font=("Arial", 14),bg="#a8defb")
    regBy_label.grid(row=4, column=0, padx=10, pady=10)

    regBy_entry = Entry(form_frame, font=("Arial", 14))
    regBy_entry.grid(row=4, column=1, padx=10, pady=10)

    regDate_label = Label(form_frame, text="Date", font=("Arial", 14),bg="#a8defb")
    regDate_label.grid(row=5, column=0, padx=10, pady=10)

    regDate_entry = Entry(form_frame, font=("Arial", 14))
    regDate_entry.grid(row=5, column=1, padx=10, pady=10)

    type_label = Label(form_frame, text="Type", font=("Arial", 14),bg="#a8defb")
    type_label.grid(row=6, column=0, padx=10, pady=10)

    type_entry = Entry(form_frame, font=("Arial", 14))
    type_entry.grid(row=6, column=1, padx=10, pady=10)

    maxRent_label = Label(form_frame, text="Max Rent", font=("Arial", 14),bg="#a8defb")
    maxRent_label.grid(row=7, column=0, padx=10, pady=10)

    maxRent_entry = Entry(form_frame, font=("Arial", 14))
    maxRent_entry.grid(row=7, column=1, padx=10, pady=10)

    submit_button = Button(client_registration_frame, text="Submit", command=insert_property, bg="#4CAF50", fg="white", font=("Arial", 16),pady=10, padx=20)
    submit_button.pack(pady=20)

    success_label = Label(client_registration_frame, fg="#4CAF50", font=("Arial", 14),bg="#a8defb")
    success_label.pack()

    client_registration_frame.pack(pady=20)



def lease_button():
    def insert_lease():
        lease_id = lease_id_entry.get()
        client_no = client_no_entry.get()
        rent = rent_entry.get()
        deposit = deposit_entry.get()
        payment_method = payment_method_entry.get()
        property_no = property_no_entry.get()
        rent_start_dt = rent_start_dt_entry.get()
        rent_end_dt = rent_end_dt_entry.get()
        duration = duration_entry.get()

        mycursor = mydb.cursor()
        sql = "INSERT INTO lease (leaseId, clientNo, Rent, Deposit, paymentmethod, propertyNo, rentStartDt, rentEndDt, DurationInYears) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (lease_id, client_no, rent, deposit, payment_method, property_no, rent_start_dt, rent_end_dt, duration)
        mycursor.execute(sql, val)
        mydb.commit()

        lease_id_entry.delete(0,END)
        client_no_entry.delete(0,END)
        rent_entry.delete(0,END)
        deposit_entry.delete(0,END)
        payment_method_entry.delete(0,END)
        property_no_entry.delete(0,END)
        rent_start_dt_entry.delete(0,END)
        rent_end_dt_entry.delete(0,END)
        duration_entry.delete(0,END)

        success_label.config(text="Record inserted successfully.")
        print(mycursor.rowcount, "record inserted.")
    lease_frame = Frame(main_frame,bg="#a8defb")
    header_label = Label(lease_frame, text="Insert into Lease Table", font=("Arial", 18,"bold"), bg="#a8defb", fg="black")
    header_label.pack(pady=20)

    # Create form
    form_frame = Frame(lease_frame, padx=20, pady=10, bg="#a8defb")
    form_frame.pack()

    lease_id_label = Label(form_frame, text="Lease ID", font=("Arial", 14), bg="#a8defb", fg="black")
    lease_id_label.grid(row=0, column=0, padx=10, pady=10)

    lease_id_entry = Entry(form_frame, font=("Arial", 14))
    lease_id_entry.grid(row=0, column=1, padx=10, pady=10)

    client_no_label = Label(form_frame, text="Client Number", font=("Arial", 14), bg="#a8defb", fg="black")
    client_no_label.grid(row=1, column=0, padx=10, pady=10)

    client_no_entry = Entry(form_frame, font=("Arial", 14))
    client_no_entry.grid(row=1, column=1, padx=10, pady=10)

    rent_label = Label(form_frame, text="Rent", font=("Arial", 14), bg="#a8defb", fg="black")
    rent_label.grid(row=2, column=0, padx=10, pady=10)

    rent_entry = Entry(form_frame, font=("Arial", 14))
    rent_entry.grid(row=2, column=1, padx=10, pady=10)

    deposit_label = Label(form_frame, text="Deposit", font=("Arial", 14), bg="#a8defb", fg="black")
    deposit_label.grid(row=3, column=0, padx=10, pady=10)

    deposit_entry = Entry(form_frame, font=("Arial", 14))
    deposit_entry.grid(row=3, column=1, padx=10, pady=10)

    payment_method_label = Label(form_frame, text="Payment Method", font=("Arial", 14), bg="#a8defb", fg="black")
    payment_method_label.grid(row=4, column=0, padx=10, pady=10)

    payment_method_entry = Entry(form_frame, font=("Arial", 14))
    payment_method_entry.grid(row=4, column=1, padx=10, pady=10)

    property_no_label = Label(form_frame, text="Property Number", font=("Arial", 14), bg="#a8defb", fg="black")
    property_no_label.grid(row=5, column=0, padx=10, pady=10)

    property_no_entry = Entry(form_frame, font=("Arial", 14))
    property_no_entry.grid(row=5, column=1, padx=10, pady=10)

    rent_start_dt_label = Label(form_frame, text="Rent Start Date (YYYY-MM-DD)", font=("Arial", 14), bg="#a8defb",fg="black")
    rent_start_dt_label.grid(row=6, column=0, padx=10, pady=10)

    rent_start_dt_entry = Entry(form_frame, font=("Arial", 14))
    rent_start_dt_entry.grid(row=6, column=1, padx=10, pady=10)

    rent_end_dt_label = Label(form_frame, text="Rent End Date (YYYY-MM-DD)", font=("Arial", 14), bg="#a8defb",fg="black")
    rent_end_dt_label.grid(row=7, column=0, padx=10, pady=10)

    rent_end_dt_entry = Entry(form_frame, font=("Arial", 14))
    rent_end_dt_entry.grid(row=7, column=1, padx=10, pady=10)

    duration_label = Label(form_frame, text="Duration in Years", font=("Arial", 14), bg="#a8defb", fg="black")
    duration_label.grid(row=8, column=0, padx=10, pady=10)

    duration_entry = Entry(form_frame, font=("Arial", 14))
    duration_entry.grid(row=8, column=1, padx=10, pady=10)

    # Create button to submit form
    submit_button = Button(lease_frame, text="Insert Record", font=("Arial", 14), command=insert_lease, bg="#4CAF50", fg="black")
    submit_button.pack(pady=20)

    # Create label for success message
    success_label = Label(lease_frame, font=("Arial", 14), bg="#a8defb", fg="black")
    success_label.pack(pady=20)
    lease_frame.pack(pady=20)


def feedback_button():
    def insert_comment():
        clientNo = clientNo_entry.get()
        propertyNo = propertyNo_entry.get()
        viewdate = viewdate_entry.get()
        comment = comment_entry.get()

        mycursor = mydb.cursor()
        sql = "INSERT INTO viewing (clientNo, propertyNo, viewdate, comment) VALUES (%s, %s, %s, %s)"
        val = (clientNo, propertyNo, viewdate, comment)
        mycursor.execute(sql, val)
        mydb.commit()

        clientNo_entry.delete(0,END)
        propertyNo_entry.delete(0,END)
        viewdate_entry.delete(0,END)
        comment_entry.delete(0,END)

        success_label.config(text="Record inserted successfully.")
        print(mycursor.rowcount, "record inserted.")

    feedback_frame  = Frame(main_frame,bg = "#a8defb")
    header_label = Label(feedback_frame, text="Provide your feedback", font=("Arial", 18,"bold"),bg = "#a8defb",fg = "black")
    header_label.pack(pady=20)

    form_frame = Frame(feedback_frame, padx=20, pady=10,bg = "#a8defb")
    form_frame.pack()

    clientNo_label = Label(form_frame, text="Client Number", font=("Arial", 14),bg = "#a8defb",fg = "black")
    clientNo_label.grid(row=0, column=0, padx=10, pady=10)
    clientNo_entry = Entry(form_frame, font=("Arial", 14))
    clientNo_entry.grid(row=0, column=1, padx=10, pady=10)
    
    propertyNo_label = Label(form_frame, text="Property Number", font=("Arial", 14),bg = "#a8defb",fg = "black")
    propertyNo_label.grid(row=1, column=0, padx=10, pady=10)
    propertyNo_entry = Entry(form_frame, font=("Arial", 14))
    propertyNo_entry.grid(row=1, column=1, padx=10, pady=10)

    viewdate_label = Label(form_frame, text="Date viewed", font=("Arial", 14),bg = "#a8defb",fg = "black")
    viewdate_label.grid(row=2, column=0, padx=10, pady=10)
    viewdate_entry = Entry(form_frame, font=("Arial", 14))
    viewdate_entry.grid(row=2, column=1, padx=10, pady=10)

    comment_label = Label(form_frame, text="Comments", font=("Arial", 14),bg = "#a8defb",fg = "black")
    comment_label.grid(row=3, column=0, padx=10, pady=10)
    comment_entry = Entry(form_frame, font=("Arial", 14))
    comment_entry.grid(row=3, column=1, padx=10, pady=10)

    submit_button = Button(feedback_frame, text="Submit", command=insert_comment, bg="#4CAF50", fg="black", font=("Arial", 16), pady=10, padx=20)
    submit_button.pack(pady=20)
    success_label = Label(feedback_frame, fg="#4CAF50", font=("Arial", 14),bg = "#a8defb")
    success_label.pack(pady = 20)
    
    feedback_frame.pack(pady=20)

def private_owner():
    def insert_owner():
        owner_no = owner_no_entry.get()
        first_name = first_name_entry.get()
        # last_name = last_name_entry.get()
        address = address_entry.get()
        tel_no = tel_no_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        mycursor = mydb.cursor()
        sql = "INSERT INTO privateowner (ownerNo, fName,address, telNo, email, password) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (owner_no, first_name, address, tel_no, email, password)
        mycursor.execute(sql, val)
        mydb.commit()
        success_label.config(text="Record inserted successfully.")
        print(mycursor.rowcount, "record inserted.")

    private_owner_frame = Frame(main_frame, bg="#a8defb")
    header_label = Label(private_owner_frame, text="Insert into Private Owner Table", font=("Arial", 18,"bold"),bg="#a8defb")
    header_label.pack(pady=20)

    # Create form
    form_frame = Frame(private_owner_frame, padx=20, pady=10,bg="#a8defb")
    form_frame.pack()

    owner_no_label = Label(form_frame, text="Owner Number", font=("Arial", 14),bg="#a8defb")
    owner_no_label.grid(row=0, column=0, padx=10, pady=10)

    owner_no_entry = Entry(form_frame, font=("Arial", 14))
    owner_no_entry.grid(row=0, column=1, padx=10, pady=10)

    first_name_label = Label(form_frame, text="First Name", font=("Arial", 14),bg="#a8defb")
    first_name_label.grid(row=1, column=0, padx=10, pady=10)

    first_name_entry = Entry(form_frame, font=("Arial", 14))
    first_name_entry.grid(row=1, column=1, padx=10, pady=10)

    address_label = Label(form_frame, text="Address", font=("Arial", 14),bg="#a8defb")
    address_label.grid(row=2, column=0, padx=10, pady=10)

    address_entry = Entry(form_frame, font=("Arial", 14))
    address_entry.grid(row=2, column=1, padx=10, pady=10)

    tel_no_label = Label(form_frame, text="Telephone Number", font=("Arial", 14),bg="#a8defb")
    tel_no_label.grid(row=3, column=0, padx=10, pady=10)

    tel_no_entry = Entry(form_frame, font=("Arial", 14))
    tel_no_entry.grid(row=3, column=1, padx=10, pady=10)

    email_label = Label(form_frame, text="Email", font=("Arial", 14),bg="#a8defb")
    email_label.grid(row=4, column=0, padx=10, pady=10)

    email_entry = Entry(form_frame, font=("Arial", 14))
    email_entry.grid(row=4, column=1, padx=10, pady=10)

    password_label = Label(form_frame, text="Password", font=("Arial", 14),bg="#a8defb")
    password_label.grid(row=5, column=0, padx=10, pady=10)

    password_entry = Entry(form_frame, show="*", font=("Arial", 14))
    password_entry.grid(row=5, column=1, padx=10, pady=10)

    submit_button = Button(private_owner_frame, text="Submit", command=insert_owner, bg="#4CAF50", fg="white", font=("Arial", 16),pady=10, padx=20)
    submit_button.pack(side="bottom", pady=20)

    # Create success label
    success_label = Label(private_owner_frame, fg="#4CAF50", font=("Arial", 14),bg="#a8defb")
    success_label.pack()
    private_owner_frame.pack(pady=20)

options_frame = Frame(root,bg = "#c3c3c3")

home_btn = Button(options_frame,text = 'Home', font = ('Bold',15),fg = '#158aff',bd = 0,bg = "#c3c3c3",command=lambda :indicate(home_indicate,home_button))
home_btn.place(x = 10,y = 50,)

home_indicate = Label(options_frame,text='',bg='#c3c3c3')
home_indicate.place(x=3,y=50,width=5,height=40)

propertyForRent_btn = Button(options_frame,text = 'Property registration', font = ('Bold',15),fg = '#158aff',bd = 0,bg = "#c3c3c3",command=lambda :indicate(propertyForRent_indicate,property_button))
propertyForRent_btn.place(x = 10,y = 110)

propertyForRent_indicate = Label(options_frame,text='',bg='#c3c3c3')
propertyForRent_indicate.place(x=3,y=110,width=5,height=40)

staff_btn = Button(options_frame,text = 'Staff registration', font = ('Bold',15),fg = '#158aff',bd = 0,bg = "#c3c3c3",command=lambda :indicate(staff_indicate,staff_button))
staff_btn.place(x = 10,y = 180)

staff_indicate = Label(options_frame,text='',bg='#c3c3c3')
staff_indicate.place(x=3,y=180,width=5,height=40)

clientRegistration_btn = Button(options_frame,text = 'Client registration', font = ('Bold',15),fg = '#158aff',bd = 0,bg = "#c3c3c3",command=lambda :indicate(clientRegistration_indicate,client_registration_button))
clientRegistration_btn.place(x = 10,y = 250)

clientRegistration_indicate = Label(options_frame,text='',bg='#c3c3c3')
clientRegistration_indicate.place(x=3,y=250,width=5,height=40)

private_owner_btn = Button(options_frame,text = 'Owner Registration', font = ('Bold',15),fg = '#158aff',bd = 0,bg = "#c3c3c3",command=lambda :indicate(private_owner_indicate,private_owner))
private_owner_btn.place(x = 10,y = 320)

private_owner_indicate = Label(options_frame,text='',bg='#c3c3c3')
private_owner_indicate.place(x=3,y=320,width=5,height=40)

lease_btn = Button(options_frame,text = 'Property lease', font = ('Bold',15),fg = '#158aff',bd = 0,bg = "#c3c3c3",command=lambda :indicate(lease_indicate,lease_button))
lease_btn.place(x = 10,y = 390)

lease_indicate = Label(options_frame,text='',bg='#c3c3c3')
lease_indicate.place(x=3,y=390,width=5,height=40)

feedback_btn = Button(options_frame,text = 'Property feedback', font = ('Bold',15),fg = '#158aff',bd = 0,bg = "#c3c3c3",command=lambda :indicate(feedback_indicate,feedback_button))
feedback_btn.place(x = 10,y = 460)

feedback_indicate = Label(options_frame,text='',bg='#c3c3c3')
feedback_indicate.place(x=3,y=460,width=5,height=40)



options_frame.pack(side = LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width =200,height = 800)

main_frame = Frame(root,bg ="#a8defb",highlightbackground='black',highlightthickness=2)

main_frame.pack(side = LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height = 800,width = 600)

root.mainloop()