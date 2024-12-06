#=========================================RESULT=============================================================
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # pip install pillow
import sqlite3


class resultClass:
    def __init__(self, root):  # Constructor
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.focus_force()

        # ==== TITLE =====
        title = Label(self.root, text="Add Student Result", font=("goudy old style", 20, "bold"), bg="orange", fg="black")
        title.place(x=10, y=15, width=1180, height=50)

        # ====== Variables =======
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []
        self.fetch_roll()

        # ====== Widgets =======
        lbl_select = Label(self.root, text="Select Student", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=100)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=160)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=220)
        lbl_marks_ob = Label(self.root, text="Marks Obtained", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=280)
        lbl_full_marks = Label(self.root, text="Full Marks", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=340)

        self.txt_student = ttk.Combobox(
            self.root, textvariable=self.var_roll, values=self.roll_list, font=("goudy old style", 15, "bold"),
            state="readonly", justify=CENTER
        )
        self.txt_student.place(x=280, y=100, width=200)
        self.txt_student.set("Select")

        btn_search = Button(
            self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2",
            command=self.search
        )
        btn_search.place(x=500, y=100, width=100, height=28)

        txt_name = Entry(
            self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"), bg="lightyellow", state="readonly"
        )
        txt_name.place(x=280, y=160, width=320)

        txt_course = Entry(
            self.root, textvariable=self.var_course, font=("goudy old style", 20, "bold"), bg="lightyellow", state="readonly"
        )
        txt_course.place(x=280, y=220, width=320)

        txt_marks = Entry(self.root, textvariable=self.var_marks, font=("goudy old style", 20, "bold"), bg="lightyellow")
        txt_marks.place(x=280, y=280, width=320)

        txt_full_marks = Entry(
            self.root, textvariable=self.var_full_marks, font=("goudy old style", 20, "bold"), bg="lightyellow"
        )
        txt_full_marks.place(x=280, y=340, width=320)

        # ====== Buttons =======
        btn_add = Button(
            self.root, text="Submit", font=("times new roman", 15), bg="lightgreen", activebackground="lightgreen",
            cursor="hand2", command=self.add
        )
        btn_add.place(x=300, y=420, width=120, height=35)

        btn_clear = Button(
            self.root, text="Clear", font=("times new roman", 15), bg="lightgray", activebackground="lightgray",
            cursor="hand2", command=self.clear
        )
        btn_clear.place(x=450, y=420, width=120, height=35)

        # ====== Image =======
        try:
            self.bg_img = Image.open("images/result.jpg").resize((500, 300))
            self.bg_img = ImageTk.PhotoImage(self.bg_img)
            Label(self.root, image=self.bg_img).place(x=630, y=100)
        except Exception as ex:
            messagebox.showerror("Error", f"Image loading failed: {str(ex)}")

    # Fetch Roll Numbers from Database
    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()
            if rows:
                self.roll_list = [row[0] for row in rows]
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    # Search Student
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name, course FROM student WHERE roll = ?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    # Add Result to Database
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "Select" or not self.var_marks.get() or not self.var_full_marks.get():
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE roll = ?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row:
                    messagebox.showerror("Error", "Result already exists", parent=self.root)
                else:
                    percentage = (int(self.var_marks.get()) * 100) / int(self.var_full_marks.get())
                    cur.execute(
                        "INSERT INTO result (roll, name, course, marks_ob, full_marks, per) VALUES (?, ?, ?, ?, ?, ?)",
                        (
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_course.get(),
                            self.var_marks.get(),
                            self.var_full_marks.get(),
                            str(round(percentage, 2))
                        ),
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Result added successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    # Clear Fields
    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")


# Helper Function to Ensure Database and Tables Exist
def create_student_table():
    con = sqlite3.connect("rms.db")
    cur = con.cursor()
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS student (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                roll TEXT UNIQUE,
                name TEXT,
                course TEXT
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS result (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                roll TEXT UNIQUE,
                name TEXT,
                course TEXT,
                marks_ob INTEGER,
                full_marks INTEGER,
                per TEXT
            )
        """)
        con.commit()
    except Exception as ex:
        print(f"Error creating tables: {str(ex)}")
    finally:
        con.close()


if __name__ == "__main__":
    create_student_table()
    root = Tk()
    obj = resultClass(root)
    root.mainloop()

'''
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # pip install pillow
import sqlite3


class resultClass:
    
    def __init__(self, root):  # Constructor
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # ==== TITLE =====
        title = Label(self.root, text="Add Student Result", font=("goudy old style", 20, "bold"), bg="orange", fg="black")
        title.place(x=10, y=15, width=1180, height=50)

        
        # ====== Variables =======
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []
        self.fetch_roll()  # This should be properly recognized now
        
        # ====== Widgets =======
        lbl_select = Label(self.root, text="Select Student", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=100)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=160)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=220)
        lbl_marks_ob = Label(self.root, text="Marks Obtained", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=280)
        lbl_full_marks = Label(self.root, text="Full Marks", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=340)

        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list, font=("goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_student.place(x=280, y=100, width=200)
        self.txt_student.set("Select")

        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=500, y=100, width=100, height=28)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"), bg="lightyellow", state="readonly")
        txt_name.place(x=280, y=160, width=320)
        
        txt_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 20, "bold"), bg="lightyellow", state="readonly")
        txt_course.place(x=280, y=220, width=320)

        txt_marks = Entry(self.root, textvariable=self.var_marks, font=("goudy old style", 20, "bold"), bg="lightyellow")
        txt_marks.place(x=280, y=280, width=320)

        txt_full_marks = Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 20, "bold"), bg="lightyellow")
        txt_full_marks.place(x=280, y=340, width=320)

        # ====== Buttons =======
        btn_add = Button(self.root, text="Submit", font=("times new roman", 15), bg="lightgreen", activebackground="lightgreen", cursor="hand2", command=self.add)
        btn_add.place(x=300, y=420, width=120, height=35)

        btn_clear = Button(self.root, text="Clear", font=("times new roman", 15), bg="lightgray", activebackground="lightgray", cursor="hand2", command=self.clear)
        btn_clear.place(x=450, y=420, width=120, height=35)

        # ====== Image =======
        try:
            self.bg_img = Image.open("images/result.jpg").resize((500, 300))
            self.bg_img = ImageTk.PhotoImage(self.bg_img)
            Label(self.root, image=self.bg_img).place(x=630, y=100)
        except Exception as ex:
            messagebox.showerror("Error", f"Image loading failed: {str(ex)}")
    
    # Fetch Roll Numbers from Database
    
    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()
            if rows:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()
           

    # Search Student
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            
            cur.execute("SELECT name, course FROM student WHERE roll = ?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")#  initial
        finally:
            con.close()



    # Add Result to Database
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "Select" or not self.var_marks.get() or not self.var_full_marks.get():
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE roll = ?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row:
                    messagebox.showerror("Error", "Result already exists", parent=self.root)
                else:
                    percentage = (int(self.var_marks.get()) * 100) / int(self.var_full_marks.get())
                    cur.execute(
                        "INSERT INTO result (roll, name, course, marks_ob, full_marks, per) VALUES (?, ?, ?, ?, ?, ?)",
                        (
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_course.get(),
                            self.var_marks.get(),
                            self.var_full_marks.get(),
                            str(round(percentage, 2))
                        ),
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Result added successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    # Clear Fields
    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")


if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()
    '''
