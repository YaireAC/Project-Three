# As creating the design for this project, we have to look at the type of components are being made to determine their connections.
# In this case, the design for this one would be of a calculator.
# Therefore, possibly having 3 GUIs: for user, for physical appearance and math equations stored in it.
# Resulting with many interactions between each other.


"""Project three"""
import tkinter as tk
from tkinter import *


class Directions:
    """Acceptable directions to hang the picture frame"""

    def __init__(self):
        """initializing the stuff"""
        self.root = tk.Tk()

    def mainloop(self):
        """Start this GUI in a window"""
        self.root.mainloop()
        # to make the class more modular. Meaning to choose when certain things happen

    def directions_frame(self):
        print("Now that you know what room and frame you want, decide on where on the wall to hang the frame")
        print("Check on the box for the frame to move to. Frame will move accordingly until you're satisfied")
        master = Tk()
        var1 = IntVar()
        Checkbutton(self.root, text='Up', variable=var1).grid(row=0, sticky=W)
        var2 = IntVar()
        Checkbutton(self.root, text='Down', variable=var2).grid(row=1, sticky=W)
        var3 = IntVar()
        Checkbutton(self.root, text='Nail It', variable=var3).grid(row=2, sticky=W)

    def formation(self, frame_height):
        maximum_height = 10
        if frame_height > maximum_height:
            label = tk.Label(self.root, text="You are putting the frame too high")
            label.pack()
        elif frame_height < 0:
            label = tk.Label(self.root, text="Going too low")
            label.pack()
        else:
            # Additional logic or actions can be added here
            """Appropriate height"""



def main():
    root = tk.Tk()
    directions_app = Directions()
    directions_app.directions_frame()

    frame_height = -1
    directions_app.formation(frame_height)

    root.mainloop()


if __name__ == "__main__":
    main()
