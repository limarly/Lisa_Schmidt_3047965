import tkinter as tk
from PIL import Image, ImageTk
from src.helpers import display_buttons


def create_post_filter_page(root, switch_page):
    frame = tk.Frame(root)
    frame.pack()

    img = Image.open('src/images/phone.png').resize((490, 875), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(frame, image=pic)
    Lab.image = pic
    Lab.pack()

    display_buttons(frame, switch_page)

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

    # Button that opened filter selection
    filter_button = tk.Button(frame, text="Filter",
                              font="Bahnschrift 15",
                              fg="#5B5C5E",
                              bg="#ffffff",
                              border=0)
    filter_button.place(x=133, y=193)

    # Button to close filter selection and return to Post Page
    close_filter_button = tk.Button(frame, text="X",
                                    font="Bahnschrift 15",
                                    fg="#5B5C5E",
                                    bg="#ffffff",
                                    border=0,
                                    command=lambda: switch_page(frame, 'post'))
    close_filter_button.place(x=350, y=193)

    # Filter logo
    filter_post_filter = Image.open('src/images/filter.png')
    filter_post_filter = filter_post_filter.resize((24, 24), Image.LANCZOS)
    filter_post_filter_image = ImageTk.PhotoImage(filter_post_filter)
    filter_post_filter_label = tk.Label(frame, image=filter_post_filter_image,
                                        border=0)
    filter_post_filter_label.image = filter_post_filter_image
    filter_post_filter_label.place(x=105, y=194)

    def create_checkbutton(frame, text, x, y):
        font_size = "impact 18"
        fg_colour = "#ffffff"
        bg_colour = "#56DAE4"
        checkbutton = tk.Checkbutton(frame, text=text, font=font_size, fg=fg_colour, bg=bg_colour)
        checkbutton.place(x=x, y=y)

    # Create university related checkbuttons
    create_checkbutton(frame, "University", 110, 240)
    create_checkbutton(frame, "Leuphana University lueneburg", 140, 268)
    create_checkbutton(frame, "Hamburg Media School", 140, 296)
    create_checkbutton(frame, "Other Choices", 140, 324)

    # Create course related checkbuttons
    create_checkbutton(frame, "Course", 110, 354)
    create_checkbutton(frame, "Digital Media", 140, 382)
    create_checkbutton(frame, "Business Administration", 140, 410)
    create_checkbutton(frame, "Other Courses", 140, 438)

    # Create city related checkbuttons
    create_checkbutton(frame, "City", 110, 468)
    create_checkbutton(frame, "lueneburg", 140, 496)
    create_checkbutton(frame, "Hamburg", 140, 524)
    create_checkbutton(frame, "Other Cities", 140, 552)

    # Create interests related checkbuttons
    create_checkbutton(frame, "Initiatives", 110, 582)
    create_checkbutton(frame, "enactus E.V.", 140, 610)
    create_checkbutton(frame, "Choir", 140, 638)
    create_checkbutton(frame, "Interests", 110, 666)
    create_checkbutton(frame, "Beach Volleyball", 140, 694)


