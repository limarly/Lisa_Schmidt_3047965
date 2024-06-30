import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from src.helpers import save_profile_information, display_buttons


def create_profile_settings(root, switch_page):
    frame = tk.Frame(root)
    frame.pack()

    img = Image.open('src/images/phone.png').resize((490, 875), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(frame, image=pic)
    Lab.image = pic
    Lab.pack()

    # StringVars to store user input for personal description and current mood link
    personal_description = tk.StringVar()
    current_mood_link = tk.StringVar()

    # Function to proceed to the next page and save profile information
    def proceed_to_next_page(frame, target_page):
        save_profile_information(personal_description.get(), current_mood_link.get())
        switch_page(frame, target_page)

    profile_settings_label = tk.Label(frame, text="Settings", font="impact 40 italic bold", fg="#ffffff", bg="#56DAE4")
    profile_settings_label.place(x=185, y=75)

    # Label and entry for personal description
    personal_description_explanation = tk.Label(frame,
                                                text="Provide a description about yourself to\nlet others get to know "
                                                     "you better!",
                                                font="Bahnschrift 15",
                                                fg="#ffffff",
                                                bg="#56DAE4",
                                                anchor="nw",
                                                justify="left"
                                                )
    personal_description_explanation.place(x=100, y=200)

    personal_description_entry = tk.Entry(frame,
                                          font="Bahnschrift 15",
                                          textvariable=personal_description,
                                          fg="#000000",
                                          bg="#ffffff",
                                          width=25,
                                          border=0)
    personal_description_entry.place(x=100, y=250)

    # Label and entry for current mood link
    personal_description_explanation = tk.Label(frame,
                                                text="Provide a link to a song that\nrepresents your current mood!",
                                                font="Bahnschrift 15",
                                                fg="#ffffff",
                                                bg="#56DAE4",
                                                anchor="nw",
                                                justify="left"
                                                )
    personal_description_explanation.place(x=100, y=400)

    current_mood_link_entry = tk.Entry(frame,
                                       font="Bahnschrift 15",
                                       textvariable=current_mood_link,
                                       fg="#000000",
                                       bg="#ffffff",
                                       width=25,
                                       border=0,
                                       )
    current_mood_link_entry.place(x=100, y=450)

    # Button to save profile information and switch back to profile page
    back_to_profile = tk.Button(frame,
                                text="Save and back to Profile",
                                font="Bahnschrift 18 bold italic",
                                fg="#56DAE4",
                                bg="#ffffff",
                                width=18,
                                height=1,
                                border=0,
                                command=lambda: proceed_to_next_page(frame, 'profile'))
    back_to_profile.place(x=120, y=700)

    # Display navigation buttons (Channels, Post, Match, Profile)
    display_buttons(frame, switch_page)
