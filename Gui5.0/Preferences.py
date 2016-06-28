from tkinter import Frame, Canvas, Scrollbar, Button, Label, Entry
from Keyboard import Keyboard


class Preferences(Frame):
    def __init__(self, master, valves):
        Frame.__init__(self, master, bg='sky blue', width=1366, height=768)
        self.master = master

        self.canvas = Canvas(self, height=640, width=1300, bg='sky blue')
        self.frame = Frame(self.canvas, bg='sky blue')
        self.frame.bind('<Button-1>', self.process_click_out)

        self.scrollbar = Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.scrollbar.configure(activebackground='DarkRed', background='red', width=40)
        self.canvas.configure(yscrollcommand=self.scrollbar.set, scrollregion=[0, 0, 1366, 2100])

        self.scrollbar.pack(side='right', fill='y')
        self.canvas.pack(side='left')
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

        self.keyboard = Keyboard(self.master)

        self.valves = valves
        self.frame.config(bg='sky blue')
        
        index = 0
        while index < 25:
            self.frame.grid_rowconfigure(index, minsize=80)
            self.frame.grid_columnconfigure(index, minsize=150)
            index += 1

        num_label = [Label(self.frame, text='1'),
                     Label(self.frame, text='2'),
                     Label(self.frame, text='3'),
                     Label(self.frame, text='4'),
                     Label(self.frame, text='5'),
                     Label(self.frame, text='6'),
                     Label(self.frame, text='7'),
                     Label(self.frame, text='8'),
                     ]
        row = 1
        for each in num_label:
            each.grid(row=row, column=0)
            each.config(width=3, font=('Lucida Console', 30), bg='sky blue', fg='RoyalBlue4')
            row += 3

        text_label = [Label(self.frame, text='VALVE 1:  '),
                     Label(self.frame, text='ACTION A: '),
                     Label(self.frame, text='ACTION B: '),

                     Label(self.frame, text='VALVE 2:  '),
                     Label(self.frame, text='ACTION A: '),
                     Label(self.frame, text='ACTION B: '),

                     Label(self.frame, text='VALVE 3:  '),
                     Label(self.frame, text='ACTION A: '),
                     Label(self.frame, text='ACTION B: '),

                     Label(self.frame, text='VALVE 4:  '),
                     Label(self.frame, text='ACTION A: '),
                     Label(self.frame, text='ACTION B: '),

                     Label(self.frame, text='VALVE 5:  '),
                     Label(self.frame, text='ACTION A: '),
                     Label(self.frame, text='ACTION B: '),

                     Label(self.frame, text='VALVE 6:  '),
                     Label(self.frame, text='ACTION A: '),
                     Label(self.frame, text='ACTION B: '),

                     Label(self.frame, text='VALVE 7:  '),
                     Label(self.frame, text='ACTION A: '),
                     Label(self.frame, text='ACTION B: '),

                     Label(self.frame, text='VALVE 8:  '),
                     Label(self.frame, text='ACTION A: '),
                     Label(self.frame, text='ACTION B: ')

                     ]
        row = 1
        for each in text_label:
            each.grid(row=row, column=1)
            each.config(width=12, font=('Lucida Console', 30), bg='sky blue', fg='RoyalBlue4')
            row += 1

        self.valve_label = [Label(self.frame, textvariable=self.valves[0].get_name()),
                            Label(self.frame, textvariable=self.valves[1].get_name()),
                            Label(self.frame, textvariable=self.valves[2].get_name()),
                            Label(self.frame, textvariable=self.valves[3].get_name()),
                            Label(self.frame, textvariable=self.valves[4].get_name()),
                            Label(self.frame, textvariable=self.valves[5].get_name()),
                            Label(self.frame, textvariable=self.valves[6].get_name()),
                            Label(self.frame, textvariable=self.valves[7].get_name())]
        row = 1 
        for each in self.valve_label:
            each.grid(row=row, column=2)
            each.config(width=12, font=('Lucida Console', 30), bg='sky blue', fg='RoyalBlue4', anchor='w')
            each.bind('<Button-1>', self.process_click_out)
            row += 3

        self.entry_field = [Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),

                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),

                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text=''),
                            Entry(self.frame, text='')
                            ]
        row = 1
        for each in self.entry_field:
            each.grid(row=row, column=3)
            each.config(width=12, font=('Lucida Console', 30), bg='sky blue', fg='RoyalBlue4')
            each.bind('<Button-1>', self.process_click_in)
            row += 1

        self.action_a_label = [Label(self.frame, textvariable=self.valves[0].get_action_a()),
                               Label(self.frame, textvariable=self.valves[1].get_action_a()),
                               Label(self.frame, textvariable=self.valves[2].get_action_a()),
                               Label(self.frame, textvariable=self.valves[3].get_action_a()),
                               Label(self.frame, textvariable=self.valves[4].get_action_a()),
                               Label(self.frame, textvariable=self.valves[5].get_action_a()),
                               Label(self.frame, textvariable=self.valves[6].get_action_a()),
                               Label(self.frame, textvariable=self.valves[7].get_action_a())
                               ]
        row = 2
        for each in self.action_a_label:
            each.grid(row=row, column=2)
            each.config(width=12, font=('Lucida Console', 30), bg='sky blue', fg='RoyalBlue4', anchor='w')
            each.bind('<Button-1>', self.process_click_out)
            row += 3

        self.action_b_label = [Label(self.frame, textvariable=self.valves[0].get_action_b()),
                               Label(self.frame, textvariable=self.valves[1].get_action_b()),
                               Label(self.frame, textvariable=self.valves[2].get_action_b()),
                               Label(self.frame, textvariable=self.valves[3].get_action_b()),
                               Label(self.frame, textvariable=self.valves[4].get_action_b()),
                               Label(self.frame, textvariable=self.valves[5].get_action_b()),
                               Label(self.frame, textvariable=self.valves[6].get_action_b()),
                               Label(self.frame, textvariable=self.valves[7].get_action_b())
                               ]

        row = 3
        for each in self.action_b_label:
            each.grid(row=row, column=2)
            each.config(width=12, font=('Lucida Console', 30), bg='sky blue', fg='RoyalBlue4', anchor='w')
            each.bind('<Button-1>', self.process_click_out)
            row += 3

        self.lock()

    def process_click_out(self, event):
        self.canvas.configure(height=660)
        self.keyboard.grid_forget()

    def process_click_in(self, event):
        index = 0
        for each in self.entry_field:
            if each == event.widget:
                break
            index += 1

        if event.widget.cget('state') == 'normal':
            self.canvas.configure(height=250)
            self.keyboard.grid(row=2, column=0)
            self.keyboard.set_entry(event.widget)
            self.canvas.yview_moveto(index / 28)

    def lock(self):
        for each in self.entry_field:
            each.config(state='disabled')
    
