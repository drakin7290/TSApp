import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import constant

top = tk.Tk()
top.geometry("765x520")
top.minsize(120, 1)
top.maxsize(1924, 1061)
top.resizable(0,  0)
top.title("TSApp")
top.configure(background="#d9d9d9")
top.configure(highlightbackground="#d9d9d9")
top.configure(highlightcolor="black")

# SECTION 1 ----------------------------------------------------------------------------
Title = tk.Label(top, activebackground="#f9f9f9", anchor='w',
                 background="#d9d9d9", compound='left', disabledforeground="#a3a3a3",
                 font="-family {Tahoma} -size 20 -weight bold", foreground="#000000",
                 highlightbackground="#d9d9d9", highlightcolor="black", text='''TSAPP - Dịch màn hình máy tính''')
Title.place(x=10, y=0, height=42, width=449)

DesScreenShotLabel = tk.Label(
    top, activebackground="#f9f9f9", anchor='w', background="#d9d9d9", compound='left',
    disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 14", foreground="#000000",
    highlightbackground="#d9d9d9", highlightcolor="black", text='''Nhấn nút để chụp màn hình''')
DesScreenShotLabel.place(x=10, y=50, height=36, width=249)

ScreenshotBtn = tk.Button(
    top, activebackground="beige", activeforeground="black", background="#d9d9d9", compound='left', disabledforeground="#a3a3a3",
    foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Dịch màn hình''')
ScreenshotBtn.place(x=260, y=50, height=34, width=157)

menubar = tk.Menu(top, font="TkMenuFont",
                  bg=constant.bgcolor, fg=constant.fgcolor)
top.configure(menu=menubar)


# ---------------------- SEPERATOR-------------------------
TSeparator1 = ttk.Separator(top)
TSeparator1.place(x=0, y=120, width=768)

# ---------------------- SEPERATOR-------------------------
TSeparator2 = ttk.Separator(top)
TSeparator2.place(x=0, y=260, width=768)

# ---------------------- SEPERATOR-------------------------
TSeparator3 = ttk.Separator(top)
TSeparator3.place(x=390, y=260, height=214)
TSeparator3.configure(orient="vertical")


# SECTION 2 ----------------------------------------------------------------------------
LabelSetting = tk.Label(top, activebackground="#f9f9f9",
                        anchor='w', background="#d9d9d9", compound='left', disabledforeground="#a3a3a3",
                        font="-family {Segoe UI Historic} -size 14 -weight bold", foreground="#000000",
                        highlightbackground="#d9d9d9", highlightcolor="black", text='''Cài đặt''')
LabelSetting.place(x=10, y=130, height=31, width=73)

LabelSourceTrans = tk.Label(top, activebackground="#f9f9f9",
                            anchor='w', background="#d9d9d9", compound='left', disabledforeground="#a3a3a3", foreground="#000000",
                            highlightbackground="#d9d9d9", highlightcolor="black", text='''Nguồn dịch''')
LabelSourceTrans.place(x=20, y=170, height=21, width=69)

soureTrans = tk.StringVar()
list_source_trans = ['Google Dịch']
comboSourceTrans = ttk.Combobox(
    top, values=list_source_trans, textvariable=soureTrans, takefocus="")
comboSourceTrans.place(x=100, y=170, height=21, width=143)
comboSourceTrans.current(0)

# SECTION 3 ----------------------------------------------------------------------------
LabelTitleTrans = tk.Label(
    top, activebackground="#f9f9f9", anchor='w', background="#d9d9d9", compound='left', disabledforeground="#a3a3a3",
    font="-family {Segoe UI Historic} -size 14 -weight bold", foreground="#000000", highlightbackground="#d9d9d9",
    highlightcolor="black", text='''Dịch''')
LabelTitleTrans.place(x=10, y=270, height=31, width=73)

LabelOriCombo = tk.Label(top, activebackground="#f9f9f9",
                         anchor='w', background="#d9d9d9", compound='left', disabledforeground="#a3a3a3", foreground="#000000",
                         highlightbackground="#d9d9d9", highlightcolor="black", text='''Ngôn ngữ nguồn''')
LabelOriCombo.place(x=10, y=300, height=21, width=98)
