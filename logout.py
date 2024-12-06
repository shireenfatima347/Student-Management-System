#===========LOGOUT=================
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from course import CourseClass
from report import reportClass
from RESULT import resultClass
from student import studentClass
from resultview import reportClass

# Ensure student.py exists and is implemented.

class RMS:
    def __init__(self, root):  # Constructor
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Get the directory of the script for robust path handling
        self.script_dir = os.path.dirname(__file__)

        # ====icons====
        logo_path = os.path.join(self.script_dir, "images", "logo_p.png")
        if os.path.exists(logo_path):
            self.logo_dash = ImageTk.PhotoImage(file=logo_path)
        else:
            self.logo_dash = None
            messagebox.showerror("Error", f"Image file not found: {logo_path}")

        # ====TITLE=====
        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT,
                      image=self.logo_dash, font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # ====Menu=====
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=80)

        Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2", command=self.add_course).place(x=20, y=5, width=200, height=40)
        Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2",command=self.add_student).place(x=240, y=5, width=200, height=40)
        Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2",command=self.add_result).place(x=460, y=5, width=200, height=40)
        Button(M_Frame, text="View student result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2",command=self.add_report).place(x=680, y=5, width=200, height=40)
        
        # Button for Logout
        Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2", command=self.logout).place(x=900, y=5, width=200, height=40)

        Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2").place(x=1120, y=5, width=200, height=40)

        # ====Content window=====
        bg_path = os.path.join(self.script_dir, "images", "bg.png")
        if os.path.exists(bg_path):
            self.bg_img = Image.open(bg_path).resize((920, 350), Image.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(self.bg_img)
            Label(self.root, image=self.bg_img).place(x=400, y=180, width=920, height=350)
        else:
            messagebox.showerror("Error", f"Background image file not found: {bg_path}")

        # ====Update details====
        self.lbl_course = Label(self.root, text="Total Courses\n[0]", font=("goudy old style", 20), bd=10,
                                relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Students\n[0]", font=("goudy old style", 20), bd=10,
                                 relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[0]", font=("goudy old style", 20), bd=10,
                                relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        # ====Footer=====
        footer = Label(self.root, text="SRMS - Student Result Management System", font=("goudy old style", 15),
                       bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def add_course(self):
        # Open the Course Management window
        self.new_win = Toplevel(self.root)
        self.new_object = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def logout(self):
        # Ask for confirmation before logging out
        response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if response == True:
            self.root.destroy()  # Closes the current window (logs out)
            messagebox.showinfo("Logged Out", "You have been successfully logged out.")
            # Optionally, you can call a login window here if you want to re-direct to the login page
            # login_window()  # Uncomment and define if you have a login screen.

    def update_details(self):
        # Placeholder for dynamic updating of details (replace with actual logic)
        courses = 10
        students = 50
        results = 30

        self.lbl_course.config(text=f"Total Courses\n[{courses}]")
        self.lbl_student.config(text=f"Total Students\n[{students}]")
        self.lbl_result.config(text=f"Total Results\n[{results}]")
        self.root.update()


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
