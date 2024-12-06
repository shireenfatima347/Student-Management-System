from tkinter import *
from tkinter import messagebox

class ExitPage:
    def __init__(self, root, main_window):
        self.root = root
        self.main_window = main_window  # Reference to the main window
        self.root.title("Exit Confirmation")
        self.root.geometry("400x200+500+200")
        self.root.config(bg="white")
        
        # Message asking the user for confirmation to exit
        Label(self.root, text="Are you sure you want to exit?", font=("Arial", 15), bg="white").pack(pady=20)
        
        # Buttons for confirmation
        Button(self.root, text="Yes", font=("Arial", 12), bg="red", fg="white", command=self.confirm_exit).pack(side=LEFT, padx=20, pady=10)
        Button(self.root, text="No", font=("Arial", 12), bg="green", fg="white", command=self.cancel_exit).pack(side=RIGHT, padx=20, pady=10)

    def confirm_exit(self):
        # Close the application if the user confirms
        self.root.destroy()  # Close the exit confirmation window
        self.main_window.destroy()  # Close the main application window

    def cancel_exit(self):
        # Close the exit confirmation window and return to the main app
        self.root.destroy()


# In your main RMS class, you would call this ExitPage when clicking the "Exit" button.
class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # ====Menu=====
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=80)

        # Exit Button
        Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2", command=self.exit_application).place(x=1120, y=5, width=200, height=40)

    def exit_application(self):
        # Call ExitPage to display confirmation dialog
        self.new_win = Toplevel(self.root)
        self.exit_page = ExitPage(self.new_win, self.root)  # Pass the main window to ExitPage


if __name__ == "__main__":
    root = Tk()
    app = RMS(root)
    root.mainloop()
