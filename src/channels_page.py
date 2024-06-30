import tkinter as tk
from PIL import Image, ImageTk
from src.helpers import get_user_data, display_buttons


def create_channels_page(root, switch_page):
    frame = tk.Frame(root)
    frame.pack()

    img = Image.open('src/images/phone.png').resize((490, 875), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(frame, image=pic)
    Lab.image = pic
    Lab.pack()

    # Display navigation buttons (Channels, Post, Match, Profile)
    display_buttons(frame, switch_page)

    # Get user data from helpers
    user_data = get_user_data()
    selected_courses = " ".join(user_data['selected_courses'])
    selected_universities = " ".join(user_data['selected_universities'])

    # title for the page
    profile = tk.Label(frame, text="Channels",
                       font="impact 40 italic bold",
                       fg="#ffffff",
                       bg="#56DAE4")
    profile.place(x=165, y=75)

    # searchbar
    search_label = tk.Label(frame, text="Search",
                            font="Bahnschrift 20",
                            fg="#ffffff",
                            bg="#56DAE4")
    search_label.place(x=100, y=148)

    searchbar = tk.Entry(frame,
                         width=25,
                         fg="#ffffff",
                         bg="#56DAE4")
    searchbar.place(x=170, y=150)

    # Channel button for Freshers University
    freshers_university = tk.Button(frame,
                                  text=f"Freshers {selected_universities}",
                                  font="impact 18",
                                  anchor="w",
                                  fg="#000000",
                                  bg="#ffffff",
                                  height=3,
                                  width=32,
                                  borderwidth=1,
                                  command=lambda: switch_page(frame, 'chats'))
    freshers_university.place(x=70, y=210)

    # Channel for selected course
    freshers_course = tk.Label(frame, text=f"Freshers {selected_courses}",
                                  font="impact 18",
                                  anchor="w",
                                  fg="#000000",
                                  bg="#ffffff",
                                  height=3,
                                  width=35,
                                  borderwidth=2,
                                  relief="solid")
    freshers_course.place(x=70, y=295)

    # channel for selected course germany
    freshers_course_ger = tk.Label(frame, text=f"Freshers {selected_courses} Germany",
                                     font="impact 18",
                                     anchor="w",
                                     fg="#000000",
                                     bg="#ffffff",
                                     height=3,
                                     width=35,
                                     borderwidth=2,
                                     relief="solid")
    freshers_course_ger.place(x=70, y=375)

    # channel for course in Lüneburg
    freshers_course_lüneburg = tk.Label(frame, text=f"Freshers {selected_courses} Lüneburg",
                                    font="impact 18",
                                    anchor="w",
                                    fg="#000000",
                                    bg="#ffffff",
                                    height=3,
                                    width=35,
                                    borderwidth=2,
                                    relief="solid")
    freshers_course_lüneburg.place(x=70, y=455)

    # button to theoretically join more channels
    join_more = tk.Button(frame, text="+ join more channels",
                          font="Bahnschrift 15",
                          fg="#000000",
                          bg="#ffffff",
                          border=0)
    join_more.place(x=85, y=620)