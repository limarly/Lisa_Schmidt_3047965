import tkinter as tk
from PIL import Image, ImageTk
from src.helpers import get_user_data, get_profile_information, display_buttons
import webbrowser  # https://stackoverflow.com/questions/23482748/how-to-create-a-hyperlink-with-a-label-in-tkinter


# Function to open URLs in default web browser
def callback(url):
    webbrowser.open_new(url)


# Function to create the profile page
def create_profile_page(root, switch_page):
    frame = tk.Frame(root)
    frame.pack()

    img = Image.open('src/images/phone.png').resize((490, 875), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(frame, image=pic)
    Lab.image = pic
    Lab.pack()

    # Profile settings button (gear icon) to navigate to profile settings
    profile_settings_button = tk.Button(frame, text="⚙", font="Bahnschrift 33", fg="#56DAE4", bg="#ffffff", border=0,
                                        command=lambda: switch_page(frame, 'profile_settings'))
    profile_settings_button.place(x=345, y=120)

    # Display navigation buttons defined in src.helpers
    display_buttons(frame, switch_page)

    # Retrieve user data
    user_data = get_user_data()

    # Label to greet user with their name and age
    hi_label = tk.Label(frame, text="Hi! I am",
                        font="impact 22",
                        fg="#ffffff",
                        bg="#56DAE4",
                        justify="left")
    hi_label.place(x=90, y=300)

    # Label displaying user's full name and age
    full_name_label = tk.Label(frame, text=f"{user_data['first_name']} {user_data['last_name']}, {user_data['age']}",
                               font="impact 24",
                               fg="#ffffff",
                               bg="#56DAE4",
                               justify="left")
    full_name_label.place(x=90, y=333)

    # Retrieve selected courses and universities
    selected_courses = " ".join(user_data['selected_courses'])
    selected_universities = " ".join(user_data['selected_universities'])
    selected_interests = ", ".join(user_data['selected_interests'])

    # Label displaying user's selected courses and universities
    profile_study_information = tk.Label(frame,
                                         text=f"I study {selected_courses}\n at {selected_universities}",
                                         font="Bahnschrift 15 bold",
                                         fg="#ffffff",
                                         bg="#56DAE4",
                                         justify="left")
    profile_study_information.place(x=90, y=375)

    # Label displaying user's selected interests
    profile_interests = tk.Label(frame, text=f" I am interested in\n   {selected_interests}",
                                 font="Bahnschrift 15 bold",
                                 fg="#ffffff",
                                 bg="#56DAE4",
                                 justify="left")
    profile_interests.place(x=90, y=430)

    # Retrieve additional profile information using helper function
    profile_information = get_profile_information()

    if profile_information:
        # Display user's personal description if available
        personal_description = profile_information.get('personal_description', '')
        personal_description_label = tk.Label(frame,
                                              text=personal_description,
                                              font="Bahnschrift 14",
                                              anchor="nw",
                                              height=11,
                                              width=35,
                                              fg="#5B5C5E",
                                              bg="#ffffff",
                                              justify="left",
                                              borderwidth=2,
                                              relief="solid")
        personal_description_label.place(x=90, y=485)

        # current mood label
        current_mood = tk.Label(frame, text="Current Mood",
                                font="impact 15",
                                fg="#56DAE4",
                                bg="#ffffff")
        current_mood.place(x=100, y=640)

        # Retrieve and bind current mood link to a clickable image
        current_mood_link = profile_information.get('current_mood_link', '')

        play_song = Image.open('src/images/play_song.png')
        play_song = play_song.resize((30, 30), Image.LANCZOS)
        play_song_image = ImageTk.PhotoImage(play_song)
        play_song_label = tk.Label(frame, image=play_song_image, border=0)
        play_song_label.image = play_song_image
        play_song_label.place(x=200, y=638)

        play_song_label.bind("<Button-1>", lambda e: callback(current_mood_link))

    else:
        # Display placeholder message if no personal description is available
        missing_personal_description = tk.Label(frame,
                                                text="This is your space to write something about\nyourself! Go to settings and help others get to\nknow you better!",
                                                font="Bahnschrift 14",
                                                anchor="nw",
                                                height=11,
                                                width=35,
                                                fg="#5B5C5E",
                                                bg="#ffffff",
                                                justify="left",
                                                borderwidth=2,
                                                relief="solid")
        missing_personal_description.place(x=90, y=485)

        # current mood label
        current_mood = tk.Label(frame, text="Current Mood",
                                font="impact 15",
                                fg="#56DAE4",
                                bg="#ffffff")
        current_mood.place(x=100, y=640)

        play_song = Image.open('src/images/play_song.png')
        play_song = play_song.resize((30, 30), Image.LANCZOS)
        play_song_image = ImageTk.PhotoImage(play_song)
        play_song_label = tk.Label(frame, image=play_song_image, border=0)
        play_song_label.image = play_song_image
        play_song_label.place(x=200, y=638)

        # placeholder for a spotify song that shows the current mood
        current_mood_explanation = tk.Label(frame, text="Add a song that represents\nyour current mood",
                                            font="Bahnschrift 10",
                                            fg="#56DAE4",
                                            bg="#ffffff",
                                            border=0,
                                            justify="left")
        current_mood_explanation.place(x=250, y=640)

        profile_label = tk.Label(frame, text="Profile", font="impact 40 italic bold", fg="#ffffff", bg="#56DAE4")
        profile_label.place(x=185, y=75)


