import tkinter as tk
from PIL import Image, ImageTk
from src.helpers import get_user_data, display_buttons, get_new_post_content


def create_post_page(root, switch_page):
    frame = tk.Frame(root)
    frame.pack()

    img = Image.open('src/images/phone.png').resize((490, 875), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(frame, image=pic)
    Lab.image = pic
    Lab.pack()

    # Display navigation buttons (Channels, Post, Match, Profile)
    display_buttons(frame, switch_page)

    # Get user data and post content from helper functions
    user_data = get_user_data()
    post_content = get_new_post_content()

    # title for the page
    profile = tk.Label(frame, text="Post",
                       font="impact 40 italic bold",
                       fg="#ffffff",
                       bg="#56DAE4")
    profile.place(x=205, y=75)

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

    filter_button = tk.Button(frame, text="Filter",
                              font="Bahnschrift 15",
                              fg="#5B5C5E",
                              bg="#ffffff",
                              border=0,
                              command=lambda: switch_page(frame, 'post_filter'))
    filter_button.place(x=133, y=193)

    # filter logo
    filter_post = Image.open('src/images/filter.png')
    filter_post = filter_post.resize((24, 24), Image.LANCZOS)
    filter_post_image = ImageTk.PhotoImage(filter_post)
    filter_post_label = tk.Label(frame, image=filter_post_image, border=0)
    filter_post_label.image = filter_post_image
    filter_post_label.place(x=105, y=194)

    create_button = tk.Button(frame, text="Create",
                              font="Bahnschrift 15",
                              fg="#5B5C5E",
                              bg="#ffffff",
                              border=0,
                              command=lambda: switch_page(frame, 'new_post'))
    create_button.place(x=320, y=193)

    # create logo
    paperplane_white = Image.open('src/images/paperplane_white.png')
    paperplane_white = paperplane_white.resize((24, 24), Image.LANCZOS)
    paperplane_white_image = ImageTk.PhotoImage(paperplane_white)
    paperplane_white_label = tk.Label(frame, image=paperplane_white_image, border=0)
    paperplane_white_label.image = paperplane_white_image
    paperplane_white_label.place(x=290, y=194)

    # Check if there is existing post content to display
    if post_content:
        post_text = post_content.get('post_text', '')
        hashtags = post_content.get('hashtags', '')
        selected_courses = " ".join(user_data['selected_courses'])
        selected_universities = " ".join(user_data['selected_universities'])

        # new post from user
        new_post_label = tk.Label(frame,
                                  text=post_text,
                                  font="Bahnschrift 14",
                                  anchor="nw",
                                  justify="left",
                                  height=13,
                                  width=36,
                                  fg="#000000",
                                  bg="#ffffff",
                                  borderwidth=2,
                                  relief="solid")
        new_post_label.place(x=85, y=250)

        hashtags_user = tk.Label(frame, text=f"{hashtags}",
                                 font="impact 13",
                                 fg="#56DAE4",
                                 bg="#ffffff")
        hashtags_user.place(x=100, y=338)

        # Placeholder profile picture
        placeholder_pic = Image.open('src/images/placeholder_pic.png')
        placeholder_pic = placeholder_pic.resize((75, 75), Image.LANCZOS)
        placeholder_pic_image = ImageTk.PhotoImage(placeholder_pic)
        placeholder_pic_label = tk.Label(frame, image=placeholder_pic_image, border=0)
        placeholder_pic_label.image = placeholder_pic_image
        placeholder_pic_label.place(x=110, y=360)

        # Display user's details
        user_details_label = tk.Label(frame,
                                        text=f"{user_data['first_name']} {user_data['last_name']}, {user_data['age']}\n{selected_courses}\n{selected_universities}",
                                        font="impact 13",
                                        justify="left",
                                        fg="#000000",
                                        bg="#ffffff")
        user_details_label.place(x=180, y=360)

        # Separator line
        first_black_line = tk.Frame(frame,
                                    bg="#000000",
                                    height=3,
                                    width=300)
        first_black_line.place(x=100, y=435)

        # Buttons for user interaction with the post
        connect_leonie = tk.Button(frame, text="edit",
                                   font="impact 10",
                                   fg="#000000",
                                   bg="#ffffff",
                                   border=0.5)
        connect_leonie.place(x=117, y=446)

        message_leonie = tk.Button(frame, text="messages",
                                   font="impact 10",
                                   fg="#000000",
                                   bg="#ffffff",
                                   border=0.5)
        message_leonie.place(x=218, y=446)

        share_leonie = tk.Button(frame, text="share",
                                 font="impact 10",
                                 fg="#000000",
                                 bg="#ffffff",
                                 border=0.5)
        share_leonie.place(x=345, y=446)

    else:
        # If no existing post content, display sample posts
        # Post from Leonie Meyer
        post_leonie_label = tk.Label(frame,
                                     text="Hi, I just moved to Lüneburg and would like\nto "
                                          "connect with some people before uni\nstarts. I've "
                                          "seen that there are Beach\nVolleyball courts on "
                                          "campus. Would someone\nlike to get together and "
                                          "play some Volleyball?",
                                     font="Bahnschrift 14",
                                     anchor="n",
                                     justify="left",
                                     height=13,
                                     width=36,
                                     fg="#000000",
                                     bg="#ffffff",
                                     borderwidth=2,
                                     relief="solid")
        post_leonie_label.place(x=85, y=250)

        hashtags_volleyball = tk.Label(frame, text="#beachvolleyball   #volleyball",
                                       font="impact 13",
                                       fg="#56DAE4",
                                       bg="#ffffff")
        hashtags_volleyball.place(x=100, y=338)

        placeholder_pic = Image.open('src/images/placeholder_pic.png')
        placeholder_pic = placeholder_pic.resize((75, 75), Image.LANCZOS)
        placeholder_pic_image = ImageTk.PhotoImage(placeholder_pic)
        placeholder_pic_label = tk.Label(frame, image=placeholder_pic_image, border=0)
        placeholder_pic_label.image = placeholder_pic_image
        placeholder_pic_label.place(x=110, y=360)

        leonie_details_label = tk.Label(frame,
                                        text="Leonie Meyer 21\nBusiness "
                                             "Administration\nLeuphana University "
                                             "Lüneburg\nLüneburg",
                                        font="impact 13",
                                        justify="left",
                                        fg="#000000",
                                        bg="#ffffff")
        leonie_details_label.place(x=180, y=360)

        first_black_line = tk.Frame(frame,
                                    bg="#000000",
                                    height=3,
                                    width=300)
        first_black_line.place(x=100, y=435)

        connect_leonie = tk.Button(frame, text="connect",
                                   font="impact 10",
                                   fg="#000000",
                                   bg="#ffffff",
                                   border=0.5)
        connect_leonie.place(x=117, y=446)

        message_leonie = tk.Button(frame, text="send message",
                                   font="impact 10",
                                   fg="#000000",
                                   bg="#ffffff",
                                   border=0.5)
        message_leonie.place(x=218, y=446)

        share_leonie = tk.Button(frame, text="share",
                                 font="impact 10",
                                 fg="#000000",
                                 bg="#ffffff",
                                 border=0.5)
        share_leonie.place(x=345, y=446)

    # post from Paula Whalley
    post_paula_label = tk.Label(frame,
                                text="Hi, I am going to move to Hamburg on 2nd "
                                     "of\nOctober. If someones free that day please "
                                     "hit\nme up. I still need a few helpers who are "
                                     "able\nto lift a bit more. I'll provide pizza and "
                                     "beer\nafterwards as a thank you.",
                                font="Bahnschrift 14",
                                anchor="n",
                                justify="left",
                                height=13,
                                width=36,
                                fg="#000000",
                                bg="#ffffff",
                                borderwidth=2,
                                relief="solid"
                                )
    post_paula_label.place(x=85, y=490)

    hashtags_moving = tk.Label(frame, text="#moving   #beer   #pizza",
                               font="impact 13",
                               fg="#56DAE4",
                               bg="#ffffff")
    hashtags_moving.place(x=100, y=578)

    placeholder_pic_paula = Image.open('src/images/placeholder_pic.png')
    placeholder_pic_paula = placeholder_pic_paula.resize((75, 75), Image.LANCZOS)
    placeholder_pic_paula_image = ImageTk.PhotoImage(placeholder_pic_paula)
    placeholder_pic_paula_label = tk.Label(frame, image=placeholder_pic_paula_image,
                                           border=0)
    placeholder_pic_paula_label.image = placeholder_pic_paula_image
    placeholder_pic_paula_label.place(x=110, y=600)

    paula_details_label = tk.Label(frame,
                                   text="Paula Whalley 20\nDigital Media\nHamburg Media School\nHamburg",
                                   font="impact 13",
                                   justify="left",
                                   fg="#000000",
                                   bg="#ffffff")
    paula_details_label.place(x=180, y=600)

    second_black_line = tk.Frame(frame,
                                 bg="#000000",
                                 height=3,
                                 width=300)
    second_black_line.place(x=100, y=675)

    connect_paula = tk.Button(frame, text="connect",
                              font="impact 10",
                              fg="#000000",
                              bg="#ffffff",
                              border=0.5)
    connect_paula.place(x=117, y=686)

    message_paula = tk.Button(frame, text="send message",
                              font="impact 10",
                              fg="#000000",
                              bg="#ffffff",
                              border=0.5)
    message_paula.place(x=218, y=686)

    share_paula = tk.Button(frame, text="share",
                            font="impact 10",
                            fg="#000000",
                            bg="#ffffff",
                            border=0.5)
    share_paula.place(x=345, y=686)
