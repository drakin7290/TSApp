
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter.constants import *
from screeninfo import get_monitors
from PIL import ImageGrab
import time
from googletrans import Translator, LANGCODES
import pytesseract
import os.path
import constant
from ui import top, ScreenshotBtn
# ------------ DEFINE
pytesseract.pytesseract.tesseract_cmd = constant.path_to_tesseract


translator = Translator()

image = None
imageCrop = None
srG = None
rect = None
coord = {"x1": 0, "y1": 0, "x2": 0, "y2": 0}

# ------------ VARIABLES
screen_width = 0
screen_height = 0

languageOriCode = 'en'
langueDestCode = 'vi'

# ------------ GET INFOR SCREEN
for m in get_monitors():
    screen_width = m.width
    screen_height = m.height


def get_index(x, lst):
    if (x in lst):
        return lst.index(x)
    return -1


def open_toplevel_window():
    sr = tk.Toplevel()
    sr.attributes('-fullscreen', True)

    # -------------- SAVE IMAGE
    # ss_img.show()

    frame = tk.Frame(sr, background="red")
    canvas = tk.Canvas(frame, width=screen_width,
                       height=screen_height,  bd=0, highlightthickness=0, bg='red')

    # label = tk.Label(frame, image=image, bd=0)
    canvas.create_image(0, 0, anchor=NW, image=image)

    # text = canvas.create_text(100, 40, text="HELLO WORLD",
    #                           fill="white", font=('Helvetica 15 bold'),)
    # r = canvas.create_rectangle(canvas.bbox(text), fill="black")
    # canvas.tag_lower(r, text)

    canvas.pack(padx=5, pady=5)

    # label.pack(padx=5, pady=5)
    frame.pack()

    def quit(event):
        sr.destroy()
        top.deiconify()
    sr.bind('<Escape>', quit)
    sr.focus_force()

    def actionPress(event):
        global coord
        coord['x1'] = event.x
        coord['y1'] = event.y

    def actionRelease(event):
        if (rect != None):
            canvas.delete(rect)

        global imageCrop
        ss_region = (coord['x1'] + 3, coord['y1'] + 3,
                     coord['x2'] + 6, coord['y2'] + 6)
        ss_img = ImageGrab.grab(ss_region)
        # ------------- CREATE FILE NAME RANDOM
        sr.destroy()
        top.deiconify()
        # image = cv2.imread(filename)
        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(
            ss_img, lang='eng+vie', config='--psm 1')
        textBoxOri.delete(1.0, END)
        textBoxOri.insert(END, text)

    def actionMotion(event):
        global rect
        if (rect != None):
            canvas.delete(rect)
        global coord
        coord['x2'] = event.x
        coord['y2'] = event.y
        rect = canvas.create_rectangle(coord['x1'], coord['y1'], coord['x2'], coord['y2'], fill='',
                                       outline='orange', width=3)

    sr.bind("<ButtonPress-1>", actionPress)
    sr.bind("<ButtonRelease-1>", actionRelease)
    sr.bind("<B1-Motion>", actionMotion)

    global srG
    srG = sr


def screenshot():
    ss_region = (0, 0, screen_width, screen_height)
    ss_img = ImageGrab.grab(ss_region)
    # ------------- CREATE FILE NAME RANDOM
    filename = "{}.png".format(os.getpid())
    ss_img.save(filename)
    return tk.PhotoImage(file=filename)


def executeScreenShot():
    # sr = tk.Toplevel(top)
    # sr.grab_set()
    top.withdraw()
    time.sleep(0.2)
    global image
    image = screenshot()
    open_toplevel_window()


def Translate():
    try:
        txt = textBoxOri.get("1.0", END)
        if (txt == '\n' or txt == '' or txt == None):
            messagebox.showerror("Error", "Điền từ cần dịch vào ô trống")
        else:
            result = translator.translate(
                txt, src="en", dest="vi")
            Text1_1.delete(1.0, END)
            Text1_1.insert(END, result.text)
    except:
        messagebox.showerror("Error", "Something wrong")


# SECTION 1 ----------------------------------------------------------------------------
ScreenshotBtn.configure(command=executeScreenShot)
constant.style_code()

# SECTION 2 ----------------------------------------------------------------------------


# SECTION 3 ----------------------------------------------------------------------------


textBoxOri = tk.Text(top, background="white", font="TkTextFont",
                     foreground="black", highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                     selectbackground="#c4c4c4", selectforeground="black", wrap="word")
textBoxOri.place(x=10, y=330, height=144, width=374)

langugeOrigin = tk.StringVar()

TCombobox2 = ttk.Combobox(top)
TCombobox2.place(x=120, y=300, height=21, width=263)
TCombobox2.configure(values=list(LANGCODES.keys()))
# TCombobox2.bind('<<ComboboxSelected>>', lambda event: Label5.config(
#     text=LANGCODES[langugeOrigin.get()]))
TCombobox2.configure(textvariable=langugeOrigin)
TCombobox2.configure(takefocus="")
TCombobox2.current(get_index('english', constant.list_language))


Label5_1 = tk.Label(top)
Label5_1.place(x=400, y=300, height=21, width=98)
Label5_1.configure(activebackground="#f9f9f9")
Label5_1.configure(anchor='w')
Label5_1.configure(background="#d9d9d9")
Label5_1.configure(compound='left')
Label5_1.configure(disabledforeground="#a3a3a3")
Label5_1.configure(foreground="#000000")
Label5_1.configure(highlightbackground="#d9d9d9")
Label5_1.configure(highlightcolor="black")
Label5_1.configure(text='''Ngôn ngữ đích''')
langueDest = tk.StringVar()
TCombobox2_1 = ttk.Combobox(top)
TCombobox2_1.place(x=490, y=300, height=21, width=264)
TCombobox2_1.configure(values=constant.list_language)
TCombobox2_1.configure(textvariable=langueDest)
TCombobox2_1.configure(takefocus="")
TCombobox2_1.current(get_index('vietnamese', constant.list_language))
Text1_1 = tk.Text(top)
Text1_1.place(x=400, y=330, height=144, width=354)
Text1_1.configure(background="white")
Text1_1.configure(font="TkTextFont")
Text1_1.configure(foreground="black")
Text1_1.configure(highlightbackground="#d9d9d9")
Text1_1.configure(highlightcolor="black")
Text1_1.configure(insertbackground="black")
Text1_1.configure(selectbackground="#c4c4c4")
Text1_1.configure(selectforeground="black")
Text1_1.configure(wrap="word")
Button2 = tk.Button(top)
Button2.place(x=300, y=490, height=34, width=187)
Button2.configure(activebackground="beige")
Button2.configure(activeforeground="black")
Button2.configure(background="#d9d9d9")
Button2.configure(compound='left')
Button2.configure(disabledforeground="#a3a3a3")
Button2.configure(foreground="#000000")
Button2.configure(highlightbackground="#d9d9d9")
Button2.configure(highlightcolor="black")
Button2.configure(pady="0")
Button2.configure(text='''Dịch''')
Button2.configure(command=Translate)


top.mainloop()
