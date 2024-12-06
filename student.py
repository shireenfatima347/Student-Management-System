#================STUDENT=================
from tkinter import *
from tkinter import messagebox


class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        self.root.geometry("800x500+300+150")
        self.root.config(bg="white")

        # Title
        title = Label(self.root, text="Manage Students", font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.pack(side=TOP, fill=X)

        # Labels and Entry Widgets
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white")
        lbl_name.place(x=50, y=100)
        self.txt_name = Entry(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_name.place(x=200, y=100, width=300)

        lbl_roll = Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"), bg="white")
        lbl_roll.place(x=50, y=150)
        self.txt_roll = Entry(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_roll.place(x=200, y=150, width=300)

        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white")
        lbl_course.place(x=50, y=200)
        self.txt_course = Entry(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_course.place(x=200, y=200, width=300)

        lbl_email = Label(self.root, text="Email", font=("goudy old style", 15, "bold"), bg="white")
        lbl_email.place(x=50, y=250)
        self.txt_email = Entry(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_email.place(x=200, y=250, width=300)

        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white")
        lbl_contact.place(x=50, y=300)
        self.txt_contact = Entry(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_contact.place(x=200, y=300, width=300)

        # Buttons
        btn_add = Button(self.root, text="Add", font=("goudy old style", 15, "bold"), bg="green", fg="white",
                         command=self.add_student)
        btn_add.place(x=150, y=400, width=100, height=40)

        btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="blue", fg="white",
                            command=self.update_student)
        btn_update.place(x=270, y=400, width=100, height=40)

        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="red", fg="white",
                            command=self.delete_student)
        btn_delete.place(x=390, y=400, width=100, height=40)

        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="gray", fg="white",
                           command=self.clear_fields)
        btn_clear.place(x=510, y=400, width=100, height=40)

    # Methods
    def add_student(self):
        # Logic to add student details to the database or data structure
        name = self.txt_name.get()
        roll = self.txt_roll.get()
        course = self.txt_course.get()
        email = self.txt_email.get()
        contact = self.txt_contact.get()

        if name == "" or roll == "" or course == "" or email == "" or contact == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
        else:
            # Example: print to console; replace with database insert logic
            print(f"Student Added: {name}, {roll}, {course}, {email}, {contact}")
            messagebox.showinfo("Success", "Student added successfully!", parent=self.root)
            self.clear_fields()

    def update_student(self):
        # Logic to update existing student details
        messagebox.showinfo("Info", "Update functionality is under development!", parent=self.root)

    def delete_student(self):
        # Logic to delete a student
        messagebox.showinfo("Info", "Delete functionality is under development!", parent=self.root)

    def clear_fields(self):
        # Clear all input fields
        self.txt_name.delete(0, END)
        self.txt_roll.delete(0, END)
        self.txt_course.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_contact.delete(0, END)
