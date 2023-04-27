import qrcode
import os
from tkinter import *
import customtkinter
from PIL import Image

#tmpimage = Image.open()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")
        self.tmp_pic_path = 'tmpqr.png'

        self.title("HME: Easy QR Generator")
        self.grid_columnconfigure((0,1), weight=1)
        self.resizable(width=False, height=False)
                
        #display area for previewing qr code
        self.picbut = customtkinter.CTkImage(dark_image=Image.open(self.tmp_pic_path), size=(164, 164))
        self.butpic = customtkinter.CTkButton(master=self, border_width=0, fg_color="white", hover_color="white", corner_radius=10, image=self.picbut, text="", width=176, height=176)
        self.butpic.grid(column=1, row=0, padx=12, pady=12)
        #end display area for qr code

        #ui area stuff
        self.uiframe = customtkinter.CTkFrame(self)
        self.uiframe.grid(row=0, column=0, padx=12, pady=12)

        #textbox for text input
        self.uitext = customtkinter.CTkEntry(master=self.uiframe, placeholder_text="QR Contents:")
        self.uitext.grid(padx=8, pady=8)
        #button for update preview
        self.update_button = customtkinter.CTkButton(master=self.uiframe, text="Update", command=self.ub_callback)
        self.update_button.grid(padx=8, pady=8)
        
        #textbox for output file name
        self.uipath = customtkinter.CTkEntry(master=self.uiframe, placeholder_text="File Name:")
        self.uipath.grid(padx=8, pady=8)
        #button for save
        self.save_qr_button = customtkinter.CTkButton(master=self.uiframe, text="Save to File", command=self.sq_callback)
        self.save_qr_button.grid(padx=8, pady=8)
        #button for clear
        #end ui area stuff

    def ub_callback(self):
        if self.uitext.get() == '':
            return
        self.updated_qr = qrcode.QRCode(border=1)
        self.updated_qr.add_data(self.uitext.get())
        self.updated_qr.make()
        self.tmpqr = self.updated_qr.make_image(fill_color=(5, 151, 225))

        self.tmpqr.save(self.tmp_pic_path)
        self.picbut.configure(dark_image=Image.open(self.tmp_pic_path))
        self.butpic.configure(image=self.picbut)

    def sq_callback(self):
        if self.uitext.get() == '':
            return
        self.ub_callback()
        #self.tmpqr = qrcode.make(self.uitext.get())
        if self.uipath.get() == '' or self.uipath.get() == self.tmp_pic_path:
            self.save_path = 'qr_code'
        else:
            self.save_path = self.uipath.get()
        self.save_path += '.png'
        self.tmpqr.save(self.save_path)

                

if __name__ == "__main__":
    setupqr = qrcode.QRCode(border=1)
    setupqr.add_data('EMPTY')       #make tmp file for storing qr codes to eas conversion process
    setupqr.make()
    tmp = setupqr.make_image(fill_color=(5,151,225))  
    tmp.save('tmpqr.png')
    app = App()
    app.mainloop()                  #run ctkinter window
    os.system('del /f tmpqr.png')   #remove tmp file in cleanup
