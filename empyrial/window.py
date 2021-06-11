from tkinter import *
from tkinter import font as tkFont
from urllib.request import urlopen
from PIL import ImageTk, Image
try:
    # Python 2 support
    from base64 import encodestring
except ImportError:
    # Python 3.9.0+ support
    from base64 import encodebytes as encodestring
import io


def page1(window):
    canvas = Canvas(
    window,
    bg = "#00041f",
    height = 975,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    canvas.place(x = 0, y = 0)
    canvas.pack(side='top', fill='both', expand='yes')

    canvas.create_image(400, 400, image=logo, anchor=NW)

    canvas.create_text(
        720, 525,
        text = "By Investors, For Investors",
        fill = "#ffffff",
        font = ("Segoe UI", int(20.0)))

    def on_enter(e):
        btn['background'] = "#ffd463"

    def on_leave(e):
        btn['background'] = "#ffe49e"

    btn = Button(window, text = 'Start', bd = '0', bg="#ffe49e", command = changepage)
    btn.place(relx=0.5, rely=0.65, anchor=CENTER)
    btn.config(height = 2, width = 15 )
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

def page2(window):
    canvas = Canvas(
    window,
    bg = "#00041f",
    height = 975,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    canvas.place(x = 0, y = 0)

  
    canvas.create_image(60, 60, image=logo2, anchor=NW)

    start = Entry(window) 
    portfolio = Entry(window) 
    allocation = Entry(window) 
    benchmark = Entry(window) 

    canvas.create_text(
        125, 180,
        text = "Start date",
        fill = "#ffffff",
        font = ("Segoe UI", int(11.0)))

    canvas.create_window(250, 180, window=start)

    canvas.create_text(
        125, 220,
        text = "Portfolio",
        fill = "#ffffff",
        font = ("Segoe UI", int(11.0)))

    canvas.create_window(250, 220, window=portfolio)

    canvas.create_text(
        125, 260,
        text = "Allocation",
        fill = "#ffffff",
        font = ("Segoe UI", int(11.0)))

    canvas.create_window(250, 260, window=allocation)

    canvas.create_text(
        125, 300,
        text = "Benchmark",
        fill = "#ffffff",
        font = ("Segoe UI", int(11.0)))

    canvas.create_window(250, 300, window=benchmark)

    def on_enter(e):
        btn['background'] = "#222e40"

    def on_leave(e):
        btn['background'] = "#415778"

    def returnEntry(arg=None):
        """Gets the result from Entry and return it to the Label"""

        result = start.get()
        resultLabel.config(text=result)
        start.delete(0, END)

  
    btn = Button(window, text = 'Backtest', bd = '0', bg="#415778", fg="#ffffff", command=returnEntry)
    btn.place(relx=0.173, rely=0.36, anchor=CENTER)
    btn.config(height = 2, width = 17 )
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    resultLabel = Label(window, text="")
    resultLabel.pack(fill=X)


    


def changepage():
    global pagenum, window
    for widget in window.winfo_children():
        widget.destroy()
    if pagenum == 1:
        page2(window)
        pagenum = 2
    else:
        page1(window)
        pagenum = 1

pagenum = 1
window = Tk()
window.geometry("1440x975")
window.configure(bg = "#00041f")
logo = PhotoImage(file='image\image.png')
logo2 = PhotoImage(file='image\images.png')
page1(window)
window.resizable(False, False)
window.mainloop()
