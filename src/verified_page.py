import tkinter as tk
from PIL import Image, ImageTk


def create_verified_page(root, switch_page):
    # Create a frame to hold all widgets of the welcome page
    frame = tk.Frame(root)
    frame.pack()

    # Load and display the background image
    img = Image.open('src/images/phone.png').resize((490, 875), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(frame, image=pic)
    Lab.image = pic
    Lab.pack()

    # Label for why verification is needed
    verified_label = tk.Label(frame, text="YOU'VE BEEN\nVERIFIED",
                              font="impact 65",
                              fg="#ffffff",
                              bg="#56DAE4")
    verified_label.place(x=90, y=220)

    # Verification check image
    check = Image.open('src/images/check_verification.png')
    check = check.resize((230, 230), Image.LANCZOS)
    check_image = ImageTk.PhotoImage(check)
    check_label = tk.Label(frame, image=check_image, border=0)
    check_label.image = check_image
    check_label.place(x=130, y=400)

    # Move on to the view the created profile
    networking = tk.Button(frame, text=">>  Start Networking",
                           font="Bahnschrift 25 bold",
                           fg="#56DAE4",
                           bg="#ffffff",
                           border=0,
                           height=2,
                           width=15,
                           command=lambda: switch_page(frame, 'profile'))
    networking.place(x=113, y=680)