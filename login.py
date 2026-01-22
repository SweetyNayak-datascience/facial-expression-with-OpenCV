from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

def on_username_click(event):
    if username_entry.get() == "Username":
        username_entry.delete(0, END)

def on_password_click(event):
    if password_entry.get() == "password":
        password_entry.delete(0, END)
        password_entry.config(show="*")

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Success", "Login successful!")
    elif username == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        messagebox.showerror("Error", "Invalid credentials")

# ----------------- Window Setup ----------------- #
root = Tk()
root.title("Login Page")
root.geometry("990x660+100+50")
root.resizable(False, False)

# ----------------- Background Image ----------------- #
url = "https://www.hak4kidz.com/images/ai_child.jpeg"
response = requests.get(url)
bgImage = Image.open(BytesIO(response.content))
bgImage = bgImage.resize((990, 660), Image.Resampling.LANCZOS)
bgPhoto = ImageTk.PhotoImage(bgImage)

bgLabel = Label(root, image=bgPhoto)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

# ----------------- Login Frame (RIGHT aligned) ----------------- #
login_frame = Frame(root, bg="black", bd=2)
login_frame.place(x=520, y=120, width=400, height=420)

# ----------------- Heading ----------------- #
Label(login_frame, text="USER LOGIN", font=("Helvetica", 28, "bold"), fg="Firebrick1", bg="black").place(x=100, y=30)

# ----------------- Username Entry ----------------- #
username_entry = Entry(login_frame, font=("Arial", 16), fg="Firebrick1", bg="black", bd=0, insertbackground='white')
username_entry.place(x=70, y=100, width=260, height=30)
username_entry.insert(0, "Username")
username_entry.bind("<FocusIn>", on_username_click)
Frame(login_frame, bg="Firebrick1", height=2, width=260).place(x=70, y=130)

# ----------------- Password Entry ----------------- #
password_entry = Entry(login_frame, font=("Arial", 16), fg="Firebrick1", bg="black", bd=0, insertbackground='white')
password_entry.place(x=70, y=160, width=260, height=30)
password_entry.insert(0, "password")
password_entry.bind("<FocusIn>", on_password_click)
Frame(login_frame, bg="Firebrick1", height=2, width=260).place(x=70, y=190)

# ----------------- Login Button ----------------- #
Button(login_frame, text="Log In", font=("Arial Rounded MT Bold", 16), bg="Firebrick1", fg="white",
       activebackground="#c0392b", activeforeground="white", bd=0, cursor="hand2", command=login)\
    .place(x=70, y=230, width=260, height=40)

# ----------------- OR separator ----------------- #
Frame(login_frame, bg="lightgrey", height=1, width=260).place(x=70, y=290)
Label(login_frame, text="OR", bg="black", fg="lightgrey", font=("Helvetica", 12, "bold")).place(x=185, y=280)

# ----------------- Forgot Password ----------------- #
Button(login_frame, text="Forgot Password?", font=("Helvetica", 11), bg="black", fg="Firebrick1",
       activebackground="black", activeforeground="white", bd=0, cursor="hand2")\
    .place(x=120, y=310)

# ----------------- Register Section ----------------- #
register_frame = Frame(login_frame, bg="black")
register_frame.place(x=0, y=350, width=400, height=60)

Label(register_frame, text="Don't have an account?", font=("Helvetica", 12), fg="white", bg="black")\
    .place(x=80, y=15)

Button(register_frame, text="Register", font=("Helvetica", 12, "bold"), fg="Firebrick1", bg="black",
       bd=0, cursor="hand2", activebackground="black", activeforeground="white")\
    .place(x=250, y=13)
def open_register():
    import os
    import sys
    import subprocess
    # Try to open register.py using the same Python interpreter
    register_file = os.path.join(os.path.dirname(__file__), "register.py")
    if os.path.exists(register_file):
        # For Windows or if GUI should be new process:
        subprocess.Popen([sys.executable, register_file])
    else:
        from tkinter import messagebox
        messagebox.showerror("Error", "register.py not found!")

Button(register_frame, text="Register", font=("Helvetica", 12, "bold"), fg="Firebrick1", bg="black",
       bd=0, cursor="hand2", activebackground="black", activeforeground="white", command=open_register)\
    .place(x=250, y=13)


root.mainloop()
