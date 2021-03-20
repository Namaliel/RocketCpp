import numpy
import turtle
from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master

def main():

    root = Tk()
    app = Window(root)

    root.wm_title("Tkinter window")
    root.mainloop()

if __name__=="__main__":

    main()
