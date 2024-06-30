import tkinter as tk
from PIL import ImageTk
from src import welcome_page, sign_in_page, sign_up_page, get_verified_page, verified_page, profile_page, \
    settings_page, match_page, post_page, channels_page, chats_page, new_post_page, post_filter_page


# Define a function to switch between different pages
def switch_page(frame, target_page):
    # Destroy the current frame
    frame.destroy()

    # Determine which page to switch to based on the target_page argument
    if target_page == 'welcome':
        welcome_page.create_welcome_page(root, switch_page)
    elif target_page == 'sign_in':
        sign_in_page.create_sign_in_page(root, switch_page)
    elif target_page == 'sign_up':
        sign_up_page.create_sign_up_page(root, switch_page)
    elif target_page == 'get_verified':
        get_verified_page.create_get_verified_page(root, switch_page)
    elif target_page == 'verified':
        verified_page.create_verified_page(root, switch_page)
    elif target_page == 'profile':
        profile_page.create_profile_page(root, switch_page)
    elif target_page == 'profile_settings':
        settings_page.create_profile_settings(root, switch_page)
    elif target_page == "match":
        match_page.create_match_page(root, switch_page)
    elif target_page == "post":
        post_page.create_post_page(root, switch_page)
    elif target_page == "channels":
        channels_page.create_channels_page(root, switch_page)
    elif target_page == "chats":
        chats_page.create_chats_page(root, switch_page)
    elif target_page == "new_post":
        new_post_page.create_new_post_page(root, switch_page)
    elif target_page == 'post_filter':
        post_filter_page.create_post_filter_page(root, switch_page)


# Create the main application window
root = tk.Tk()
root.title("Freshers Connect")
root.geometry("490x875")

# Load and set the application icon
icon_img = ImageTk.PhotoImage(file='src/images/logo_fc.png')  # Provide the correct path to your .ico file
root.iconphoto(False, icon_img)

# Create and display the welcome page initially
welcome_page.create_welcome_page(root, switch_page)
# Start the Tkinter main event loop
root.mainloop()
