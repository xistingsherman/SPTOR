from tkinter import Frame, Canvas, Scrollbar, Label, Button, PhotoImage
from LED_light import LED
import threading
import time
import math


class RunScreen(Frame):
    def __init__(self, master, valves):
        Frame.__init__(self, master, bg='sky blue', width=950, height=750)
        self.master = master
        self.valves = valves
        self.threads = []
        
        self.canvas = Canvas(self, height=750, width=950, bg='sky blue')
        self.frame = Frame(self.canvas, bg='sky blue')
        self.scrollbar = Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.scrollbar.configure(activebackground='DarkRed', background='red', width=40)
        self.canvas.configure(yscrollcommand=self.scrollbar.set, scrollregion=[0, 0, 1366, 1300])

        self.scrollbar.pack(side='right', fill='y')
        self.canvas.pack(side='left')
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

        self.frame.config(bg='sky blue')

        self.valve_num = [Label(self.frame, text='1'),
                            Label(self.frame, text='2'),
                            Label(self.frame, text='3'),
                            Label(self.frame, text='4'),
                            Label(self.frame, text='5'),
                            Label(self.frame, text='6'),
                            Label(self.frame, text='7'),
                            Label(self.frame, text='8')]

        row = 0
        for each in self.valve_num:
            each.grid(row=row, column=0)
            each.config(width=4, font=('Lucida Console', 30), bg='sky blue', fg='RoyalBlue4')
            row += 2

        self.valve_name = [Label(self.frame, textvariable=valves[0].get_name()),
                            Label(self.frame, textvariable=valves[1].get_name()),
                            Label(self.frame, textvariable=valves[2].get_name()),
                            Label(self.frame, textvariable=valves[3].get_name()),
                            Label(self.frame, textvariable=valves[4].get_name()),
                            Label(self.frame, textvariable=valves[5].get_name()),
                            Label(self.frame, textvariable=valves[6].get_name()),
                            Label(self.frame, textvariable=valves[7].get_name())]

        row = 0
        for each in self.valve_name:
            each.grid(row=row, column=2)
            each.config(width=15, font=('Lucida Console', 30), bg='sky blue', fg='RoyalBlue4')
            row += 2

        valve = 0
        self.valve_activity = []
        self.on_image = PhotoImage(file="img/yes.png").subsample(x=6, y=6)
        self.off_image = PhotoImage(file="img/no.png").subsample(x=6, y=6)
        for each in self.valves:
            if each.get_setting() is 'INACTIVE':
                self.valve_activity.append(Button(self.frame, image=self.off_image, text='OFF', command=lambda: self.activate(valve)))
            else:
                self.valve_activity.append(Button(self.frame, image=self.on_image, text='ON', command=lambda: self.activate(valve)))
            valve += 1

        row = 0
        for each in self.valve_activity:
            each.grid(row=row, column=1)
            each.config(bg='SkyBlue4', activebackground='midnight blue')
            each.config()
            row += 2

        self.valve_action_a = [Label(self.frame, textvariable=valves[0].get_action_a()),
                               Label(self.frame, textvariable=valves[1].get_action_a()),
                               Label(self.frame, textvariable=valves[2].get_action_a()),
                               Label(self.frame, textvariable=valves[3].get_action_a()),
                               Label(self.frame, textvariable=valves[4].get_action_a()),
                               Label(self.frame, textvariable=valves[5].get_action_a()),
                               Label(self.frame, textvariable=valves[6].get_action_a()),
                               Label(self.frame, textvariable=valves[7].get_action_a())]

        row = 0
        for each in self.valve_action_a:
            each.grid(row=row, column=3)
            each.config(width=10, font=('Lucida Console', 30), bg='sky blue', fg='RoyalBlue4', anchor='w')
            row += 2

        self.valve_action_b = [Label(self.frame, textvariable=valves[0].get_action_b()),
                               Label(self.frame, textvariable=valves[1].get_action_b()),
                               Label(self.frame, textvariable=valves[2].get_action_b()),
                               Label(self.frame, textvariable=valves[3].get_action_b()),
                               Label(self.frame, textvariable=valves[4].get_action_b()),
                               Label(self.frame, textvariable=valves[5].get_action_b()),
                               Label(self.frame, textvariable=valves[6].get_action_b()),
                               Label(self.frame, textvariable=valves[7].get_action_b())]

        row = 1
        for each in self.valve_action_b:
            each.grid(row=row, column=3)
            each.config(width=10, font=('Lucida Console', 30), bg='sky blue', fg='RoyalBlue4', anchor='w')
            row += 2

        self.lightsA = [LED(self.frame, 30, 'green1', 'green', 'dark green', 'Dark Green', False),
                        LED(self.frame, 30, 'green1', 'green', 'dark green', 'Dark Green', False),
                        LED(self.frame, 30, 'green1', 'green', 'dark green', 'Dark Green', False),
                        LED(self.frame, 30, 'green1', 'green', 'dark green', 'Dark Green', False),
                        LED(self.frame, 30, 'green1', 'green', 'dark green', 'Dark Green', False),
                        LED(self.frame, 30, 'green1', 'green', 'dark green', 'Dark Green', False),
                        LED(self.frame, 30, 'green1', 'green', 'dark green', 'Dark Green', False),
                        LED(self.frame, 30, 'green1', 'green', 'dark green', 'Dark Green', False)
                        ]

        self.lightsB = [LED(self.frame, 30, 'red', 'dark red', 'red4', 'DarkRed', False),
                        LED(self.frame, 30, 'red', 'dark red', 'red4', 'DarkRed', False),
                        LED(self.frame, 30, 'red', 'dark red', 'red4', 'DarkRed', False),
                        LED(self.frame, 30, 'red', 'dark red', 'red4', 'DarkRed', False),
                        LED(self.frame, 30, 'red', 'dark red', 'red4', 'DarkRed', False),
                        LED(self.frame, 30, 'red', 'dark red', 'red4', 'DarkRed', False),
                        LED(self.frame, 30, 'red', 'dark red', 'red4', 'DarkRed', False),
                        LED(self.frame, 30, 'red', 'dark red', 'red4', 'DarkRed', False)
                        ]

    #Turn valve on or off
    def activate(self, index):
        if self.valve_activity[index].cget('text') == 'ON':
            self.valve_activity[index].config(text='OFF', image=self.off_image)
        else:
            self.valve_activity[index].config(text='ON', image=self.on_image)

    #Set up layout of GUI
    def make_frame(self):
        row = 0
        for each in self.lightsA:
            each.grid(row=row, column=4, padx=10, pady=20)
            row += 2

        row = 1
        for each in self.lightsB:
            each.grid(row=row, column=4, padx=10, pady=20)
            row += 2

    #Start all valves, if not disabled. May be able to shut off each valve individually.
    def run_all(self, boolean):
        
        if boolean:

            self.threads = [threading.Thread(target=self.run_valve, args=(0, self.valves[0].get_interval() )),
                            threading.Thread(target=self.run_valve, args=(1, self.valves[1].get_interval() )),
                            threading.Thread(target=self.run_valve, args=(2, self.valves[2].get_interval() )),
                            threading.Thread(target=self.run_valve, args=(3, self.valves[3].get_interval() )),
                            threading.Thread(target=self.run_valve, args=(4, self.valves[4].get_interval() )),
                            threading.Thread(target=self.run_valve, args=(5, self.valves[5].get_interval() )),
                            threading.Thread(target=self.run_valve, args=(6, self.valves[6].get_interval() )),
                            threading.Thread(target=self.run_valve, args=(7, self.valves[7].get_interval() )),
                            ]
            for thread in self.threads:
                thread.start()
            
        else:
            for each in self.valve_activity:
                each.config(text='OFF')
                
    #Individual valve is run.
    def run_valve(self, index, interval):
        run_time = interval[0]
        delay_time = interval[1]

        start_time = math.floor( time.time() )
        
        valve_a_on = True
        delay_on = False
        
        try:

            self.valve_a_on(index)

            while( self.valve_activity[index].cget('text') == 'ON' ):
                
                time_lapse = math.floor( time.time() ) - start_time

                
                if delay_on:
                    if time_lapse > delay_time and not valve_a_on:
                        #Switch from delay to b
                        delay_on = False
                        start_time = math.floor( time.time())
                        self.valve_b_on(index)
                    elif time_lapse > delay_time and valve_a_on:
                        #switch from delay to a
                        delay_on = False
                        valve_a_on = True
                        start_time = math.floor( time.time())
                        self.valve_a_on(index)
                elif valve_a_on:
                    if time_lapse > run_time:
                        #Switching from a to delay
                        valve_a_on = False
                        delay_on = True
                        start_time = math.floor( time.time() )
                        self.valve_delay_all(index)        
                else:
                    if time_lapse > run_time:
                        #Switching from b to delay
                        valve_a_on = True
                        delay_on = True
                        start_time = math.floor( time.time() )
                        self.valve_delay_all(index)
                time.sleep(0.1)

        finally:
            self.valve_delay_all(index)

    #Turn on valve A, and turn off valve B.
    def valve_a_on(self, index):
        self.lightsA[index].set_state(True)
        self.lightsB[index].set_state(False)
        self.master.update()

    #Turn on valve B, and turn off valve A.
    def valve_b_on(self, index):
        self.lightsA[index].set_state(False)
        self.lightsB[index].set_state(True)
        self.master.update()

    #Turn off valves A and B.
    def valve_delay_all(self, index):
        self.lightsA[index].set_state(False)
        self.lightsB[index].set_state(False)
        self.master.update()


