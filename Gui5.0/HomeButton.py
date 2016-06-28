from tkinter import Button, PhotoImage

class HomeButton(Button):
    def __init__(self, master, command, file_name):
        Button.__init__(self, master, bg='SkyBlue4', command=command, activebackground='midnight blue', border=5)
        image = PhotoImage(file=file_name).subsample(x=4, y=4)
        self.configure(image=image)
        self.image=image