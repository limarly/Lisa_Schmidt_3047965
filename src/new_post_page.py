import tkinter as tk
from PIL import Image, ImageTk
from src.helpers import display_buttons, save_new_post


def create_new_post_page(root, switch_page):
    frame = tk.Frame(root)
    frame.pack()

    img = Image.open('src/images/phone.png').resize((490, 875), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(frame, image=pic)
    Lab.image = pic
    Lab.pack()

    # Display navigation buttons (Channels, Post, Match, Profile)
    display_buttons(frame, switch_page)

    # Initialize StringVars to store hashtag and post text input
    hashtags = tk.StringVar()
    post_text = tk.StringVar()

    # Function to save the new post and switch to the next page
    def proceed_to_next_page(frame, target_page):
        save_new_post(hashtags.get(), post_text.get())  # Save post using helper function
        switch_page(frame, target_page)  # Switch to the specified page

    # title for the page
    profile = tk.Label(frame, text="Create a new post",
                       font="impact 40 italic bold",
                       fg="#ffffff",
                       bg="#56DAE4")
    profile.place(x=105, y=75)

    post_text_explanation = tk.Label(frame,
                                     text="What would you like to post?",
                                     font="Bahnschrift 15",
                                     fg="#ffffff",
                                     bg="#56DAE4",
                                     anchor="nw",
                                     justify="left"
                                     )
    post_text_explanation.place(x=100, y=200)

    # Entry field for entering post text
    post_text_entry = tk.Entry(frame,
                               font="Bahnschrift 15",
                               textvariable=post_text,
                               fg="#000000",
                               bg="#ffffff",
                               width=25,
                               border=0)
    post_text_entry.place(x=100, y=250)

    hashtags_explanation = tk.Label(frame, text="Add some # so others can find your post easier!",
                                    font="Bahnschrift 15",
                                    fg="#ffffff",
                                    bg="#56DAE4",
                                    anchor="nw",
                                    justify="left"
                                    )
    hashtags_explanation.place(x=100, y=400)

    # Entry field for entering hashtags
    hashtags_entry = tk.Entry(frame,
                              font="Bahnschrift 15",
                              textvariable=hashtags,
                              fg="#000000",
                              bg="#ffffff",
                              width=25,
                              border=0,
                              )
    hashtags_entry.place(x=100, y=450)

    # Button to proceed to posting the new post
    back_to_post_page = tk.Button(frame,
                                text="POST",
                                font="Bahnschrift 18 bold italic",
                                fg="#56DAE4",
                                bg="#ffffff",
                                width=18,
                                height=1,
                                border=0,
                                command=lambda: proceed_to_next_page(frame, 'post'))
    back_to_post_page.place(x=120, y=700)
