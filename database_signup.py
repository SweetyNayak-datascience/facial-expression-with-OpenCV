from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql


def clear():
    usernameEntry.delete(0, END)
    emailEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)

def register():
    username = usernameEntry.get()
    email = emailEntry.get()
    password = passwordEntry.get()
    confirm = confirmEntry.get()

    if username == "" or email == "" or password == "" or confirm == "":
        messagebox.showerror("Error", "All fields are required")
    elif password != confirm:
        messagebox.showerror("Error", "Passwords do not match")
    else:
       ''' try:
            # Connect to MySQL
            conn = pymysql.connect(
                host="localhost",
                user="your_username",         # e.g., 'root'
                password="your_password",     # your MySQL password
                database="users_db"
            )
            cursor = conn.cursor()

            # Insert data
            cursor.execute(
                "INSERT INTO register (username, email, password) VALUES (%s, %s, %s)",
                (username, email, password)
            )
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Registered successfully!")

            # Clear fields
            usernameEntry.delete(0, END)
            emailEntry.delete(0, END)
            passwordEntry.delete(0, END)
            confirmEntry.delete(0, END)

        except pymysql.err.IntegrityError:
            messagebox.showerror("Error", "Email already registered!")
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {str(e)}")
        finally:
            if 'conn' in locals() and conn.open:
                conn.close()    '''
import pymysql

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",        # change if needed
            password="",        # your MySQL password
            database="users_db"
        )
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM register WHERE username=%s AND password=%s",
            (username, password)
        )

        row = cursor.fetchone()

        if row:
            messagebox.showinfo("Success", "Login Successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password")

        conn.close()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))
