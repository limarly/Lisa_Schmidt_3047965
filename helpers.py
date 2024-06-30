import tkinter as tk
from PIL import Image, ImageTk
from datetime import date

# Dictionary to store user information
user_data = {}
profile_information = {}
new_post = {}


# Function to display a tooltip
# https://stackoverflow.com/questions/23482748/how-to-create-a-hyperlink-with-a-label-in-tkinter
def show_tooltip(event, text):
    global tooltip
    x, y, _, _ = event.widget.bbox("insert")
    x += event.widget.winfo_rootx() + 15
    y += event.widget.winfo_rooty() + 25
    tooltip = tk.Toplevel(event.widget)
    tooltip.wm_overrideredirect(True)
    tooltip.wm_geometry(f"+{x}+{y}")
    label = tk.Label(tooltip, text=text,
                     font="Bahnschrift 13",
                     fg="#000000",
                     bg="#ffffff",
                     width=29,
                     border=0,
                     anchor='w')
    label.pack()


# Function to hide the tooltip
def hide_tooltip(event):
    global tooltip
    if tooltip:
        tooltip.destroy()
    tooltip = None


# Function to calculate age based on birthday
def calculate_age(birthday):
    year, month, day = birthday.split("-")
    year = int(year)
    month = int(month)
    day = int(day)

    # convert the dob into date format
    dob = date(year, month, day)

    # todays date
    current_date = date.today()

    # calculate the age
    user_age = int((current_date - dob).days / 365.25)

    return user_age


# Function to save user information into global dictionary
def save_user_information(first_name, last_name, birthday, username, password, selected_interests,
                          selected_universities, selected_courses):
    global user_data
    user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "birthday": birthday,
        "age": calculate_age(birthday),
        "username": username,
        "password": password,
        "selected_interests": selected_interests,
        "selected_universities": selected_universities,
        "selected_courses": selected_courses
    }

    print("User Information Saved Successfully!")


# Function to save profile information into global dictionary
def save_profile_information(personal_description, current_mood_link):
    global profile_information
    profile_information = {
        "personal_description": personal_description,
        "current_mood_link": current_mood_link
    }
    print("Profile Information Saved Successfully!")


# Function to save new post content into global dictionary
def save_new_post(hashtags, post_text):
    global new_post
    new_post = {
        "hashtags": hashtags,
        "post_text": post_text
    }
    print("Post Content Saved Successfully!")


# Function to retrieve user data
def get_user_data():
    global user_data
    return user_data


# Function to retrieve profile information
def get_profile_information():
    global profile_information
    return profile_information


# Function to retrieve new post content
def get_new_post_content():
    global new_post
    return new_post


# Function to display navigation buttons on a frame
def display_buttons(frame, switch_page):
    # Logo and button for 'Channels'
    channels_profile_pic = Image.open('src/images/channel_light.png')
    channels_profile_pic = channels_profile_pic.resize((50, 50), Image.LANCZOS)
    channels_profile_pic_image = ImageTk.PhotoImage(channels_profile_pic)
    channels_profile_pic_label = tk.Label(frame, image=channels_profile_pic_image,
                                          border=0)
    channels_profile_pic_label.image = channels_profile_pic_image
    channels_profile_pic_label.place(x=98, y=735)

    channels_button = tk.Button(frame, text="Channels", font="Bahnschrift 17", fg="#5B5C5E", bg="#ffffff", border=0,
                                command=lambda: switch_page(frame, 'channels'))
    channels_button.place(x=75, y=790)

    # logo for post
    post_profile_pic = Image.open('src/images/post_light.png')
    post_profile_pic = post_profile_pic.resize((48, 48), Image.LANCZOS)
    post_profile_pic_image = ImageTk.PhotoImage(post_profile_pic)
    post_profile_pic_label = tk.Label(frame, image=post_profile_pic_image, border=0)
    post_profile_pic_label.image = post_profile_pic_image
    post_profile_pic_label.place(x=190, y=737)

    post_button = tk.Button(frame, text="Post", font="Bahnschrift 17", fg="#5B5C5E", bg="#ffffff", border=0,
                            command=lambda: switch_page(frame, 'post'))
    post_button.place(x=182, y=790)

    # logo for match
    match_profile_pic = Image.open('src/images/match_light.png')
    match_profile_pic = match_profile_pic.resize((48, 48), Image.LANCZOS)
    match_profile_pic_image = ImageTk.PhotoImage(match_profile_pic)
    match_profile_pic_label = tk.Label(frame, image=match_profile_pic_image,
                                       border=0)
    match_profile_pic_label.image = match_profile_pic_image
    match_profile_pic_label.place(x=273, y=735)

    match_button = tk.Button(frame, text="Match", font="Bahnschrift 17", fg="#5B5C5E", bg="#ffffff", border=0,
                             command=lambda: switch_page(frame, 'match'))
    match_button.place(x=252, y=790)

    # logo for current page profile
    profile_profile_pic = Image.open('src/images/profile_dark.png')
    profile_profile_pic = profile_profile_pic.resize((50, 50), Image.LANCZOS)
    profile_profile_pic_image = ImageTk.PhotoImage(profile_profile_pic)
    profile_profile_pic_label = tk.Label(frame, image=profile_profile_pic_image,
                                         border=0)
    profile_profile_pic_label.image = profile_profile_pic_image
    profile_profile_pic_label.place(x=350, y=737)

    profile_button = tk.Button(frame, text="Profile", font="Bahnschrift 17", fg="#56DAE4", bg="#ffffff", border=0,
                               command=lambda: switch_page(frame, 'profile'))
    profile_button.place(x=335, y=790)
