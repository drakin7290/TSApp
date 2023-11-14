# from pynput import keyboard

# # The key combination to check
# COMBINATIONS = [
#     {keyboard.Key.shift, keyboard.KeyCode(char='a')},
#     {keyboard.Key.shift, keyboard.KeyCode(char='A')}
# ]

# current = set()


# def gen_event(func):
#     def on_press(key):
#         if any([key in COMBO for COMBO in COMBINATIONS]):
#             current.add(key)
#             if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
#                 func()

#     def on_release(key):
#         try:
#             if any([key in COMBO for COMBO in COMBINATIONS]):
#                 current.remove(key)
#         except:
#             pass

#     return on_press, on_release

# from googletrans import LANGCODES, LANGUAGES
# print(LANGUAGES)

from customtkinter import *
from PIL import Image
import os

list_themes = os.listdir("./themes");

set_appearance_mode("dark")
set_default_color_theme("./themes/GhostTrain.json")

def choose_themes(choice):
	path = "./themes/Greengage.json"


top = CTk()
top.geometry("765x520")
top.minsize(120, 1)
top.maxsize(1924, 1061)
top.resizable(0,  0)
top.title("TSApp")
top.configure(background="#d9d9d9")
top.configure(highlightbackground="#d9d9d9")
top.configure(highlightcolor="black")

# SECTION 1 ----------------------------------------------------------------------------
title_label = CTkLabel(master=top, text='''TSAPP - Translate scan app''', font=("Tahoma", 32, "bold"))
title_label.place(x=10, y=10)

my_image = CTkImage(light_image=Image.open("./Image.png"),
                                  dark_image=Image.open("./Image.png"),
                                  size=(240, 200))
image_label = CTkLabel(top, image=my_image, text="")  # display image with a CTkLabel

image_label.place(x=480, y=10)

button_trans_screen = CTkButton(master=top, text='Dịch màn hình', font=("Tahoma", 14))
button_trans_screen.place (x=10, y=60 )

button_trans_file = CTkButton(master=top, text='Dịch file ảnh', font=("Tahoma", 14))
button_trans_file.place (x=160, y=60 )

setting_label = CTkLabel(master=top, text='''Cài đặt''', font=("Tahoma", 24, "bold"))
setting_label.place(x=10, y=100)

choose_themes_label = CTkLabel(master=top, text='''Chọn theme''', font=("Tahoma", 14))
choose_themes_label.place(x=10, y=140)

choose_themes_cbo = CTkComboBox(top, values=list_themes, command=choose_themes)
choose_themes_cbo.place (x=100, y=140)

top.mainloop()