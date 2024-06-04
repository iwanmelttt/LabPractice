from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Employee.db")
root = Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

# Entries Frame
entries_frame = Frame(root, bg="#D3D3D3")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Employee Management System", font=("times new roman", 18, "bold"), bg="#D3D3D3", fg="black")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")  #alignment to left, e for right, nsew for center

lblName = Label(entries_frame, text="Name", font=("times new roman", 16), bg="#D3D3D3", fg="black")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
txtName = Entry(entries_frame, textvariable=name, font=("times new roman", 16), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

lblAge = Label(entries_frame, text="Age", font=("times new roman", 16), bg="#D3D3D3", fg="black")
lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
txtAge = Entry(entries_frame, textvariable=age, font=("times new roman", 16), width=30)
txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")

lbldoj = Label(entries_frame, text="Date of Birth", font=("times new roman", 16), bg="#D3D3D3", fg="black")
lbldoj.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
txtDoj = Entry(entries_frame, textvariable=doj, font=("times new roman", 16), width=30)
txtDoj.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

lblEmail = Label(entries_frame, text="Email", font=("times new roman", 16), bg="#D3D3D3", fg="black")
lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
txtEmail = Entry(entries_frame, textvariable=email, font=("times new roman", 16), width=30)
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")

lblGender = Label(entries_frame, text="Gender", font=("times new roman", 16), bg="#D3D3D3", fg="black")
lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
comboGender = ttk.Combobox(entries_frame, font=("times new roman", 16), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=3, column=1, padx=10, sticky="nsew")

lblContact = Label(entries_frame, text="Contact No", font=("times new roman", 16), bg="#D3D3D3", fg="black")
lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")
txtContact = Entry(entries_frame, textvariable=contact, font=("times new roman", 16), width=30)
txtContact.grid(row=3, column=3, padx=10, sticky="nsew")

lblAddress = Label(entries_frame, text="Address", font=("times new roman", 16), bg="#D3D3D3", fg="black")
lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

txtAddress = Text(entries_frame, width=85, height=5, font=("times new roman", 16))
txtAddress.grid(row=5, column=0, columnspan=4, padx=10, sticky="nsew")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        centered_row = tuple([str(value).center(25) for value in row])  # Centering each value in the row
        tv.insert("", END, values=centered_row)


def add_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return
    db.insert(txtName.get(),txtAge.get(), txtDoj.get() , txtEmail.get() ,comboGender.get(), txtContact.get(), txtAddress.get(
            1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    displayAll()



def update_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(),
              txtAddress.get(
                  1.0, END))
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    displayAll()


def delete_employee():
    db.remove(row[0])
    clearAll()
    displayAll()


def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0, END)


btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="black",
                bg="pink", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="black", bg="#90EE90",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="black", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="black",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)

# Table Frame
#treeview widget - display hierarchical data in a tabular form
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Name")
tv.heading("3", text="Age")
tv.column("3", width=5)
tv.heading("4", text="D.O.B")
tv.column("4", width=10)
tv.heading("5", text="Email")
tv.heading("6", text="Gender")
tv.column("6", width=10)
tv.heading("7", text="Contact")
tv.heading("8", text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

displayAll()
root.mainloop()