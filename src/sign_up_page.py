import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from src.helpers import save_user_information, show_tooltip, hide_tooltip
from tkinter import filedialog
import cv2

# Global variable to store the uploaded image
uploaded_image = None
panelA = None  # Initialize panelA as None


# Function to upload a profile picture
# Reference: https://medium.com/@abhishiktadhar111/exploring-image-processing-through-python-and-tkinter-440b389e5e53
# #:~:text=Uploading%20image,image%20in%20a%20Tkinter%20GUI.&text=The%20function%20opens%20a%20file,
# file%20types%20to%20JPEG%20(%20*.
def upload_profile_pic(frame):
    global panelA, uploaded_image
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]  # File types allowed
    path = filedialog.askopenfilename(filetypes=f_types)  # Open file dialog to select an image
    print(f"Selected path: {path}")  # Debugging print

    if path:
        # Read and process the image using OpenCV
        image = cv2.imread(path)
        if image is None:
            print(f"Failed to load image from {path}")
            return

        image = cv2.resize(image, (120, 160), Image.LANCZOS)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Convert to PIL format and then to ImageTk format
        image_pil = Image.fromarray(image)
        image_tk = ImageTk.PhotoImage(image_pil)

        # Store the uploaded image in a global variable
        uploaded_image = image

        # Update or create the image panel
        if panelA:
            panelA.config(image=image_tk)
            panelA.image = image_tk
        else:
            panelA = tk.Label(frame, image=image_tk)
            panelA.image = image_tk
            panelA.place(x=185, y=130)


# Global variables to store selected items
selected_interests = []
selected_universities = []
selected_courses = []


# Function to check if the date is in a valid format (YYYY-MM-DD)
def is_valid_date_format(date_str):
    try:
        year, month, day = map(int, date_str.split('-'))
        # Check if it's a valid date
        if 1 <= month <= 12 and 1 <= day <= 31:
            return True
    except ValueError:
        return False
    return False


# Function to check the validity of the date of birth
def check_date_of_birth(dob):
    if not is_valid_date_format(dob.get()):
        messagebox.showerror("Invalid Date", "Please enter a valid date in the format YYYY-MM-DD")
        return False
    return True


# Function to create the sign-up page
def create_sign_up_page(root, switch_page):
    global interests_listbox
    frame = tk.Frame(root)
    frame.pack()

    img = Image.open('src/images/phone.png').resize((490, 875), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(frame, image=pic)
    Lab.image = pic
    Lab.pack()

    # StringVars to hold input data
    username = tk.StringVar()
    birthday = tk.StringVar()
    password = tk.StringVar()
    last_name = tk.StringVar()
    first_name = tk.StringVar()

    # Function to toggle the visibility of the interests listbox
    def toggle_interests_listbox():
        if interests_listbox.winfo_ismapped():
            interests_listbox.place_forget()  # Hide the interests listbox if it's visible
        else:
            interests_listbox.place(x=185, y=412)  # Show the interests listbox if it's hidden
            interests_listbox.lift()

    # Function to toggle the visibility of the universities listbox
    def toggle_universities_listbox():
        if universities_listbox.winfo_ismapped():
            universities_listbox.place_forget()  # Hide the universities listbox if it's visible
        else:
            universities_listbox.place(x=185, y=528)  # Show the universities listbox if it's hidden
            universities_listbox.lift()

    # Function to toggle the visibility of the courses listbox
    def toggle_courses_listbox():
        if courses_listbox.winfo_ismapped():
            courses_listbox.place_forget()  # Hide the courses listbox if it's visible
        else:
            courses_listbox.place(x=185, y=593)  # Show the courses listbox if it's hidden
            courses_listbox.lift()

    # Function to handle selection of interests
    def on_interests_select(event):
        global selected_interests
        new_selection = [interests_listbox.get(idx) for idx in interests_listbox.curselection()]
        for item in new_selection:
            if item not in selected_interests:
                selected_interests.append(item)
        update_selected_interests_label()

    # Function to handle selection of universities
    def on_universities_select(event):
        global selected_universities
        new_selection = [universities_listbox.get(idx) for idx in universities_listbox.curselection()]
        for item in new_selection:
            if item not in selected_universities:
                selected_universities.clear()
                selected_universities.append(item)
        update_selected_universities_label()

    # Function to handle selection of courses
    def on_courses_select(event):
        global selected_courses
        new_selection = [courses_listbox.get(idx) for idx in courses_listbox.curselection()]
        for item in new_selection:
            if item not in selected_universities:
                selected_courses.clear()
                selected_courses.append(item)
        update_selected_courses_label()

    # Function to update the label displaying selected interests
    def update_selected_interests_label():
        selected_interests_label = tk.Label(frame, font="Bahnschrift 15", fg="#ffffff", bg="#56DAE4")
        selected_interests_label.place(x=185, y=530)
        selected_interests_label.config(text=", ".join(selected_interests))

    # Function to update the label displaying selected universities
    def update_selected_universities_label():
        selected_universities_label = tk.Label(frame, font="Bahnschrift 15", fg="#ffffff", bg="#56DAE4")
        selected_universities_label.place(x=185, y=595)
        selected_universities_label.config(text=" ".join(selected_universities))

    def update_selected_courses_label():
        # Selected Courses Label
        selected_courses_label = tk.Label(frame, font="Bahnschrift 15", fg="#ffffff", bg="#56DAE4")
        selected_courses_label.place(x=185, y=660)
        selected_courses_label.config(text=" ".join(selected_courses))

    # Function to check if all required fields are filled
    def check_all_fields_filled():
        if first_name.get() and last_name.get() and birthday.get() and username.get() and password.get() and \
                selected_interests and selected_universities and selected_courses:
            return True
        else:
            return False

    # Function to proceed to the next page after validation
    def proceed_to_next_page(frame, target_page, dob):
        if check_date_of_birth(dob):
            if check_all_fields_filled():
                switch_page(frame, target_page)
                save_user_information(first_name.get(), last_name.get(), birthday.get(), username.get(), password.get(),
                                      selected_interests, selected_universities, selected_courses)
            else:
                tk.messagebox.showwarning("Important",
                                          "Please fill out all the information so we can create your profile.")

    profile_pic_placeholder = Image.open('src/images/profile_pic_placeholder.png')
    profile_pic_placeholder = profile_pic_placeholder.resize((130, 130), Image.LANCZOS)
    profile_pic_placeholder_image = ImageTk.PhotoImage(profile_pic_placeholder)
    profile_pic_placeholder_label = tk.Label(frame, image=profile_pic_placeholder_image, border=0)
    profile_pic_placeholder_label.place(x=180, y=140)

    # Button to upload the profile picture
    upload_button = tk.Button(frame, text="Upload",
                              font="Bahnschrift 15 bold",
                              fg="#56DAE4",
                              bg="#ffffff",
                              border=0,
                              height=1,
                              width=5,
                              command=lambda: upload_profile_pic(frame))
    upload_button.place(x=200, y=190)

    # create a title for the page
    sign_up_label = tk.Label(frame, text="Sign up",
                             font="impact 40 italic bold",
                             fg="#ffffff",
                             bg="#56DAE4"
                             )
    sign_up_label.place(x=180, y=75)

    first_name_label = tk.Label(frame, text="First Name",
                                font="Bahnschrift 18",
                                fg="#ffffff",
                                bg="#56DAE4"
                                )
    first_name_label.place(x=90, y=300)

    # Input field for First Name
    first_name_entry = tk.Entry(frame,
                                textvariable=first_name,
                                font="Bahnschrift 15",
                                fg="#000000",
                                bg="#ffffff",
                                width=20,
                                border=0
                                )
    first_name_entry.place(x=185, y=300)

    last_name_label = tk.Label(frame, text="Last Name",
                               font="Bahnschrift 18",
                               fg="#ffffff",
                               bg="#56DAE4"
                               )
    last_name_label.place(x=90, y=340)

    # Input field for Last Name
    last_name_entry = tk.Entry(frame,
                               textvariable=last_name,
                               font="Bahnschrift 15",
                               fg="#000000",
                               bg="#ffffff",
                               width=20,
                               border=0
                               )
    last_name_entry.place(x=185, y=340)

    birthday_label = tk.Label(frame, text="Birthday",
                              font="Bahnschrift 18",
                              fg="#ffffff",
                              bg="#56DAE4"
                              )
    birthday_label.place(x=90, y=380)

    # Input field for birthday
    birthday_entry = tk.Entry(frame,
                              textvariable=birthday,
                              font="Bahnschrift 15",
                              fg="#000000",
                              bg="#ffffff",
                              width=20,
                              border=0
                              )
    birthday_entry.place(x=185, y=380)

    birthday_entry.bind("<Enter>", lambda event: show_tooltip(event, "Please use the format YYYY-MM-DD"))
    birthday_entry.bind("<Leave>", hide_tooltip)

    # input username
    username_entry = tk.Entry(frame,
                              textvariable=username,
                              font="Bahnschrift 15",
                              fg="#000000",
                              bg="#ffffff",
                              width=20,
                              border=0
                              )
    username_entry.place(x=185, y=420)

    username_label = tk.Label(frame, text="Username",
                              font="Bahnschrift 18",
                              fg="#ffffff",
                              bg="#56DAE4")
    username_label.place(x=90, y=420)

    # input password
    password_entry = tk.Entry(frame,
                              textvariable=password,
                              font="Bahnschrift 15",
                              fg="#000000",
                              bg="#ffffff",
                              width=20,
                              border=0
                              )
    password_entry.place(x=185, y=460)

    password_label = tk.Label(frame, text="Password",
                              font="Bahnschrift 18",
                              fg="#ffffff",
                              bg="#56DAE4")
    password_label.place(x=90, y=460)

    # Provide Interests
    interests_label = tk.Label(frame, text="Interest",
                               font="Bahnschrift 18",
                               fg="#ffffff",
                               bg="#56DAE4")
    interests_label.place(x=90, y=500)

    # Interests listbox
    interests_listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE, fg="#5B5C5E", bg="#ffffff",
                                   selectbackground="#56DAE4",
                                   height=5)
    # interests_listbox.place(x=185, y=412) # Hide provided selection at the start
    for item in ["Art", "AStA", "Initiatives", "Sport", "Music"]:
        interests_listbox.insert(tk.END, item)
    interests_listbox.bind("<<ListboxSelect>>", on_interests_select)

    # Choose Interests Button
    choose_interests_button = tk.Button(frame, text="Choose Interests",
                                        font="Bahnschrift 17",
                                        fg="#5B5C5E",
                                        bg="#ffffff",
                                        width=16,
                                        border=0,
                                        command=toggle_interests_listbox)
    choose_interests_button.place(x=185, y=500)

    # Provide Universities
    universities_label = tk.Label(frame, text="University",
                                  font="Bahnschrift 18",
                                  fg="#ffffff",
                                  bg="#56DAE4")
    universities_label.place(x=90, y=565)

    # Universities listbox
    universities_listbox = tk.Listbox(frame, selectmode=tk.SINGLE, fg="#5B5C5E", bg="#ffffff",
                                      selectbackground="#56DAE4",
                                      height=2)
    # universities_listbox.place(x=185, y=613) # Hide provided selection at the start
    for item in ["Leuphana University", "Hamburg Media School"]:
        universities_listbox.insert(tk.END, item)
    universities_listbox.bind("<<ListboxSelect>>", on_universities_select)

    # Choose Universities Button
    choose_universities_button = tk.Button(frame, text="Choose Universities",
                                           font="Bahnschrift 17",
                                           fg="#5B5C5E",
                                           bg="#ffffff",
                                           width=16,
                                           border=0,
                                           command=toggle_universities_listbox)
    choose_universities_button.place(x=185, y=565)

    # Provide Courses
    courses_label = tk.Label(frame, text="Course:",
                             font="Bahnschrift 18",
                             fg="#ffffff",
                             bg="#56DAE4")
    courses_label.place(x=90, y=630)

    # courses listbox
    courses_listbox = tk.Listbox(frame, selectmode=tk.SINGLE, fg="#5B5C5E", bg="#ffffff", selectbackground="#56DAE4",
                                 height=2)
    # courses_listbox.place(x=185, y=613) # Hide provided selection at the start
    for item in ["Digital Media", "Business Administration"]:
        courses_listbox.insert(tk.END, item)
    courses_listbox.bind("<<ListboxSelect>>", on_courses_select)

    # Choose courses Button
    choose_courses_button = tk.Button(frame, text="Choose Course",
                                      font="Bahnschrift 17",
                                      fg="#5B5C5E",
                                      bg="#ffffff",
                                      width=16,
                                      border=0,
                                      command=toggle_courses_listbox)
    choose_courses_button.place(x=185, y=630)

    # move on to the next page
    create_profile = tk.Button(frame, text=">>  Create Profile",
                               font="Bahnschrift 20 bold",
                               fg="#56DAE4",
                               bg="#ffffff",
                               border=0,
                               height=2,
                               width=15,
                               command=lambda: proceed_to_next_page(frame, 'get_verified', birthday))
    create_profile.place(x=125, y=700)
