from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

# ----------------- Placeholder Clear Functions ----------------- #
def on_entry_click(entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, END)

# ----------------- Register Function ----------------- #
def register():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm = confirm_entry.get()

    if username == "" or email == "" or password == "" or confirm == "":
        messagebox.showerror("Error", "All fields are required")
    elif password != confirm:
        messagebox.showerror("Error", "Passwords do not match")
    else:
        messagebox.showinfo("Success", "Registered successfully!")

# ----------------- Window Setup ----------------- #
root = Tk()
root.title("Registration Page")
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

# ----------------- Registration Frame (RIGHT aligned) ----------------- #
reg_frame = Frame(root, bg="black", bd=2)
reg_frame.place(x=520, y=80, width=400, height=500)

# ----------------- Heading ----------------- #
Label(reg_frame, text="REGISTER", font=("Helvetica", 28, "bold"), fg="Firebrick1", bg="black").place(x=110, y=20)

# ----------------- Username Entry ----------------- #
username_entry = Entry(reg_frame, font=("Arial", 16), fg="Firebrick1", bg="black", bd=0, insertbackground='white')
username_entry.place(x=70, y=90, width=260, height=30)
username_entry.insert(0, "Username")
username_entry.bind("<FocusIn>", lambda e: on_entry_click(username_entry, "Username"))
Frame(reg_frame, bg="Firebrick1", height=2, width=260).place(x=70, y=120)

# ----------------- Email Entry ----------------- #
email_entry = Entry(reg_frame, font=("Arial", 16), fg="Firebrick1", bg="black", bd=0, insertbackground='white')
email_entry.place(x=70, y=140, width=260, height=30)
email_entry.insert(0, "Email")
email_entry.bind("<FocusIn>", lambda e: on_entry_click(email_entry, "Email"))
Frame(reg_frame, bg="Firebrick1", height=2, width=260).place(x=70, y=170)

# ----------------- Password Entry ----------------- #
password_entry = Entry(reg_frame, font=("Arial", 16), fg="Firebrick1", bg="black", bd=0, insertbackground='white')
password_entry.place(x=70, y=190, width=260, height=30)
password_entry.insert(0, "Password")
password_entry.bind("<FocusIn>", lambda e: on_entry_click(password_entry, "Password"))
Frame(reg_frame, bg="Firebrick1", height=2, width=260).place(x=70, y=220)

# ----------------- Confirm Password Entry ----------------- #
confirm_entry = Entry(reg_frame, font=("Arial", 16), fg="Firebrick1", bg="black", bd=0, insertbackground='white')
confirm_entry.place(x=70, y=240, width=260, height=30)
confirm_entry.insert(0, "Confirm Password")
confirm_entry.bind("<FocusIn>", lambda e: on_entry_click(confirm_entry, "Confirm Password"))
Frame(reg_frame, bg="Firebrick1", height=2, width=260).place(x=70, y=270)

# ----------------- Sign Up Button ----------------- #
Button(reg_frame, text="Sign Up", font=("Arial Rounded MT Bold", 16), bg="Firebrick1", fg="white",
       activebackground="#c0392b", activeforeground="white", bd=0, cursor="hand2", command=register)\
    .place(x=70, y=300, width=260, height=40)

# ----------------- OR separator ----------------- #
Frame(reg_frame, bg="lightgrey", height=1, width=260).place(x=70, y=360)
Label(reg_frame, text="OR", bg="black", fg="lightgrey", font=("Helvetica", 12, "bold")).place(x=185, y=350)

# ----------------- Already Have Account ----------------- #
Label(reg_frame, text="Already have an account?", font=("Helvetica", 12), fg="white", bg="black")\
    .place(x=70, y=380)

Button(reg_frame, text="Login", font=("Helvetica", 12, "bold"), fg="Firebrick1", bg="black",
       bd=0, cursor="hand2", activebackground="black", activeforeground="white")\
    .place(x=250, y=378)

root.mainloop()
