from tkinter import Frame, Button, Entry


class Keyboard(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg='sky blue', width=1366, height=768)
        self.master = master
        self.master.configure(bg='sky blue')
        
        self.configure(bg='sky blue')
        self.current_character = ''
        self.entry = Entry()

        index = 0
        while index < 4:
            self.grid_rowconfigure(index, minsize=80)
            index += 1

        index = 0
        while index < 12:
            self.grid_columnconfigure(index, minsize=80)
            index += 1

        self.list1 = [Button(self, font=('Lucida Console', 30), text='1', command=lambda: self.bob_print('1')),
                 Button(self, font=('Lucida Console', 30), text='2', command=lambda: self.bob_print('2')),
                 Button(self, font=('Lucida Console', 30), text='3', command=lambda: self.bob_print('3')),
                 Button(self, font=('Lucida Console', 30), text='4', command=lambda: self.bob_print('4')),
                 Button(self, font=('Lucida Console', 30), text='5', command=lambda: self.bob_print('5')),
                 Button(self, font=('Lucida Console', 30), text='6', command=lambda: self.bob_print('6')),
                 Button(self, font=('Lucida Console', 30), text='7', command=lambda: self.bob_print('7')),
                 Button(self, font=('Lucida Console', 30), text='8', command=lambda: self.bob_print('8')),
                 Button(self, font=('Lucida Console', 30), text='9', command=lambda: self.bob_print('9')),
                 Button(self, font=('Lucida Console', 30), text='0', command=lambda: self.bob_print('0')),
                 Button(self, font=('Lucida Console', 30), text='<', command=lambda: self.bob_print('<'))
                ]

        index = 0
        for each in self.list1:
            each.grid(row=0, column=index, sticky='w')
            each.config(bg='SkyBlue4', activebackground='midnight blue', fg='white', activeforeground='white')

            index += 1

        self.list2 = [Button(self, font=('Lucida Console', 30), text='Q', command=lambda: self.bob_print('Q')),
                 Button(self, font=('Lucida Console', 30), text='W', command=lambda: self.bob_print('W')),
                 Button(self, font=('Lucida Console', 30), text='E', command=lambda: self.bob_print('E')),
                 Button(self, font=('Lucida Console', 30), text='R', command=lambda: self.bob_print('R')),
                 Button(self, font=('Lucida Console', 30), text='T', command=lambda: self.bob_print('T')),
                 Button(self, font=('Lucida Console', 30), text='Y', command=lambda: self.bob_print('Y')),
                 Button(self, font=('Lucida Console', 30), text='U', command=lambda: self.bob_print('U')),
                 Button(self, font=('Lucida Console', 30), text='I', command=lambda: self.bob_print('I')),
                 Button(self, font=('Lucida Console', 30), text='O', command=lambda: self.bob_print('O')),
                 Button(self, font=('Lucida Console', 30), text='P', command=lambda: self.bob_print('P'))
                ]

        index = 0
        for each in self.list2:
            char = self.list2[index].cget('text')
            each.grid(row=1, column=index, sticky='e')
            each.config(bg='SkyBlue4', activebackground='midnight blue', fg='white', activeforeground='white')
            index += 1

        self.list3 = [Button(self, font=('Lucida Console', 30), text='A', command=lambda: self.bob_print('A')),
                 Button(self, font=('Lucida Console', 30), text='S', command=lambda: self.bob_print('S')),
                 Button(self, font=('Lucida Console', 30), text='D', command=lambda: self.bob_print('D')),
                 Button(self, font=('Lucida Console', 30), text='F', command=lambda: self.bob_print('F')),
                 Button(self, font=('Lucida Console', 30), text='G', command=lambda: self.bob_print('G')),
                 Button(self, font=('Lucida Console', 30), text='H', command=lambda: self.bob_print('H')),
                 Button(self, font=('Lucida Console', 30), text='J', command=lambda: self.bob_print('J')),
                 Button(self, font=('Lucida Console', 30), text='K', command=lambda: self.bob_print('K')),
                 Button(self, font=('Lucida Console', 30), text='L', command=lambda: self.bob_print('L')),
                 Button(self, font=('Lucida Console', 30), text='-', command=lambda: self.bob_print('-'))
                ]

        index = 0
        for each in self.list3:
            each.grid(row=2, column=index, sticky='w')
            each.config(bg='SkyBlue4', activebackground='midnight blue', fg='white', activeforeground='white' )
            index += 1

        self.list4 = [Button(self, font=('Lucida Console', 30), text='Z', command=lambda: self.bob_print('Z')),
                 Button(self, font=('Lucida Console', 30), text='X', command=lambda: self.bob_print('X')),
                 Button(self, font=('Lucida Console', 30), text='C', command=lambda: self.bob_print('C')),
                 Button(self, font=('Lucida Console', 30), text='V', command=lambda: self.bob_print('V')),
                 Button(self, font=('Lucida Console', 30), text='B', command=lambda: self.bob_print('B')),
                 Button(self, font=('Lucida Console', 30), text='N', command=lambda: self.bob_print('N')),
                 Button(self, font=('Lucida Console', 30), text='M', command=lambda: self.bob_print('M')),
                 Button(self, font=('Lucida Console', 30), text='.', command=lambda: self.bob_print('.'))
                ]

        index = 1
        for each in self.list4:
            each.grid(row=3, column=index)
            each.config(bg='SkyBlue4', activebackground='midnight blue', fg='white', activeforeground='white')
            index += 1

    def set_entry(self, field):
        self.entry = field

    # def get_character(self):
    #     return self.current_character

    def bob_print(self, name):
        if name != '<' and len(self.entry.get()) < 7:
            self.entry.insert('end', name)
        else:
            string = self.entry.get()
            self.entry.delete(0, 'end')
            self.entry.insert(0, string[:-1])

# window = Tk()
# window.geometry('900x400')
# window.wm_title('GUIDO')
# gui = Keyboard(window)
# window.mainloop()

