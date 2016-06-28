from tkinter import Frame, Text, Scrollbar


class Summary(Frame):
    def __init__(self, master, valves):
        Frame.__init__(self, master)

        scrollbar = Scrollbar(self)
        scrollbar.pack(side='right', fill='y')
        scrollbar.config(background='red', activebackground='DarkRed', width=40)

        text = Text(self, wrap='word', yscrollcommand=scrollbar.set, width=52, height=14, padx=10)
        text.config(font=('Lucida Console', 30), bg='sky blue', fg='RoyalBlue4')
        text.pack()

        index = 1
        for each in valves:
            text.insert('end', 'VALVE ' + str(index) + '\n\n')
            text.insert('end', each)
            text.insert('end', '-------------------------------------------------------\n')
            index += 1

        scrollbar.config(command=text.yview)


