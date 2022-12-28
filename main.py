from tkinter import *
from tkcalendar import *
from datetime import datetime as dt
import requests
import webbrowser
from tkinter import messagebox

# window setup
root = Tk()
root.title("Coding Tracker")
root.iconphoto(True, PhotoImage(file="code.png"))
root.resizable(width=False, height=False)
root.config(pady=20, padx=20)
URL = "https://pixe.la/v1/users/jojowick/graphs/graph1.html"
TODAY = dt.now()


def open_browser():
    webbrowser.open(URL, new=1)


def format_date():
    cal.config(date_pattern="yyyyMMdd")
    date = cal.get_date()
    cal.config(date_pattern="dd/MM/yyyy")
    return date


def add_pixel():
    endpoint = "https://pixe.la/v1/users/jojowick/graphs/graph1/"
    pixel_add = {
        "date": format_date(),
        "quantity": user_in.get(),
    }
    requests.post(url=endpoint, json=pixel_add, headers=headers)
    user_in.delete(0, END)
    messagebox.showinfo(message="Pixel added.")


def del_pixel():
    endpoint = f"https://pixe.la/v1/users/jojowick/graphs/graph1/{format_date()}"
    requests.delete(url=endpoint, headers=headers)
    messagebox.showinfo(message="Pixel deleted.")


def change_pixel():
    endpoint = f"https://pixe.la/v1/users/jojowick/graphs/graph1/{format_date()}"
    pixel_update = {
        "quantity": user_in.get(),
    }
    requests.put(url=endpoint, json=pixel_update, headers=headers)
    user_in.delete(0, END)
    messagebox.showinfo(message="Pixel updated.")


# calender setup
cal = Calendar(root, selectmode="day", year=TODAY.year, month=TODAY.month, day=TODAY.day)
cal.grid(row=0, column=0, columnspan=4)

# label
units = Label(text="Hours:")
units.grid(row=1, column=0, columnspan=2, pady=10, sticky="e")

# entry
user_in = Entry(width=10)
user_in.grid(row=1, column=2, sticky="w")

TOKEN = "brifbi23dif2828fefu"
GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

# buttons
add = Button(text="Add", command=add_pixel)
add.grid(row=2, column=0, pady=10)
update = Button(text="Update", command=change_pixel)
update.grid(row=2, column=1, pady=10, sticky="w")
delete = Button(text="Delete", command=del_pixel)
delete.grid(row=2, column=2, pady=10, sticky="w")
link = Button(text="Show\nGraph", command=open_browser)
link.grid(row=2, column=3)

root.mainloop()
