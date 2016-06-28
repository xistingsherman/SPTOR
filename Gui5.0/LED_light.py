from tkinter import Canvas


class LED(Canvas):
    def __init__(self, parent, radius, color_on, o_color_on, color_off, o_color_off, off_or_on):
        Canvas.__init__(self, parent, borderwidth=0, highlightthickness=0, bg='sky blue')
        padding = 0

        self.color_on = color_on
        self.color_off = color_off
        self.o_color_on = o_color_on
        self.o_color_off = o_color_on

        self.current_color = color_on
        self.outline_color = o_color_on

        self.light = self.create_oval((3, 3, radius, radius), width=radius/5, fill=self.current_color)

        self.set_state(off_or_on)
        (x0, y0, x1, y1) = self.bbox("all")
        radius = (x1-x0) + padding
        self.configure(width=radius, height=radius)

    def set_state(self, off_or_on):
        if off_or_on:
            self.itemconfigure(self.light, fill=self.color_on, outline=self.color_on)
        else:
            self.itemconfigure(self.light, fill=self.color_off, outline=self.color_off)
