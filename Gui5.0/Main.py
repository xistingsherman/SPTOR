from tkinter import Tk
from Gui import GUI


def main():
    window = Tk()
    window.geometry('1366x768')
    window.attributes('-fullscreen', True)
    window.wm_title('GUIDO')
    gui = GUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()

