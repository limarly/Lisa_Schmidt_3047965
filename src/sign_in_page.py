import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox


# Function to show a warning message for failed login
def failed_log_in():
    tk.messagebox.showwarning("Warning!", "Only for illustrative purposes!\nPlease sign up")


# Function to create the sign-in page
def create_sign_in_page(root, switch_page):
    frame = tk.Frame(root)
    frame.pack()

    img = Image.open('src/images/phone.png').resize((490, 875), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(frame, image=pic)
    Lab.image = pic
    Lab.pack()

    app_title = Image.open('src/images/logo_fc1.png')
    app_title = app_title.resize((290, 290), Image.LANCZOS)
    app_title_image = ImageTk.PhotoImage(app_title)
    app_title_label = tk.Label(frame, image=app_title_image, border=0)
    app_title_label.image = app_title_image
    app_title_label.place(x=100, y=90)

    # Username entry field
    username_entry = tk.Entry(frame,
                              font="Bahnschrift 15",
                              fg="#000000",
                              bg="#ffffff",
                              width=20,
                              border=0
                              )
    username_entry.place(x=185, y=430)

    # Username label
    username_label = tk.Label(frame, text="Username:",
                              font="Bahnschrift 18",
                              fg="#ffffff",
                              bg="#56DAE4")
    username_label.place(x=90, y=430)

    # Password entry field
    password_entry = tk.Entry(frame,
                              font="Bahnschrift 15",
                              fg="#000000",
                              bg="#ffffff",
                              width=20,
                              border=0
                              )
    password_entry.place(x=185, y=490)

    # Pasword label
    password_label = tk.Label(frame, text="Password:",
                              font="Bahnschrift 18",
                              fg="#ffffff",
                              bg="#56DAE4")
    password_label.place(x=90, y=490)

    # Login button
    login_button = tk.Button(frame, text="Log in",
                             font="impact 30 italic bold",
                             fg="#56DAE4",
                             bg="#ffffff",
                             width=15,
                             border=0,
                             command=failed_log_in)
    login_button.place(x=105, y=600)

    # "Or" label
    or_label = tk.Label(frame, text="----------- or -----------",
                        font="Bahnschrift 18",
                        fg="#ffffff",
                        bg="#56DAE4")
    or_label.place(x=150, y=655)

    # Sign up button
    sign_up_button = tk.Button(frame, text="Sign up",
                               font="impact 30 italic bold",
                               fg="#56DAE4",
                               bg="#ffffff",
                               width=15,
                               border=0,
                               command=lambda: switch_page(frame, 'sign_up'))
    sign_up_button.place(x=105, y=700)