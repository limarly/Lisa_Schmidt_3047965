import tkinter as tk
from PIL import Image, ImageTk
from src.helpers import hide_tooltip, show_tooltip

# Create a global variable for the tooltip
tooltip = None


# Definition that checks if both checkboxes have been ticket
def check_if_both_checked(personal_id_var, student_id_var, button):
    if personal_id_var.get() == 1 and student_id_var.get() == 1:
        button.place(x=180, y=700)
    else:
        button.place_forget()


def create_get_verified_page(root, switch_page):
    frame = tk.Frame(root)
    frame.pack()

    img = Image.open('src/images/phone.png').resize((490, 875), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(frame, image=pic)
    Lab.image = pic
    Lab.pack()

    # Title for the page
    get_verified = tk.Label(frame, text="Get Verified",
                            font="impact 40 italic bold",
                            fg="#ffffff",
                            bg="#56DAE4")
    get_verified.place(x=140, y=75)

    question = Image.open('src/images/questionmark.png')
    question = question.resize((70, 70), Image.LANCZOS)
    question_image = ImageTk.PhotoImage(question)
    question_label = tk.Label(frame, image=question_image, border=0)
    question_label.image = question_image
    question_label.place(x=70, y=190)

    # Label for why is verification needed
    why_verification_label = tk.Label(frame, text="Why do I need to get verified?",
                                      font="impact 18",
                                      fg="#ffffff",
                                      bg="#56DAE4")
    why_verification_label.place(x=150, y=210)

    # Answer label for why verification is needed
    answer_label = tk.Label(frame,
                            text="This platform is currently only for\nfirst semesters who study "
                                 "at a\nGerman university. We want to\nensure a safe space "
                                 "for\nconnections and conversations \nwhere you can get to know "
                                 "your \nfellow students.",
                            font="Bahnschrift 14",
                            fg="#5B5C5E",
                            bg="#ffffff",
                            borderwidth=2,
                            relief="solid")
    answer_label.place(x=150, y=250)

    # Theoretical button to upload a picture of your personal ID
    personal_id_pic = Image.open('src/images/upload.png')
    personal_id_pic = personal_id_pic.resize((60, 60), Image.LANCZOS)
    personal_id_pic_image = ImageTk.PhotoImage(personal_id_pic)
    personal_id_pic_label = tk.Label(frame, image=personal_id_pic_image, border=0)
    personal_id_pic_label.image = personal_id_pic_image
    personal_id_pic_label.place(x=80, y=425)

    # Label for personal ID
    personal_id_label = tk.Label(frame, text="Upload a Picture of your Personal ID",
                                 font="impact 18",
                                 fg="#ffffff",
                                 bg="#56DAE4")
    personal_id_label.place(x=150, y=440)

    # Bind the tooltip to the personal_id_pic_label
    personal_id_label.bind("<Enter>", lambda event: show_tooltip(event, "Tick the box below to confirm your upload"))
    personal_id_label.bind("<Leave>", hide_tooltip)

    # Checkbox to mimic an upload and actual check of the ID
    personal_id_var = tk.IntVar()
    personal_id_tickbox = tk.Checkbutton(frame, text="uploaded",
                                         font="Bahnschrift 14",
                                         fg="#ffffff",
                                         bg="#56DAE4",
                                         variable=personal_id_var,
                                         command=lambda: check_if_both_checked(personal_id_var, student_id_var,
                                                                               get_ver_next))
    personal_id_tickbox.place(x=155, y=475)

    # Theoretical button to upload a picture of your student ID
    student_id_pic = Image.open('src/images/upload.png')
    student_id_pic = student_id_pic.resize((60, 60), Image.LANCZOS)
    student_id_pic_image = ImageTk.PhotoImage(student_id_pic)
    student_id_pic_label = tk.Label(frame, image=student_id_pic_image, border=0)
    student_id_pic_label.image = student_id_pic_image
    student_id_pic_label.place(x=80, y=575)

    # Label for student ID
    student_id_label = tk.Label(frame, text="Upload a Picture of your Student ID",
                                font="impact 18",
                                fg="#ffffff",
                                bg="#56DAE4")
    student_id_label.place(x=150, y=590)

    # Bind the tooltip to the personal_id_pic_label
    student_id_label.bind("<Enter>", lambda event: show_tooltip(event, "Tick the box below to confirm your upload"))
    student_id_label.bind("<Leave>", hide_tooltip)

    # Checkbox to mimic an upload and actual check of the ID
    student_id_var = tk.IntVar()
    student_id_tickbox = tk.Checkbutton(frame, text="uploaded",
                                        font="Bahnschrift 14",
                                        fg="#ffffff",
                                        bg="#56DAE4",
                                        variable=student_id_var,
                                        command=lambda: check_if_both_checked(personal_id_var, student_id_var,
                                                                              get_ver_next))
    student_id_tickbox.place(x=155, y=625)

    # Button to move on to get verified page (initially hidden)
    get_ver_next = tk.Button(frame, text=f">>  Next",
                             font="Bahnschrift 25 bold italic",
                             fg="#56DAE4",
                             bg="#ffffff",
                             width=6,
                             height=1,
                             border=0,
                             command=lambda: switch_page(frame, 'verified'))
    get_ver_next.place(x=180, y=700)
    get_ver_next.place_forget()  # Hide the button initially
