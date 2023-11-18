from customtkinter import *
from PIL import Image, ImageGrab
from CTkToolTip import *
from StoreData import *
from CTkMessagebox import CTkMessagebox
from tkinter import StringVar
import time
from googletrans import LANGUAGES
from CTkScrollableDropdown import *
from screeninfo import get_monitors
import tkinter as tk
import easyocr

class App(CTk):
    def __init__(self):
        super().__init__()

        self.reader = easyocr.Reader (['en', 'vi'], gpu=False)

        self.screen_width = 0
        self.screen_height = 0
        self.rect = None

        self.choose_darkmode_var = StringVar(self)
        self.store = StoreData ("./data/global.txt")
        self.list_themes = [_.split(".json")[0] for _ in os.listdir("./themes")]
        self.image = None
        self.trans_y = 0
        self.width_window = 765
        self.height_window = 620
        self.list_language = [*LANGUAGES.values()]
        self.coord = {"x1": 0, "y1": 0, "x2": 0, "y2": 0}

        set_appearance_mode(str(self.store.getData("darkmode", "dark")))
        set_default_color_theme("./themes/" + str(self.store.getData("theme", "Blue")).split(".json")[0] + ".json")

        for m in get_monitors():
            self.screen_width = m.width
            self.screen_height = m.height

        self.geometry(str(self.width_window)+"x"+str(self.height_window))
        self.minsize(120, 1)
        self.maxsize(1924, 1061)
        self.resizable(0,  0)
        self.title("TSApp")
        self.configure(background="#d9d9d9")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="black")

        self.title_label = CTkLabel(master=self, text='''TSAPP - Translate scan app''', font=("Tahoma", 32, "bold"))
        self.title_label.place(x=10, y=10)

        self.my_image = CTkImage(light_image=Image.open("./Image.png"),
                                        dark_image=Image.open("./Image.png"),
                                        size=(240, 200))
        self.image_label = CTkLabel(self, image=self.my_image, text="")  # display image with a CTkLabel

        self.image_label.place(x=480, y=10)

        self.button_trans_screen = CTkButton(master=self, text='Dịch màn hình', font=("Tahoma", 14), command=self.executeScreenshot)
        self.button_trans_screen.place (x=10, y=60 )

        self.button_trans_file = CTkButton(master=self, text='Dịch file ảnh', font=("Tahoma", 14), command=self.executeTransFile)
        self.button_trans_file.place (x=160, y=60 )

        self.setting_label = CTkLabel(master=self, text='''Cài đặt''', font=("Tahoma", 24, "bold"))
        self.setting_label.place(x=10, y=100)

        self.choose_themes_label = CTkLabel(master=self, text='''Chọn theme''', font=("Tahoma", 14))
        self.choose_themes_label.place(x=10, y=140)

        self.choose_themes_cbo = CTkComboBox(self, values=self.list_themes, command=self.choose_themes)
        self.choose_themes_cbo.place (x=100, y=140)

        self.choose_darkmode = CTkCheckBox(master=self, text="Dark mode", command=self.darkmode_command, variable=self.choose_darkmode_var, onvalue="dark", offvalue="light")
        self.choose_darkmode.place (x=280, y=142)

        self.choose_gpu_checkbox = CTkCheckBox(master=self, text='Dùng GPU để scan', font=("Tahoma", 14))
        self.choose_gpu_checkbox.place (x=10, y=180)
        CTkToolTip(self.choose_gpu_checkbox, delay=0.1, message="Dùng GPU để tốc độ truy xuất chữ từ hình ảnh nhanh hơn")

        self.source_trans_label = CTkLabel(master=self, text='''Nguồn dịch''', font=("Tahoma", 14))
        self.source_trans_label.place(x=10, y=220)
        
        self.source_trans_cbo = CTkComboBox(self, values=['Google dịch'])
        self.source_trans_cbo.place (x=100, y=220)

        self.trans_label = CTkLabel(master=self, text='''Dịch thuật''', font=("Tahoma", 24, "bold"))
        self.trans_label.place(x=10, y=265+self.trans_y)

        self.language_origin_label = CTkLabel(master=self, text='''Ngôn ngữ nguồn''', font=("Tahoma", 14))
        self.language_origin_label.place(x=10, y=305+self.trans_y)

        self.language_ori_cbo = CTkComboBox(self)
        self.language_ori_cbo.place (x=125, y=305+self.trans_y)
        CTkScrollableDropdown(self.language_ori_cbo, values=self.list_language, button_color="transparent", frame_corner_radius=4)

        self.language_dest_label = CTkLabel(master=self, text='''Ngôn ngữ đích''', font=("Tahoma", 14))
        self.language_dest_label.place(x=self.width_window / 2 + 10, y=305+self.trans_y)

        self.language_dest_cbo = CTkComboBox(self)
        self.language_dest_cbo.place (x=self.width_window / 2 + 125, y=305+self.trans_y)
        CTkScrollableDropdown(self.language_dest_cbo, values=self.list_language, button_color="transparent", frame_corner_radius=4)

        self.language_ori_textbox = CTkTextbox(master=self, width=self.width_window / 2 - 20, height=200, corner_radius=12)
        self.language_ori_textbox.place (x=10, y=355+self.trans_y)

        self.language_dest_textbox = CTkTextbox(master=self, width=self.width_window / 2 - 20, height=200, corner_radius=12)
        self.language_dest_textbox.place (x=self.width_window / 2 + 10, y=355+self.trans_y)

        self.button_trans_lang = CTkButton(master=self, text='Dịch', font=("Tahoma", 14), width=self.width_window / 2)
        self.button_trans_lang.place (x=self.width_window / 2 - self.width_window / 4, y=570+self.trans_y )

        self.afterEffects()


    def darkmode_command (self):
        set_appearance_mode(self.choose_darkmode_var.get())
        self.store.saveData("darkmode", self.choose_darkmode_var.get())
    
    def choose_themes (self, choice):
        if (self.store.getData("theme", "Blue") != choice):
            self.store.saveData ('theme', choice)
            msg = CTkMessagebox(title="Yêu cầu reset ứng dụng", message="Bạn cần mở lại ứng dụng để được cập nhật giao diện mới!", icon="warning", option_2="Để sau", option_1="Đóng ngay")
            if (msg.get()=="Đóng ngay"):
                self.destroy()
        
    def afterEffects(self):
        self.choose_themes_cbo.set(self.store.getData("theme", "Blue"))
        self.language_ori_cbo.set('english')
        self.language_dest_cbo.set('vietnamese')
        if(str(self.store.getData("darkmode", "dark")) == "dark"):
            self.choose_darkmode.select()
        else: self.choose_darkmode.deselect()
    
    def executeScreenshot(self):
        self.withdraw()
        time.sleep(0.2)
        self.image = self.screenshot()
        self.open_screen()
    
    def screenshot(self):
            ss_region = (0, 0, self.screen_width, self.screen_height)
            ss_img = ImageGrab.grab(ss_region)
            # ------------- CREATE FILE NAME RANDOM
            filename = "{}.png".format(os.getpid())
            ss_img.save(filename)
            return tk.PhotoImage(file=filename)


    def executeTransFile (self):
        # self.reader = easyocr.Reader (['en', 'vi'], gpu=False)
        pass

    def open_screen(self):
        self.sr = tk.Toplevel()
        self.sr.attributes('-fullscreen', True)
        self.frame_sr = tk.Frame(self.sr, background="red")
        self.canvas_sr = tk.Canvas(self.frame_sr, width=self.screen_width,
                       height=self.screen_height,  bd=0, highlightthickness=0, bg='red')
        self.canvas_sr.create_image(0, 0, anchor=NW, image=self.image)
        self.canvas_sr.pack (padx=3, pady=3)
        self.frame_sr.pack()
        
        def quit(event):
            self.sr.destroy()
            self.deiconify()
        
        def actionPress(event):
            self.coord['x1'] = event.x
            self.coord['y1'] = event.y
        
        def actionRelease(event):
            if (self.rect != None):
                self.canvas_sr.delete(self.rect)

            ss_region = (self.coord['x1'] + 3, self.coord['y1'] + 3,
                        self.coord['x2'] + 6, self.coord['y2'] + 6)
            ss_img = ImageGrab.grab(ss_region)
            filename = "{}.png".format(os.getpid())
            ss_img.save(filename)
            result = self.reader.readtext (filename)
            text = ''
            for x in result:
                text += x[1]
            text_sr = self.canvas_sr.create_text(result[0][0][0][0] + self.coord['x1'], result[0][0][0][1] + self.coord['y1'], text=text,
                                        fill="white", font=('Helvetica 15 bold'),)
            r = self.canvas_sr.create_rectangle(self.canvas_sr.bbox(text_sr), fill="black")
            self.canvas_sr.tag_lower(r, text_sr)

            # ------------- CREATE FILE NAME RANDOM
        
        def actionMotion(event):
            if (self.rect != None):
                self.canvas_sr.delete(self.rect)
            self.coord['x2'] = event.x
            self.coord['y2'] = event.y
            self.rect = self.canvas_sr.create_rectangle(self.coord['x1'], self.coord['y1'], self.coord['x2'], self.coord['y2'], fill='',
                                        outline='orange', width=3)


        self.sr.bind("<ButtonPress-1>", actionPress)
        self.sr.bind("<ButtonRelease-1>", actionRelease)
        self.sr.bind("<B1-Motion>", actionMotion)

        self.sr.bind('<Escape>', quit)
        self.sr.focus_force()

if __name__ == "__main__":
    app = App()
    app.mainloop()