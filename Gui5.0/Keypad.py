from tkinter import Tk, Frame, Button, Entry


class Keypad(Frame):
    def __init__(self, master, gui, password):
        Frame.__init__(self, master, bg='sky blue', width=450, height=550)
        self.master.geometry('400x550')
        self.master = master
        self.master.configure(bg='sky blue')
        self.gui = gui
        self.password = password
        self.frame = Frame(master)
        self.frame.pack()
        self.frame.configure(bg='sky blue')

        index = 0
        while index < 5:
            self.frame.grid_rowconfigure(index, minsize=50)
            index += 1

        index = 0
        while index < 5:
            self.frame.grid_columnconfigure(index, minsize=50)
            index += 1

        self.box = Entry(self.frame)

        self.box.grid(row=0, columnspan=3)
        self.box.config(font=('Lucida Console', 78), width=6)

        self.list1 = [Button(self.frame, font=('Lucida Console', 30), text='1', command=lambda: self.bob_print(1)),
                 Button(self.frame, font=('Lucida Console', 30), text='2', command=lambda: self.bob_print(2)),
                 Button(self.frame, font=('Lucida Console', 30), text='3', command=lambda: self.bob_print(3))
                ]

        index = 0
        for each in self.list1:
            each.grid(row=1, column=index)
            each.config(bg='SkyBlue4', activebackground='midnight blue', fg='white', activeforeground='white')
            each.config(height=2, width=4)
            index += 1

        self.list2 = [Button(self.frame, font=('Lucida Console', 30), text='4', command=lambda: self.bob_print(4)),
                 Button(self.frame, font=('Lucida Console', 30), text='5', command=lambda: self.bob_print(5)),
                 Button(self.frame, font=('Lucida Console', 30), text='6', command=lambda: self.bob_print(6))
                ]

        index = 0
        for each in self.list2:
            each.grid(row=2, column=index)
            each.config(bg='SkyBlue4', activebackground='midnight blue', fg='white', activeforeground='white')
            each.config(height=2, width=4)
            index += 1

        self.list3 = [Button(self.frame, font=('Lucida Console', 30), text='7', command=lambda: self.bob_print(7)),
                 Button(self.frame, font=('Lucida Console', 30), text='8', command=lambda: self.bob_print(8)),
                 Button(self.frame, font=('Lucida Console', 30), text='9', command=lambda: self.bob_print(9))
                ]

        index = 0
        for each in self.list3:
            each.grid(row=3, column=index)
            each.config(bg='SkyBlue4', activebackground='midnight blue', fg='white', activeforeground='white')
            each.config(height=2, width=4)
            index += 1

        self.list4 = [Button(self.frame, font=('Lucida Console', 30), text='<', command=lambda: self.bob_print('<')),
                 Button(self.frame, font=('Lucida Console', 30), text='0', command=lambda: self.bob_print(0)),
                 Button(self.frame, font=('Lucida Console', 30), text='E', command=lambda: self.bob_print('E'))
                ]

        index = 0
        for each in self.list4:
            each.grid(row=4, column=index)
            each.config(bg='SkyBlue4', activebackground='midnight blue', fg='white', activeforeground='white')
            each.config(height=2, width=4)
            index += 1

    def bob_print(self, character):
        if not (character is '<' or character is 'E'):
            self.box.insert("end", character)
        elif character is '<':
            string = self.box.get()
            self.box.delete(0, 'end')
            self.box.insert('end', string[:-1])
        else:
            if self.box.get() == self.password:
                self.gui.access_granted()
                self.master.destroy()
            else:
                self.box.delete(0, 'end')
