import tkinter as tk
from PIL import Image, ImageTk
from src.helpers import get_user_data, display_buttons


def create_chats_page(root, switch_page):
    frame = tk.Frame(root)
    frame.pack()

    img = Image.open('src/images/phone.png').resize((490, 875), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(frame, image=pic)
    Lab.image = pic
    Lab.pack()

    # Display navigation buttons (Channels, Post, Match, Profile)
    display_buttons(frame, switch_page)

    # Retrieve user data from helpers
    user_data = get_user_data()
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
    search_label.place(x=100, y=128)

    searchbar = tk.Entry(frame,
                         width=25,
                         fg="#ffffff",
                         bg="#56DAE4")
    searchbar.place(x=170, y=130)

    # Chat entries for different conversations
    # Chat entry for Paula Whalley
    freshers_chat_title = tk.Label(frame, text=f"Freshers {selected_universities}",
                                   font="impact 18",
                                   anchor="center",
                                   fg="#000000",
                                   bg="#ffffff",
                                   height=2,
                                   width=33,
                                   borderwidth=2,
                                   relief="solid")
    freshers_chat_title.place(x=78, y=170)

    white_label_paula = tk.Label(frame, text="",
                                 height=6,
                                 width=36,
                                 bg="#ffffff",
                                 borderwidth=2,
                                 relief="solid")
    white_label_paula.place(x=80, y=230)

    text_paula = tk.Label(frame,
                          text="Hi, I am going to move to lueneburg on 2nd of October. If "
                               "some-\nones free that day please hit me up. I still need "
                               "a few helpers who\nare able to lift a bit more. I'll "
                               "provide pizza and beer afterwards\nas a thank you.",
                          font="Bahnschrift 10",
                          fg="#000000",
                          bg="#ffffff",
                          justify="left",
                          anchor="nw"
                          )
    text_paula.place(x=85, y=249)

    chat_paula = tk.Label(frame, text="Paula Whalley  20",
                          font="impact 11",
                          fg="#000000",
                          bg="#ffffff",
                          anchor="nw"
                          )
    chat_paula.place(x=86, y=234)

    hashtags_paula = tk.Label(frame, text="#moving   #beer   #pizza",
                              font="impact 11",
                              fg="#56DAE4",
                              bg="#ffffff",
                              )
    hashtags_paula.place(x=165, y=287)

    contribute_paula = tk.Label(frame, text="contribute",
                                font="impact 11",
                                fg="#000000",
                                bg="#ffffff"
                                )
    contribute_paula.place(x=140, y=305)

    save_conversation_paula = tk.Label(frame, text="save conversation",
                                       font="impact 11",
                                       fg="#000000",
                                       bg="#ffffff"
                                       )
    save_conversation_paula.place(x=260, y=305)

    # chat justus value
    white_label_justus = tk.Label(frame, text="",
                                  height=10,
                                  width=36,
                                  bg="#ffffff",
                                  borderwidth=2,
                                  relief="solid")
    white_label_justus.place(x=80, y=339)

    text_justus = tk.Label(frame,
                           text="Hey guys, does someone know the email address for the "
                                "faculty\nof business administration or know where I can "
                                "find it?",
                           font="Bahnschrift 10",
                           fg="#000000",
                           bg="#ffffff",
                           justify="left",
                           anchor="nw"
                           )
    text_justus.place(x=85, y=358)

    chat_justus = tk.Label(frame, text="Justus Value  20",
                           font="impact 11",
                           fg="#000000",
                           bg="#ffffff",
                           anchor="nw"
                           )
    chat_justus.place(x=86, y=343)

    hashtags_justus = tk.Label(frame, text="#faculty",
                               font="impact 11",
                               fg="#56DAE4",
                               bg="#ffffff",
                               )
    hashtags_justus.place(x=100, y=385)

    contribute_justus = tk.Label(frame, text="contribute",
                                 font="impact 11",
                                 fg="#000000",
                                 bg="#ffffff"
                                 )
    contribute_justus.place(x=140, y=410)

    save_conversation_justus = tk.Label(frame, text="save conversation",
                                        font="impact 11",
                                        fg="#000000",
                                        bg="#ffffff"
                                        )
    save_conversation_justus.place(x=260, y=410)

    black_line = tk.Frame(frame,
                          bg="#000000",
                          height=3,
                          width=300)
    black_line.place(x=100, y=438)

    text_leonie = tk.Label(frame,
                           text="It's ibae.faculty@leuphana.de, you can find alle the "
                                "important\nemails at www.emails/leuphana.de",
                           font="Bahnschrift 10",
                           fg="#000000",
                           bg="#ffffff",
                           justify="right",
                           anchor="nw"
                           )
    text_leonie.place(x=95, y=460)

    chat_leonie = tk.Label(frame, text="Leonie Meyer  21",
                           font="impact 11",
                           fg="#000000",
                           bg="#ffffff",
                           anchor="nw"
                           )
    chat_leonie.place(x=320, y=441)

    # chat justin kern
    white_label_justin = tk.Label(frame, text="",
                                  height=6,
                                  width=36,
                                  bg="#ffffff",
                                  borderwidth=2,
                                  relief="solid")
    white_label_justin.place(x=80, y=540)

    text_justin = tk.Label(frame,
                           text="Hey everyone, just wanted to remind you of the big "
                                "freshers meet\nup next Saturday at Mensawiese. It's a "
                                "great opportunity to con-\nnect in person before uni "
                                "starts. You can find additional infor-\nmation and the "
                                "registration form at www.asta/freshers/meetup.de",
                           font="Bahnschrift 10",
                           fg="#000000",
                           bg="#ffffff",
                           justify="left",
                           anchor="nw"
                           )
    text_justin.place(x=85, y=559)

    chat_justin = tk.Label(frame, text="Justin Kern  23",
                           font="impact 11",
                           fg="#000000",
                           bg="#ffffff",
                           anchor="nw"
                           )
    chat_justin.place(x=86, y=544)

    contribute_justin = tk.Label(frame, text="contribute",
                                 font="impact 11",
                                 fg="#000000",
                                 bg="#ffffff"
                                 )
    contribute_justin.place(x=140, y=615)

    save_conversation_justin = tk.Label(frame, text="save conversation",
                                        font="impact 11",
                                        fg="#000000",
                                        bg="#ffffff"
                                        )
    save_conversation_justin.place(x=260, y=615)

    # start a conversation
    conversation = tk.Label(frame, text="Start a conversation",
                            font="impact 15",
                            fg="#000000",
                            bg="#ffffff",
                            anchor="nw",
                            height=3,
                            width=36,
                            borderwidth=2,
                            relief="solid")
    conversation.place(x=78, y=648)

    conversation_entry = tk.Entry(frame,
                                  fg="#000000",
                                  bg="#ffffff",
                                  width=30
                                  )
    conversation_entry.place(x=78, y=680)

    # send logo
    paperplane_blue = Image.open('src/images/paperplane_blue.png')
    paperplane_blue = paperplane_blue.resize((25, 25), Image.LANCZOS)
    paperplane_blue_image = ImageTk.PhotoImage(paperplane_blue)
    paperplane_blue_label = tk.Label(frame, image=paperplane_blue_image, border=0)
    paperplane_blue_label.image = paperplane_blue_image
    paperplane_blue_label.place(x=375, y=680)
