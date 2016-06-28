from tkinter import Frame, Label, Button, Tk, StringVar, PhotoImage, Toplevel
from Edit import Edit
from MomentaryPi2 import Momentary
from Valve import Valve
from Summary import Summary
from Preferences import Preferences
from RunScreen import RunScreen
from Keypad import Keypad
from HomeButton import HomeButton
import csv

class GUI:
    def __init__(self, master):
        self.valves = self.get_valves()

        self.master = master
        self.master.configure(bg='sky blue')
        self.password = '0000'

        self.momentary = Momentary(self.master, self.valves)
        self.edit = Edit(self.master, self.valves)
        self.summary = Summary(self.master, self.valves)
        self.preferences = Preferences(self.master, self.valves)
        self.run_screen = RunScreen(self.master, self.valves)

        self.header = self.make_header(self.master)
        self.home = self.home_page(self.master)
        self.frame = self.home

    def make_header(self, master):
        header = Frame(master, bg='sky blue')

        self.label = StringVar()
        self.label.set('NONE')

        self.start_label = StringVar()
        self.start_label.set('START')
        
        self.lock_label = StringVar()
        self.lock_label.set('LOCKED')

        self.title = Label(header, textvariable=self.label, pady=20, font=('Lucida Console', 50))
        self.title.config(bg='sky blue', fg='RoyalBlue4')

        self.run_image = PhotoImage(file="img/animate.png").subsample(x=5, y=5)
        self.run_button = Button(header, image=self.run_image, command=self.run, bg='SkyBlue4', activebackground='midnight blue', border=5)

        self.start_button = Button(header, textvariable=self.start_label, font=('Lucida Console', 30), command=self.start_stop, height=5)
        self.start_button.config(bg='brown3', activebackground='brown4', fg='white', activeforeground='white', width=10, border=5)

        self.save_image = PhotoImage(file="img/save.png").subsample(x=5, y=5)
        self.save_button = Button(header, image=self.save_image, command=self.save, bg='SkyBlue4', activebackground='midnight blue', border=5)
        self.save_button.config(state='disabled')

        self.reset_image = PhotoImage(file="img/reset.png").subsample(x=5, y=5)
        self.reset_button = Button(header, image=self.reset_image, command=self.reset, bg='SkyBlue4', activebackground='midnight blue', border=5)

        self.home_image = PhotoImage(file="img/home.png").subsample(x=5, y=5)
        self.home_button = Button(header, image=self.home_image, command=self.to_home, bg='SkyBlue4', activebackground='midnight blue', border=5)

        self.locked_image = PhotoImage(file="img/lock.png").subsample(x=5, y=5)
        self.unlocked_image = PhotoImage(file="img/unlock.png").subsample(x=5, y=5)
        self.lock_button = Button(header, image=self.locked_image, command=self.lock, bg='SkyBlue4', activebackground='midnight blue', border=5, textvariable=self.lock_label)

        return header

    def home_page(self, master):
        frame = Frame(master)
        frame.grid(row=0, column=0)

        image = PhotoImage(file="img/guido.gif")
        bg = Label(frame, image=image)
        bg.image = image
        bg.grid(row=0, column=0, rowspan=4, columnspan=2)

        index = 0
        while index < 3:
            frame.grid_columnconfigure(index, minsize=200)
            frame.grid_rowconfigure(index, minsize=80)
            index += 1

        summary_button = HomeButton(frame, self.to_summary, 'img/summary.png')
        summary_button.grid(row=0, column=0, sticky='w')

        edit_button = HomeButton(frame, self.to_edit, 'img/edit.png')
        edit_button.grid(row=0, column=1, sticky='e')

        momentary_button = HomeButton(frame, self.to_momentary, 'img/momentary.png')
        momentary_button.grid(row=1, column=0, sticky='w')

        preferences_button = HomeButton(frame, self.to_pref, 'img/preferences.png')
        preferences_button.grid(row=1, column=1, sticky='e')

        music = HomeButton(frame, self.to_summary, 'img/music.png')
        music.grid(row=2, column=0, sticky='w')

        info = HomeButton(frame, self.to_summary, 'img/info.png')
        info.grid(row=2, column=1, sticky='e')

        return frame

    # CSV file input
    def get_valves(self):
        valves = [Valve('VALVE 1', 'DEFAULT', 'Action A', 'Action B', [0, 0]),
                  Valve('VALVE 2', 'DEFAULT', 'Action A', 'Action B', [0, 0]),
                  Valve('VALVE 3', 'DEFAULT', 'Action A', 'Action B', [0, 0]),
                  Valve('VALVE 4', 'DEFAULT', 'Action A', 'Action B', [0, 0]),
                  Valve('VALVE 5', 'DEFAULT', 'Action A', 'Action B', [0, 0]),
                  Valve('VALVE 6', 'DEFAULT', 'Action A', 'Action B', [0, 0]),
                  Valve('VALVE 7', 'DEFAULT', 'Action A', 'Action B', [0, 0]),
                  Valve('VALVE 8', 'DEFAULT', 'Action A', 'Action B', [0, 0])]

        file = open('data.csv', 'rt', newline='')
        try:
            reader = csv.reader(file, lineterminator='\n')
            index = 0
            for row in reader:
                if index == 0:
                    index += 1
                    continue
                else:
                    run = int(row[4])
                    delay = int(row[5])
                    interval = [run, delay]
                    valves[index - 1] = Valve(row[0], row[1], row[2], row[3], interval)
                index += 1
        finally:
            file.close()
            return valves

    def lock(self):
        if self.lock_label.get() == 'LOCKED':
            window = Toplevel()
            window.geometry('318x550')
            self.keypad = Keypad(window, self, self.password)
        else:
            self.save_button.config(state='disabled')
            self.edit.lock()
            self.preferences.lock()
            self.lock_label.set('LOCKED')
            self.lock_button.config(image=self.locked_image)
        
    def save(self):
        self.save_pref()
        self.save_edit()
        
    def save_edit(self):
        file = open('data.csv', 'w')
        interval = self.edit.get_intervals()
        try:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(('Name', 'Setting', 'Action A', 'Action B', 'Runtime', 'Delaytime'))
            index = 0
            for i in self.valves:
                i.set_interval([interval[index].get(), interval[index + 8].get()])
                valve_interval = i.get_interval()
                if self.edit.plusInterval[index].cget('state') == 'disabled' and self.edit.motor[index].cget('state') != 'disabled':
                    i.set_setting('MOTOR')
                    writer.writerow((i.get_name().get(), i.get_setting(), i.get_action_a().get(), i.get_action_b().get(), 0, 0))
                elif interval[index].get() is 0:
                    i.set_setting('INACTIVE')
                    writer.writerow((i.get_name().get(), i.get_setting(), 'NONE', 'NONE', 0, 0))
                else:
                    i.set_setting('DEFAULT')
                    writer.writerow((i.get_name().get(), i.get_setting(), i.get_action_a().get(), i.get_action_b().get(), valve_interval[0], valve_interval[1]))
                index += 1
        finally:
            file.close()

    # must fix
    def save_pref(self):
        index = 0
        for i in self.valves:
            num = index * 3
            if self.preferences.entry_field[num].get():
                i.set_name(self.preferences.entry_field[num].get())
                self.preferences.entry_field[num].delete(0, 'end')
                
            if self.preferences.entry_field[num + 1].get():
                i.set_action_a(self.preferences.entry_field[num + 1].get())
                self.preferences.entry_field[num + 1].delete(0, 'end')
                
            if self.preferences.entry_field[num + 2].get():
                i.set_action_b(self.preferences.entry_field[num + 2].get())
                self.preferences.entry_field[num + 2].delete(0, 'end')
                
            index += 1
                
    def start_stop(self):
        if self.start_label.get() == 'START':
            self.start_label.set('STOP')
            self.master.update()

            self.run_screen.run_all(True)
            self.home_button.config(state='disabled')
        else:
            self.start_label.set('START')
            self.run_screen.run_all(False)
            self.home_button.config(state='normal')

    def run(self):
        self.summary.grid_remove()
        self.run_button.pack_forget()

        self.run_screen.make_frame()
        self.frame = self.run_screen
        self.frame.grid(row=0, column=0)
        self.header.grid(row=0, column=1)

        self.label.set('RUN')
        self.title.pack(side='top')
        self.start_button.pack()
        self.home_button.pack(side='bottom')

    def to_home(self):
        self.momentary.end_all()
        self.momentary.delete_frame()

        self.lock_button.pack_forget()
        self.run_button.pack_forget()
        self.save_button.pack_forget()
        self.reset_button.pack_forget()
        self.home_button.pack_forget()
        self.start_button.pack_forget()

        self.preferences.grid_remove()
        self.frame.grid_remove()
        self.header.grid_remove()

        self.frame = self.home
        self.frame.grid(row=0, column=0)

    def to_summary(self):
        self.frame.grid_remove()
        self.label.set('SUMMARY')
        self.home_button.pack(side='right')
        self.run_button.pack(side='right')
        self.header.grid(row=0, column=0, columnspan=1, sticky='nsew')
        
        self.title.pack(side='left')

        self.summary = Summary(self.master, self.valves)
        self.frame = self.summary
        self.frame.grid(row=1, column=0)

    def to_edit(self):
        self.frame.grid_remove()
        self.label.set('EDIT PROGRAM')

        self.header.grid(row=0, column=0, columnspan=1, sticky='nsew')
        self.home_button.pack(side='right')
        self.save_button.pack(side='right')
        self.lock_button.pack(side='right')
        self.reset_button.pack(side='right')
        self.title.pack(side='left')

        self.frame = self.edit
        self.frame.grid(row=1, column=0)

    def to_momentary(self):
        self.frame.grid_forget()
        self.label.set('MOMENTARY')

        self.header.grid(row=0, column=0, columnspan=12, sticky='ew')
        self.title.pack(side='left')
        self.home_button.pack(side='right')

        self.momentary.make_frame()

    def to_pref(self):
        self.frame.grid_remove()
        self.label.set('PREFERENCES')
        
        self.header.grid(row=0, column=0, columnspan=1, sticky='nsew')
        self.home_button.pack(side='right')
        self.save_button.pack(side='right')
        self.lock_button.pack(side='right')
        self.reset_button.pack(side='right')
        
        self.title.pack(side='left')

        self.frame = self.preferences
        self.frame.grid(row=1, column=0)

    def reset(self):
        self.master.quit()
        
    def access_granted(self):
        self.lock_label.set('UNLOCKED')
        self.lock_button.config(image=self.unlocked_image)
        self.save_button.config(state='normal')
        index = 0
        while index < 8:
            self.edit.minusInterval[index].config(state='normal')
            self.edit.minusDelay[index].config(state='normal')
            self.edit.plusInterval[index].config(state='normal')
            self.edit.plusDelay[index].config(state='normal')
            self.edit.motor[index].config(state='normal')
            self.edit.adv[index].config(state='normal')
            index += 1

        for each in self.preferences.entry_field:
            each.config(state='normal')
        self.edit.set_seconds()
        self.save_button.config(state='normal')





