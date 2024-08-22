import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

# Function to handle the login
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Basic validation (replace with actual validation logic)
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Function to close the application
def close_app():
    root.destroy()

# Create and place the username label and entry
label_username = tk.Label(root, text="Username")
label_username.pack(pady=10)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Create and place the password label and entry
label_password = tk.Label(root, text="Password")
label_password.pack(pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Create and place the login button
button_login = tk.Button(root, text="Login", command=login)
button_login.pack(pady=20)

# Create and place the exit button
button_exit = tk.Button(root, text="Exit", command=close_app)
button_exit.pack(pady=5)

# Run the main loop
root.mainloop()
import tkinter as tk
from tkinter import messagebox

# In-memory storage for users (username and password)
user_db = {}

# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Check if the username exists and password matches
    if username in user_db and user_db[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        show_main_interface()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Function to handle new account creation
def create_account():
    username = entry_new_username.get()
    password = entry_new_password.get()
    
    if username in user_db:
        messagebox.showerror("Error", "Username already exists!")
    else:
        user_db[username] = password
        messagebox.showinfo("Account Created", "Account created successfully! Please log in.")
        show_login_form()

# Function to display the account creation form
def show_create_account_form():
    clear_screen()

    tk.Label(root, text="Create New Account").pack(pady=10)
    
    global entry_new_username, entry_new_password
    tk.Label(root, text="New Username").pack(pady=5)
    entry_new_username = tk.Entry(root)
    entry_new_username.pack(pady=5)
    
    tk.Label(root, text="New Password").pack(pady=5)
    entry_new_password = tk.Entry(root, show="*")
    entry_new_password.pack(pady=5)
    
    tk.Button(root, text="Create Account", command=create_account).pack(pady=20)
    tk.Button(root, text="Back to Login", command=show_login_form).pack(pady=5)

# Function to display the main interface after login
def show_main_interface():
    clear_screen()
    
    tk.Label(root, text="Main Interface").pack(pady=20)
    
    tk.Button(root, text="Home", command=show_home).pack(pady=10)
    tk.Button(root, text="Profile", command=show_profile).pack(pady=10)
    tk.Button(root, text="Logout", command=show_login_form).pack(pady=10)

# Function to show the home screen
def show_home():
    messagebox.showinfo("Home", "This is the Home screen.")

# Function to show the profile screen
def show_profile():
    messagebox.showinfo("Profile", "This is the Profile screen.")

# Function to clear the screen
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

# Function to display the login form
def show_login_form():
    clear_screen()
    
    tk.Label(root, text="Login Form").pack(pady=10)
    
    global entry_username, entry_password
    tk.Label(root, text="Username").pack(pady=5)
    entry_username = tk.Entry(root)
    entry_username.pack(pady=5)
    
    tk.Label(root, text="Password").pack(pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)
    
    tk.Button(root, text="Login", command=login).pack(pady=20)
    tk.Button(root, text="Create New Account", command=show_create_account_form).pack(pady=5)

# Create the main window
root = tk.Tk()
root.title("User Login System")
root.geometry("300x300")

# Initialize with the login form
show_login_form()

# Run the main loop
root.mainloop()
