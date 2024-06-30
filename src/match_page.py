import tkinter as tk
from PIL import Image, ImageTk
from src.helpers import get_user_data, display_buttons


def create_match_page(root, switch_page):
    frame = tk.Frame(root)
    frame.pack()

    img = Image.open('src/images/phone.png').resize((490, 875), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(frame, image=pic)
    Lab.image = pic
    Lab.pack()

    # title for the page
    match = tk.Label(frame, text="Match",
                     font="impact 40 italic bold",
                     fg="#ffffff",
                     bg="#56DAE4")
    match.place(x=190, y=75)

    # call to action label
    fellow_freshers = tk.Label(frame, text="Let's get to know some fellow freshers",
                               font="impact 20",
                               fg="#ffffff",
                               bg="#56DAE4")
    fellow_freshers.place(x=90, y=140)

    # Explanation of what Match is
    whats_match = tk.Label(frame, text="What is Match?\nMatch is a page that shows you people who have at\nleast "
                                       "three commonalities with you based on what\nthey study, which university they "
                                       "study at, which city\nthey live in, and what common interests you might have",
                           font="arial 14",
                           anchor="n",
                           justify="left",
                           fg="#000000",
                           bg="#ffffff")
    whats_match.place(x=80, y=170)

    # Display navigation buttons (Channels, Post, Match, Profile)
    display_buttons(frame, switch_page)

    # Retrieve user data from helpers
    user_data = get_user_data()
    selected_courses = " ".join(user_data['selected_courses'])
    selected_universities = " ".join(user_data['selected_universities'])
    selected_interests = ", ".join(user_data['selected_interests'])

    # formatting of post from Leonie Meyer
    white_label_leonie = tk.Label(frame, text="",
                                  height=12,
                                  width=36,
                                  bg="#ffffff",
                                  borderwidth=2,
                                  relief="solid")
    white_label_leonie.place(x=85, y=270)

    post_uni_leonie = tk.Label(frame,
                               text=f"{selected_universities}\n {selected_interests}",
                               font="impact 13",
                               anchor="n",
                               justify="left",
                               height=2,
                               width=25,
                               fg="#56DAE4",
                               bg="#ffffff")
    post_uni_leonie.place(x=220, y=370)

    post_studyat_leonie = tk.Label(frame,
                                   text="You both study at \nand have interests in",
                                   font="impact 13",
                                   anchor="nw",
                                   justify="left",
                                   height=2,
                                   width=15,
                                   fg="#000000",
                                   bg="#ffffff")
    post_studyat_leonie.place(x=120, y=370)

    # Placeholder picture for Leonie Meyer
    placeholder_pic = Image.open('src/images/placeholder_pic.png')
    placeholder_pic = placeholder_pic.resize((75, 75), Image.LANCZOS)
    placeholder_pic_image = ImageTk.PhotoImage(placeholder_pic)
    placeholder_pic_label = tk.Label(frame, image=placeholder_pic_image, border=0)
    placeholder_pic_label.image = placeholder_pic_image
    placeholder_pic_label.place(x=108, y=285)

    leonie_details_label = tk.Label(frame,
                                    text=f"Leonie Meyer 21\n{selected_courses}\n{selected_universities}",
                                    font="impact 13",
                                    justify="left",
                                    fg="#000000",
                                    bg="#ffffff")
    leonie_details_label.place(x=180, y=285)

    first_black_line = tk.Frame(frame,
                                bg="#000000",
                                height=3,
                                width=300)
    first_black_line.place(x=100, y=420)

    connect_leonie = tk.Button(frame, text="connect",
                               font="impact 10",
                               fg="#000000",
                               bg="#ffffff",
                               border=0.5)
    connect_leonie.place(x=125, y=432)

    message_leonie = tk.Button(frame, text="send message",
                               font="impact 10",
                               fg="#000000",
                               bg="#ffffff",
                               border=0.5)
    message_leonie.place(x=225, y=432)


    # formatting of post from Maya Lemmer
    white_label_maya = tk.Label(frame, text="",
                                height=12,
                                width=36,
                                bg="#ffffff",
                                borderwidth=2,
                                relief="solid")
    white_label_maya.place(x=85, y=490)

    post_uni_maya = tk.Label(frame,
                             text=f"{selected_universities}\n {selected_courses}\nHamburg",
                             font="impact 13",
                             anchor="n",
                             justify="left",
                             height=2,
                             width=25,
                             fg="#56DAE4",
                             bg="#ffffff")
    post_uni_maya.place(x=220, y=590)

    post_studyat_maya = tk.Label(frame, text="You both study at \nand study",
                                 font="impact 13",
                                 anchor="nw",
                                 justify="left",
                                 height=2,
                                 width=15,
                                 fg="#000000",
                                 bg="#ffffff")
    post_studyat_maya.place(x=120, y=590)

    # Placeholder picture for Maya Lemmer
    placeholder_pic_maya = Image.open('src/images/placeholder_pic.png')
    placeholder_pic_maya = placeholder_pic_maya.resize((75, 75), Image.LANCZOS)
    placeholder_pic_image_maya = ImageTk.PhotoImage(placeholder_pic_maya)
    placeholder_pic_label_maya = tk.Label(frame, image=placeholder_pic_image_maya,
                                          border=0)
    placeholder_pic_label_maya.image = placeholder_pic_image_maya
    placeholder_pic_label_maya.place(x=108, y=505)

    maya_details_label = tk.Label(frame,
                                  text=f"Maya Lemmer 20\n{selected_courses}\n{selected_universities}\nHamburg",
                                  font="impact 13",
                                  justify="left",
                                  fg="#000000",
                                  bg="#ffffff")
    maya_details_label.place(x=180, y=505)

    second_black_line = tk.Frame(frame,
                                 bg="#000000",
                                 height=3,
                                 width=300)
    second_black_line.place(x=100, y=640)

    connect_maya = tk.Button(frame, text="connect",
                             font="impact 10",
                             fg="#000000",
                             bg="#ffffff",
                             border=0.5)
    connect_maya.place(x=125, y=652)

    message_maya = tk.Button(frame, text="send message",
                             font="impact 10",
                             fg="#000000",
                             bg="#ffffff",
                             border=0.5)
    message_maya.place(x=225, y=652)