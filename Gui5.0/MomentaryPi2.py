from tkinter import Label, Frame, Radiobutton, IntVar, Tk, Button, PhotoImage
from LED_light import LED
#1366 x 768

import wiringpi

pin_base = 65       # lowest available starting number is 65
i2c_addr = 0x21     # A0, A1, A2 pins all wired to GND

wiringpi.wiringPiSetup()                    # initialise wiringpi
wiringpi.mcp23017Setup(pin_base, i2c_addr)   # set up the pins and i2c address

wiringpi.pinMode(65, 1)
wiringpi.digitalWrite(65, 0)
wiringpi.pinMode(66, 1)
wiringpi.digitalWrite(66, 0)
wiringpi.pinMode(67, 1)
wiringpi.digitalWrite(67, 0)
wiringpi.pinMode(68, 1)
wiringpi.digitalWrite(68, 0)
wiringpi.pinMode(69, 1)
wiringpi.digitalWrite(69, 0)
wiringpi.pinMode(70, 1)
wiringpi.digitalWrite(70, 0)
wiringpi.pinMode(71, 1)
wiringpi.digitalWrite(71, 0)
wiringpi.pinMode(72, 1)
wiringpi.digitalWrite(72, 0)
wiringpi.pinMode(73, 1)
wiringpi.digitalWrite(73, 0)
wiringpi.pinMode(74, 1)
wiringpi.digitalWrite(74, 0)
wiringpi.pinMode(75, 1)
wiringpi.digitalWrite(75, 0)
wiringpi.pinMode(76, 1)
wiringpi.digitalWrite(76, 0)
wiringpi.pinMode(77, 1)
wiringpi.digitalWrite(77, 0)
wiringpi.pinMode(78, 1)
wiringpi.digitalWrite(78, 0)
wiringpi.pinMode(79, 1)
wiringpi.digitalWrite(79, 0)
wiringpi.pinMode(80, 1)
wiringpi.digitalWrite(80, 0)
wiringpi.pinMode(81, 1)
wiringpi.digitalWrite(81, 0)
wiringpi.pinMode(82, 1)
wiringpi.digitalWrite(82, 0)

class Momentary:
    def __init__(self, master, valves):
        self.valves = valves

        self.master = master
        self.frame1 = Frame(master)
        self.frame2 = Frame(master)

        self.master.configure(bg='sky blue')
        self.frame1.configure(bg='sky blue')
        self.frame2.configure(bg='sky blue')

        index = 0
        while index < 6:
            self.frame1.grid_columnconfigure(index, minsize=6)
            self.frame2.grid_columnconfigure(index, minsize=6)

            self.frame1.grid_rowconfigure(index, minsize=140)
            self.frame2.grid_rowconfigure(index, minsize=140)
            index += 1

        self.end_all_image = PhotoImage(file="img/stop.png").subsample(x=6, y=6)
        self.end_all_button = Button(self.master, image=self.end_all_image, command=lambda: self.end_all() )
        self.end_all_button.config(bg='brown3', activebackground='brown4', border=5, width=850)

        self.label = [Label(self.frame1, textvariable=self.valves[0].get_name()),
                      Label(self.frame1, textvariable=self.valves[1].get_name()),
                      Label(self.frame1, textvariable=self.valves[2].get_name()),
                      Label(self.frame1, textvariable=self.valves[3].get_name()),
                      Label(self.frame2, textvariable=self.valves[4].get_name()),
                      Label(self.frame2, textvariable=self.valves[5].get_name()),
                      Label(self.frame2, textvariable=self.valves[6].get_name()),
                      Label(self.frame2, textvariable=self.valves[7].get_name())]

        row = 0
        for each in self.label:
            each.config(width=7, height=2)
            each.config(bg='sky blue', fg='RoyalBlue4', font=('Lucida Console', 30), padx=18)
            each.grid(row=row % 4, column=0)
            row += 1

        self.lightsA = [LED(self.frame1, 30, 'green1', 'green', 'dark green', 'Dark Green', False),
                        LED(self.frame1, 30, 'green1', 'green', 'dark green', 'Dark Green', False),
                        LED(self.frame1, 30, 'green1', 'green', 'dark green', 'Dark Green', False),
                        LED(self.frame1, 30, 'green1', 'green', 'dark green', 'Dark Green', False),
                        LED(self.frame2, 30, 'green1', 'green', 'dark green', 'Dark Green', False),
                        LED(self.frame2, 30, 'green1', 'green', 'dark green', 'Dark Green', False),
                        LED(self.frame2, 30, 'green1', 'green', 'dark green', 'Dark Green', False),
                        LED(self.frame2, 30, 'green1', 'green', 'dark green', 'Dark Green', False)
                        ]

        self.lightsB = [LED(self.frame1, 30, 'red', 'dark red', 'red4', 'DarkRed', False),
                        LED(self.frame1, 30, 'red', 'dark red', 'red4', 'DarkRed', False),
                        LED(self.frame1, 30, 'red', 'dark red', 'red4', 'DarkRed', False),
                        LED(self.frame1, 30, 'red', 'dark red', 'red4', 'DarkRed', False),
                        LED(self.frame2, 30, 'red', 'dark red', 'red4', 'DarkRed', False),
                        LED(self.frame2, 30, 'red', 'dark red', 'red4', 'DarkRed', False),
                        LED(self.frame2, 30, 'red', 'dark red', 'red4', 'DarkRed', False),
                        LED(self.frame2, 30, 'red', 'dark red', 'red4', 'DarkRed', False)
                        ]

        self.v = [IntVar(),
                  IntVar(),
                  IntVar(),
                  IntVar(),
                  IntVar(),
                  IntVar(),
                  IntVar(),
                  IntVar()]

        for each in self.v:
            each.set(3)

        self.a = [Radiobutton(self.frame1, text='A', command=lambda: self.activate_a(0), value=1),
                  Radiobutton(self.frame1, text='A', command=lambda: self.activate_a(1), value=1),
                  Radiobutton(self.frame1, text='A', command=lambda: self.activate_a(2), value=1),
                  Radiobutton(self.frame1, text='A', command=lambda: self.activate_a(3), value=1),
                  Radiobutton(self.frame2, text='A', command=lambda: self.activate_a(4), value=1),
                  Radiobutton(self.frame2, text='A', command=lambda: self.activate_a(5), value=1),
                  Radiobutton(self.frame2, text='A', command=lambda: self.activate_a(6), value=1),
                  Radiobutton(self.frame2, text='A', command=lambda: self.activate_a(7), value=1)]

        index = 0
        for each in self.a:
            each.grid(row=index % 4, column=2)
            each.config(width=4, height=2,  indicatoron=0, variable=self.v[index], font=('Lucida Console', 30))
            each.config(bg='SkyBlue4', activebackground='midnight blue', selectcolor='midnight blue', fg='white')
            each.config(activeforeground='white')
            index += 1

        self.b = [Radiobutton(self.frame1, text='B', command=lambda: self.activate_b(0), value=0),
                  Radiobutton(self.frame1, text='B', command=lambda: self.activate_b(1), value=0),
                  Radiobutton(self.frame1, text='B', command=lambda: self.activate_b(2), value=0),
                  Radiobutton(self.frame1, text='B', command=lambda: self.activate_b(3), value=0),
                  Radiobutton(self.frame2, text='B', command=lambda: self.activate_b(4), value=0),
                  Radiobutton(self.frame2, text='B', command=lambda: self.activate_b(5), value=0),
                  Radiobutton(self.frame2, text='B', command=lambda: self.activate_b(6), value=0),
                  Radiobutton(self.frame2, text='B', command=lambda: self.activate_b(7), value=0)]

        index = 0
        for each in self.b:
            each.grid(row=index % 4, column=3)
            each.config(width=4, height=2,  indicatoron=0, variable=self.v[index], font=('Lucida Console', 30))
            each.config(bg='SkyBlue4', activebackground='midnight blue', selectcolor='midnight blue', fg='white')
            each.config(activeforeground='white')
            index += 1

        self.end_image = PhotoImage(file="img/no.png").subsample(x=6, y=6)
        self.end_button = [Radiobutton(self.frame1, image=self.end_image, command=lambda: self.end(0)),
                           Radiobutton(self.frame1, image=self.end_image, command=lambda: self.end(1)),
                           Radiobutton(self.frame1, image=self.end_image, command=lambda: self.end(2)),
                           Radiobutton(self.frame1, image=self.end_image, command=lambda: self.end(3)),
                           Radiobutton(self.frame2, image=self.end_image, command=lambda: self.end(4)),
                           Radiobutton(self.frame2, image=self.end_image, command=lambda: self.end(5)),
                           Radiobutton(self.frame2, image=self.end_image, command=lambda: self.end(6)),
                           Radiobutton(self.frame2, image=self.end_image, command=lambda: self.end(7)),
                           ]

        index = 0
        for each in self.end_button:
            each.grid(row=index % 4, column=5)
            each.config(value=2, variable=self.v[index], indicatoron=0)
            each.config(bg='brown3', activebackground='brown4')
            index += 1
        

    def make_frame(self):
        self.frame1.grid(row=2, column=0, rowspan=5)
        self.frame2.grid(row=2, column=1, rowspan=5)
        self.end_all_button.grid(row=1, column=0, columnspan=2)

        row = 0
        for each in self.lightsA:
            each.grid(row=row % 4, column=1, padx=20, pady=20)
            row += 1

        row = 0
        for each in self.lightsB:
            each.grid(row=row % 4, column=4, padx=20, pady=20)
            row += 1


    def delete_frame(self):
        self.frame1.grid_remove()
        self.frame2.grid_remove()
        self.end_all_button.grid_remove()

        for each in self.lightsA:
            each.grid_remove()

        for each in self.lightsB:
            each.grid_remove()

    def activate_a(self, number):
        pin_number = 65 + number
        pin_opposite = 80 - number

        if self.v[number].get() == 1:
            self.lightsA[number].set_state(True)
            self.lightsB[number].set_state(False)
            
            wiringpi.digitalWrite(pin_number, 1)
            wiringpi.digitalWrite(pin_opposite, 0)

    def activate_b(self, number):
        pin_number = 80 - number
        pin_opposite = 65 + number

        if self.v[number].get() == 0:
            self.lightsA[number].set_state(False)
            self.lightsB[number].set_state(True)
            wiringpi.digitalWrite(pin_number, 1)
            wiringpi.digitalWrite(pin_opposite, 0)
            

    def end(self, number):
        pin_number = 65 + number
        pin_opposite = 80 - number

        wiringpi.digitalWrite(pin_number, 0)
        wiringpi.digitalWrite(pin_opposite, 0)

        self.v[number].set(3)
        self.lightsA[number].set_state(False)
        self.lightsB[number].set_state(False)

    def end_all(self):
        number = 0
        while number < 8:
            self.end(number)
            number += 1

