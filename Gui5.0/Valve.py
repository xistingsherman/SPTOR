from tkinter import StringVar
class Valve:
    def __init__(self, name, setting, action_a, action_b, interval):
        self.name = StringVar()
        self.name.set('Valve')
        self.set_name(name)

        self.setting = setting
        self.interval = interval

        self.action_a = StringVar()
        self.action_a.set('ACTION A')
        self.set_action_a(action_a)

        self.action_b = StringVar()
        self.action_b.set('ACTION B')
        self.set_action_b(action_b)

    def __str__(self):
        string = 'NAME:\t  ' + self.name.get() + '\nACTION A:\t' + self.action_a.get() + '\t\tSETTNG:\t' + self.setting
        string += '\nACTION B:\t' + self.action_b.get() + '\t\tINTERVAL:\t(' + str(self.interval[0]) + ', ' + str(self.interval[1]) + ')\n'
        return string

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name.set(name)

    def get_setting(self):
        return self.setting

    def set_setting(self, setting):
        self.setting = setting

    def get_interval(self):
        return self.interval

    def set_interval(self, interval):
        self.interval = interval

    def get_action_a(self):
        return self.action_a

    def set_action_a(self, action):
        self.action_a.set(action)

    def get_action_b(self):
        return self.action_b

    def set_action_b(self, action):
        self.action_b.set(action)
