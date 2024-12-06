#==============================COURSE================================
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import sqlite3
import os

class CourseClass:
    def __init__(self, root):  # Constructor
        self.root = root
        self.root.title("Manage Course Details")       # Corrected the geometry format: widthxheight+x_offset+y_offset
        self.root.geometry("1200x480+8+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #======TITLE=========
        title = Label(self.root, text="Manage Course Details", font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        #====variables=======
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        #=======widgets======
        lbl_courseName = Label(self.root, text="Course Name", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=60)
        lbl_duration = Label(self.root, text="Duration", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=100)
        lbl_charges = Label(self.root, text="Charges", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=140)
        lbl_description = Label(self.root, text="Description", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=180)

        #=====entry fiels=====
        self.txt_courseName = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.txt_courseName.place(x=150, y=60, width=200)
        
        txt_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        txt_duration.place(x=150, y=100, width=200)
        
        txt_charges = Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        txt_charges.place(x=150, y=140, width=200)
        
        self.txt_description = Text(self.root, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.txt_description.place(x=150, y=180, width=500, height=100)
        
        #======buttons========
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        
        
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        #=======search panel========
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Course Name",font=("goudy old style",15, 'bold')).place(x=670, y=60, width=180)
        txt_search_courseName = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, 'bold'), bg='lightyellow').place(x=870, y=60, width=180)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28) 

        #========content===========
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)
        
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charges","description"),yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        
        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Course Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable["show"]='headings'

        self.CourseTable.column("cid",width=50)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=150)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#=================================
  
        
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.set("1.0",END)
        self.var_courseName.config(state=NORMAL)
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","course name should be required",parent=self.root)
            else:
                '''cur.execute("select *from course where name=",(self.var_course.get(),))
                row=cur.fetchone()'''
                cur.execute("select * from course where name=?", (self.var_course.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","please select course fronm the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete fro course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","course deleted successsfully",parent=self.root)
                        self.clear()
                        
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def get_data(self,ev):
        self.txt_courseName.conflict(state='readonly()')
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        #self.var_description.set(row[4])
        self.txt_description.delete("1.0",END)
        self.txt_description.insert(END,row[4])
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","course name should be required",parent=self.root)
            else:
                '''cur.execute("select *from course where name=",(self.var_course.get(),))
                row=cur.fetchone()'''
                cur.execute("select * from course where name=?", (self.var_course.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","course name alread availiable",parent=self.root)
                else:
                    cur.execute("insert into course(name,duration,charges,description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END)
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")
    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","course name should be required",parent=self.root)
            else:
                '''cur.execute("select *from course where name=",(self.var_course.get(),))
                row=cur.fetchone()'''
                cur.execute("select * from course where name=?", (self.var_course.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","select course from list",parent=self.root)
                else:
                    cur.execute("update into course set duration=?,charges=?,description=? where  name=?",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END),
                        self.var_course.get()
                        
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Course updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")
    

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            # Check if courses exist in the database
            cur.execute("SELECT * FROM course")
            rows = cur.fetchall()

            # If rows are empty, show a message and return
            if not rows:
                messagebox.showinfo("No Data", "No courses found in the database.", parent=self.root)
                return

            # Clear previous data and insert new data
            self.CourseTable.delete(*self.CourseTable.get_children())
            
            for row in rows:
                self.CourseTable.insert('', 'end', values=row)  # Insert each row into the table

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)


    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            
            cur.execute("select *from course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)                    
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")




        
        
if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
