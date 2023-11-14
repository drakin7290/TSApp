import os.path
import sys
import tkinter.ttk as ttk
from googletrans import LANGUAGES

# ------------ DEFINE
path_to_tesseract = r".\ocr\tesseract.exe"

# -----------------------

script = sys.argv[0]
location = os.path.dirname(script)
bgcolor = '#d9d9d9'  # X11 color: 'gray85'
fgcolor = '#000000'  # X11 color: 'black'
compcolor = 'gray40'  # X11 color: #666666
ana1color = '#c3c3c3'  # Closest X11 color: 'gray76'
ana2color = 'beige'  # X11 color: #f5f5dc
tabfg1 = 'black'
tabfg2 = 'black'
tabbg1 = 'grey75'
tabbg2 = 'grey89'
bgmode = 'light'
style_code_ran = 0
list_language = [*LANGUAGES.values()]

# -------------------------


def style_code():
    global style_code_ran
    if style_code_ran:
        return
    style = ttk.Style()
    if sys.platform == "win32":
        style.theme_use('winnative')
    style.configure('.', background=bgcolor)
    style.configure('.', foreground=fgcolor)
    style.configure('.', font='TkDefaultFont')
    style.map('.', background=[
              ('selected', compcolor), ('active', ana2color)])
    if bgmode == 'dark':
        style.map('.', foreground=[('selected', 'white'), ('active', 'white')])
    else:
        style.map('.', foreground=[('selected', 'black'), ('active', 'black')])
    style_code_ran = 1

