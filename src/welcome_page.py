import tkinter as tk
from PIL import Image, ImageTk


# Function to create the welcome page
def create_welcome_page(root, switch_page):
    # Create a frame to hold all widgets of the welcome page
    frame = tk.Frame(root)
    frame.pack()

    # Load and display the background image
    img = Image.open('src/images/phone.png').resize((490, 875), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(frame, image=pic)
    Lab.image = pic
    Lab.pack()

    # Create and place a welcome message label
    welcome = tk.Label(frame, text="Welcome to",
                       font="impact 45 italic bold",
                       fg="#ffffff",
                       bg="#56DAE4")
    welcome.place(x=130, y=100)

    # Load and display the application title image (logo)
    app_title = Image.open('src/images/logo_fc1.png')
    app_title = app_title.resize((250, 250), Image.LANCZOS)
    app_title_image = ImageTk.PhotoImage(app_title)
    app_title_label = tk.Label(frame, image=app_title_image, border=0)
    app_title_label.image = app_title_image
    app_title_label.place(x=124, y=180)

    # Create and place an explanation label
    explanation = tk.Label(frame, text="Get to know other first semesters\n from all over germany.\n Ask other students"
                                       "to join you\n for activities and share your\n knowledge and questions during\n "
                                       "your first semester at university!",
                           font="Bahnschrift 20",
                           fg="#000000",
                           bg="#ffffff",
                           height=7,
                           width=26,
                           borderwidth=2,
                           relief="solid")
    explanation.place(x=75, y=450)

    # Create and place a "Get connected" button
    get_connected = tk.Button(frame, text=">> Get connected",
                              font="Bahnschrift 25 bold italic",
                              fg="#56DAE4",
                              bg="#ffffff",
                              width=16,
                              height=2,
                              border=0,
                              command=lambda: switch_page(frame, 'sign_in'))
    get_connected.place(x=104, y=700)
