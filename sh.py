from screeninfo import get_monitors
from PIL import ImageGrab, Image, ImageTk
import pytesseract
import cv2
import os
from tkinter import *
from comboKey import gen_event
from pynput import keyboard
import sys
import pyautogui


def execute():
    print("Do Something")


on_press, on_release = gen_event(execute)


def quit(event):
    sys.exit()  # if you want to exit the entire thing


# ------------ DEFINE
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# ------------ VARIABLES
screen_width = 0
screen_height = 0

# ------------ GET INFOR SCREEN
for m in get_monitors():
    screen_width = m.width
    screen_height = m.height

# --------------- CREATE UI APP
root = Tk()
root.attributes('-fullscreen', True)
root.title = "TSApp"
root.geometry(str(screen_width)+"x"+str(screen_height))
root.configure(bg='')


# ----------------------------------------------

# --------------------------- KEYBOARD LISTENER------------------------------
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
# --------------------------- KEYBOARD LISTENER------------------------------

# ------------- SCREENSHOT
ss_region = (0, 0, screen_width, screen_height)
ss_img = ImageGrab.grab(ss_region)

# ------------- CREATE FILE NAME RANDOM
filename = "{}.png".format(os.getpid())

# -------------- SAVE IMAGE
# ss_img.show()
ss_img.save(filename)


frame = Frame(root, background="red")
canvas = Canvas(frame, width=screen_width,
                height=screen_height,  bd=0, highlightthickness=0, bg='red')


image = PhotoImage(file=filename)
# label = Label(frame, image=image, bd=0)
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.create_rectangle(0, 0, 200, 200, fill='', outline='orange', width=5)
text = canvas.create_text(100, 40, text="HELLO WORLD",
                          fill="white", font=('Helvetica 15 bold'),)
r = canvas.create_rectangle(canvas.bbox(text), fill="black")
canvas.tag_lower(r, text)
canvas.pack(padx=5, pady=5)

# label.pack(padx=5, pady=5)
frame.pack()

# frame = Frame(root, background="orange")
# canvas = Canvas(frame,  bd=0, highlightthickness=0, bg='red')
# # canvas.create_image(0, 0, anchor=NW, image=image)
# canvas.create_rectangle(0, 0, 200, 200, fill='yellow')
# # canvas.pack()
# frame.pack()

root.bind('<Escape>', quit)


def action(event):
    print('hello')


root.bind("<ButtonPress-1>", action)

root.mainloop()
listener.stop()
listener.join()

# --------------- HANDLE IMAGE AND EXTRACT TO TEXT
# image = cv2.imread(filename)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# pytesseract.pytesseract.tesseract_cmd = path_to_tesseract


# text = pytesseract.image_to_string(ss_img)

# ---------- REMOVE IMAGE
# os.remove(filename)

# print(text)

# import googletrans
# from googletrans import Translator

# t = Translator()
# a = t.translate("xin chao", src="vi", dest="en")
# print (a.text)
