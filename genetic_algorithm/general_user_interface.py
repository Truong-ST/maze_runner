from tkinter import *


class GeneralUserInterface:
    def __init__(self, title, w, h):
        self.window = Tk()
        self.window.title(title)
        self.window.geometry('{0}x{1}'.format(w, h))


    def block_entry(self, nameTab, label, column, row, isVertical=0):
        """
        isVertical : int (1 <-> vertical)
        """
        Label(nameTab, text = label).grid(column = column, row = row, sticky = W, pady = 5)
        entry = Entry(nameTab)

        if isVertical == 1:
            entry.grid(column = column, row = row + 1, sticky = W)
        else:
            entry.grid(column = column + 1, row = row, sticky = W)

        return entry