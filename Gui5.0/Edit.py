from tkinter import Label, Button, Frame, IntVar, Canvas, Scrollbar, PhotoImage

class Edit(Frame):
    def __init__(self, master, valves):
        Frame.__init__(self, master, bg='sky blue', width=1366, height=768)
        self.master = master

        self.canvas = Canvas(self, height=630, width=1320, bg='sky blue')
        self.frame = Frame(self.canvas, bg='sky blue')
        self.scrollbar = Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.scrollbar.configure(activebackground='DarkRed', background='red', width=40)
        self.canvas.configure(yscrollcommand=self.scrollbar.set, scrollregion=[0, 0, 1366, 800])

        self.scrollbar.pack(side='right', fill='y')
        self.canvas.pack(side='left')
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')
        
        self.valves = valves
        self.frame.config(bg='sky blue')

        index = 0
        while index < 10:
            self.frame.grid_rowconfigure(index, minsize=80)
            self.frame.grid_columnconfigure(index, minsize=30)
            index += 1

        self.frame.grid_columnconfigure(3, minsize=130)
        self.frame.grid_columnconfigure(6, minsize=130)

        interval = Label(self.frame, text='RUN', width=6, font=('Lucida Console', 30))
        interval.grid(row=0, column=2)
        interval.config(bg='sky blue', fg='RoyalBlue4')

        delay = Label(self.frame, text='DELAY', width=6, font=('Lucida Console', 30))
        delay.grid(row=0, column=5)
        delay.config(bg='sky blue', fg='RoyalBlue4')

        self.seconds = [IntVar(),
                        IntVar(),
                        IntVar(),
                        IntVar(),
                        IntVar(),
                        IntVar(),
                        IntVar(),
                        IntVar(),
                        IntVar(),
                        IntVar(),
                        IntVar(),
                        IntVar(),
                        IntVar(),
                        IntVar(),
                        IntVar(),
                        IntVar(),
                        IntVar(),
                        IntVar()]

        for each in self.seconds:
            each.set(0)

        self.set_seconds()

        self.valve_label = [Label(self.frame, textvariable=self.valves[0].get_name()),
                            Label(self.frame, textvariable=self.valves[1].get_name()),
                            Label(self.frame, textvariable=self.valves[2].get_name()),
                            Label(self.frame, textvariable=self.valves[3].get_name()),
                            Label(self.frame, textvariable=self.valves[4].get_name()),
                            Label(self.frame, textvariable=self.valves[5].get_name()),
                            Label(self.frame, textvariable=self.valves[6].get_name()),
                            Label(self.frame, textvariable=self.valves[7].get_name())
                            ]
       
        row = 1
        for each in self.valve_label:
            each.grid(row=row, column=0)
            each.config(width=8, font=('Lucida Console', 30), bg='sky blue', fg='RoyalBlue4')
            row += 1

        self.minus_image = PhotoImage(file="img/minus.png").subsample(x=5, y=5)
        self.minusInterval = [Button(self.frame, image=self.minus_image, command=lambda: self.subtract(0)),
                              Button(self.frame, image=self.minus_image, command=lambda: self.subtract(1)),
                              Button(self.frame, image=self.minus_image, command=lambda: self.subtract(2)),
                              Button(self.frame, image=self.minus_image, command=lambda: self.subtract(3)),
                              Button(self.frame, image=self.minus_image, command=lambda: self.subtract(4)),
                              Button(self.frame, image=self.minus_image, command=lambda: self.subtract(5)),
                              Button(self.frame, image=self.minus_image, command=lambda: self.subtract(6)),
                              Button(self.frame, image=self.minus_image, command=lambda: self.subtract(7)),
                              ]

        row = 1
        for each in self.minusInterval:
            each.grid(row=row, column=1)
            each.config(bg='SkyBlue4', activebackground='midnight blue', fg='white')
            row += 1

        self.labelInterval = [Label(self.frame, textvariable=self.seconds[0]),
                              Label(self.frame, textvariable=self.seconds[1]),
                              Label(self.frame, textvariable=self.seconds[2]),
                              Label(self.frame, textvariable=self.seconds[3]),
                              Label(self.frame, textvariable=self.seconds[4]),
                              Label(self.frame, textvariable=self.seconds[5]),
                              Label(self.frame, textvariable=self.seconds[6]),
                              Label(self.frame, textvariable=self.seconds[7])]
        row = 1
        for each in self.labelInterval:
            each.grid(row=row, column=2)
            each.config(width=4, font=('Lucida Console', 30), bg='sky blue', fg='RoyalBlue4')
            row += 1

        self.plus_image = PhotoImage(file="img/plus.png").subsample(x=5, y=5)
        self.plusInterval = [Button(self.frame, image=self.plus_image, command=lambda: self.add(0)),
                             Button(self.frame, image=self.plus_image, command=lambda: self.add(1)),
                             Button(self.frame, image=self.plus_image, command=lambda: self.add(2)),
                             Button(self.frame, image=self.plus_image, command=lambda: self.add(3)),
                             Button(self.frame, image=self.plus_image, command=lambda: self.add(4)),
                             Button(self.frame, image=self.plus_image, command=lambda: self.add(5)),
                             Button(self.frame, image=self.plus_image, command=lambda: self.add(6)),
                             Button(self.frame, image=self.plus_image, command=lambda: self.add(7)),
                             ]

        row = 1
        for each in self.plusInterval:
            each.grid(row=row, column=3)
            each.config(bg='SkyBlue4', activebackground='midnight blue', fg='white')
            row += 1

        self.minusDelay = [Button(self.frame, image=self.minus_image, command=lambda: self.subtract(8)),
                           Button(self.frame, image=self.minus_image, command=lambda: self.subtract(9)),
                           Button(self.frame, image=self.minus_image, command=lambda: self.subtract(10)),
                           Button(self.frame, image=self.minus_image, command=lambda: self.subtract(11)),
                           Button(self.frame, image=self.minus_image, command=lambda: self.subtract(12)),
                           Button(self.frame, image=self.minus_image, command=lambda: self.subtract(13)),
                           Button(self.frame, image=self.minus_image, command=lambda: self.subtract(14)),
                           Button(self.frame, image=self.minus_image, command=lambda: self.subtract(15)),
                           ]
        row = 1
        for each in self.minusDelay:
            each.grid(row=row, column=4)
            each.config(bg='SkyBlue4', activebackground='midnight blue', fg='white')
            each.config()
            row += 1

        self.labelDelay = [Label(self.frame, textvariable=self.seconds[8]),
                           Label(self.frame, textvariable=self.seconds[9]),
                           Label(self.frame, textvariable=self.seconds[10]),
                           Label(self.frame, textvariable=self.seconds[11]),
                           Label(self.frame, textvariable=self.seconds[12]),
                           Label(self.frame, textvariable=self.seconds[13]),
                           Label(self.frame, textvariable=self.seconds[14]),
                           Label(self.frame, textvariable=self.seconds[15])]
        row = 1
        for each in self.labelDelay:
            each.grid(row=row, column=5)
            each.config(width=4, font=('Lucida Console', 30), bg='sky blue', fg='RoyalBlue4')
            row += 1

        self.plusDelay = [Button(self.frame, image=self.plus_image, command=lambda: self.add(8)),
                          Button(self.frame, image=self.plus_image, command=lambda: self.add(9)),
                          Button(self.frame, image=self.plus_image, command=lambda: self.add(10)),
                          Button(self.frame, image=self.plus_image, command=lambda: self.add(11)),
                          Button(self.frame, image=self.plus_image, command=lambda: self.add(12)),
                          Button(self.frame, image=self.plus_image, command=lambda: self.add(13)),
                          Button(self.frame, image=self.plus_image, command=lambda: self.add(14)),
                          Button(self.frame, image=self.plus_image, command=lambda: self.add(15)),
                          ]
        row = 1
        for each in self.plusDelay:
            each.grid(row=row, column=6)
            each.config(bg='SkyBlue4', activebackground='midnight blue')
            each.config()
            row += 1

        self.motor_image = PhotoImage(file="img/motor.png").subsample(x=5, y=5)
        self.motor = [Button(self.frame, text='MOTOR', image=self.motor_image, command=lambda: self.motor_on(0)),
                      Button(self.frame, text='MOTOR', image=self.motor_image, command=lambda: self.motor_on(1)),
                      Button(self.frame, text='MOTOR', image=self.motor_image, command=lambda: self.motor_on(2)),
                      Button(self.frame, text='MOTOR', image=self.motor_image, command=lambda: self.motor_on(3)),
                      Button(self.frame, text='MOTOR', image=self.motor_image, command=lambda: self.motor_on(4)),
                      Button(self.frame, text='MOTOR', image=self.motor_image, command=lambda: self.motor_on(5)),
                      Button(self.frame, text='MOTOR', image=self.motor_image, command=lambda: self.motor_on(6)),
                      Button(self.frame, text='MOTOR', image=self.motor_image, command=lambda: self.motor_on(7))]

        row = 1
        for each in self.motor:
            each.grid(row=row, column=7)
            each.config(bg='SkyBlue4', activebackground='midnight blue', fg='white')
            each.config()
            row += 1

        self.adv_image = PhotoImage(file="img/options.png").subsample(x=5, y=5)
        self.adv = [Button(self.frame, image=self.adv_image, command=lambda: self.motor_on(0)),
                    Button(self.frame, image=self.adv_image, command=lambda: self.motor_on(1)),
                    Button(self.frame, image=self.adv_image, command=lambda: self.motor_on(2)),
                    Button(self.frame, image=self.adv_image, command=lambda: self.motor_on(3)),
                    Button(self.frame, image=self.adv_image, command=lambda: self.motor_on(4)),
                    Button(self.frame, image=self.adv_image, command=lambda: self.motor_on(5)),
                    Button(self.frame, image=self.adv_image, command=lambda: self.motor_on(6)),
                    Button(self.frame, image=self.adv_image, command=lambda: self.motor_on(7)),
                    ]

        row = 1
        for each in self.adv:
            each.grid(row=row, column=8)
            each.config(bg='SkyBlue4', activebackground='midnight blue', fg='white')
            row += 1
            
        self.set_seconds()
        self.lock()
            
    def lock(self):
        index = 0
        while index < 8:
            self.minusInterval[index].config(state='disabled')
            self.minusDelay[index].config(state='disabled')
            self.plusInterval[index].config(state='disabled')
            self.plusDelay[index].config(state='disabled')
            self.motor[index].config(state='disabled')
            self.adv[index].config(state='disabled')
            index += 1

    def set_seconds(self):
        index = 0
        while index < 8:
            if self.valves[index].get_setting() == 'DEFAULT':
                interval = self.valves[index].get_interval()
                # setting seconds for runtime
                self.seconds[index].set(interval[0])
                # setting seconds for delay
                self.seconds[index + 8].set(interval[1])
            else:
                self.minusInterval[index].config(state='disabled')
                self.minusDelay[index].config(state='disabled')
                self.plusInterval[index].config(state='disabled')
                self.plusDelay[index].config(state='disabled')
            index += 1

    def get_intervals(self):
        return self.seconds

    def motor_on(self, index):

        if self.minusDelay[index].cget('state') == 'normal':
            self.minusInterval[index].config(state='disabled')
            self.minusDelay[index].config(state='disabled')
            self.plusInterval[index].config(state='disabled')
            self.plusDelay[index].config(state='disabled')
            self.adv[index].config(state='disabled')
            self.seconds[index].set(0)
            self.seconds[index + 8].set(0)
        else:
            interval = self.valves[index].get_interval()
            self.minusInterval[index].config(state='normal')
            self.minusDelay[index].config(state='normal')
            self.plusInterval[index].config(state='normal')
            self.plusDelay[index].config(state='normal')
            self.adv[index].config(state='normal')
            self.seconds[index].set(interval[0])
            self.seconds[index + 8].set(interval[1])

    def add(self, number):
        if self.seconds[number].get() < 99:
            self.seconds[number].set(self.seconds[number].get() + 1)

    def subtract(self, number):
        if self.seconds[number].get() > 0:
            self.seconds[number].set(self.seconds[number].get() - 1)
