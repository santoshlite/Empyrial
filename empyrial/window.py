from tkinter import *
from tkinter import font as tkFont

window = Tk()

window.geometry("1440x975")
window.configure(bg = "#000000")
canvas = Canvas(
    window,
    bg = "#00041f",
    height = 975,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

logo = PhotoImage(file='image.png')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(400, 400, image=logo, anchor=NW)

canvas.create_text(
    720, 525,
    text = "By Investors, For Investors",
    fill = "#ffffff",
    font = ("Segoe UI", int(20.0)))

canvas.create_text(
    720, 700,
    text = "Start",
    fill = "#ffffff",
    font = ("Segoe UI", int(15.0)))

print("Empyrial")
window.resizable(False, False)
window.mainloop()
