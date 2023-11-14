from customtkinter import *
from PIL import Image
import os
from CTkToolTip import *
from StoreData import *
from CTkMessagebox import CTkMessagebox
from tkinter import StringVar
import time

class App(CTk):
    def __init__(self):
        super().__init__()

        self.choose_darkmode_var = StringVar(self)
        self.store = StoreData ("./data/global.txt")
        self.list_themes = [_.split(".json")[0] for _ in os.listdir("./themes")]
        self.image = None

        set_appearance_mode(str(self.store.getData("darkmode", "dark")))
        set_default_color_theme("./themes/" + str(self.store.getData("theme", "Blue")).split(".json")[0] + ".json")

        self.geometry("765x520")
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

        self.button_trans_file = CTkButton(master=self, text='Dịch file ảnh', font=("Tahoma", 14))
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
        if(str(self.store.getData("darkmode", "dark")) == "dark"):
            self.choose_darkmode.select()
        else: self.choose_darkmode.deselect()
    
    def executeScreenshot(self):
        self.withdraw()
        time.sleep(0.2)
        self.image = self.screenshot()
        self.open_screen()
    
    def screenshot(self):
            pass


    def open_screen(self):
        self.sr = CTkToplevel()
        self.sr.attributes('-fullscreen', True)
        self.frame_sr = CTkFrame(self.sr, background="red")
        self.frame_sr.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()