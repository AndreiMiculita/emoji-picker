import tkinter as tk
from Xlib import display


def mouse_position():
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]


def close_window(event):
    root.destroy()


root = tk.Tk()  # create a Tk root window
root.title("emojiPicker")
w = 300  # width for the Tk root
h = 250  # height for the Tk root

x, y = mouse_position()

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x-w, y))
root.resizable(False, False)

searchBox = tk.Text(root, height=1, width=50)
searchBox.pack()
# searchBox.insert(tk.END, "search")
searchBox.focus_set()

root.bind("<Escape>", close_window)
# root.overrideredirect(True)

root.mainloop()

