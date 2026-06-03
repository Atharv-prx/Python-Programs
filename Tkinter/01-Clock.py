from tkinter import *
from time import *

def update():
    # strftime converts tuple or struct representation a time as returned by gmtime() or localtime() to a string as specified by format arguments 
    current_time = strftime("%H:%M:%S %p") # %H - Hour (24-hour clock) as a zero-padded decimal number, %M - Minute as a zero-padded decimal number, %S - Second as a zero-padded decimal number, %p - Locale’s equivalent of either AM or PM.
    time_label.config(text=current_time) # text=current_time sets the text of the label to the current time

    current_day = strftime("%A") # %A - Weekday as locale’s full name.
    day_label.config(text=current_day) # text=current_day sets the text of the label to the current day

    current_date = strftime("%B %d, %Y") # %B - Month as locale’s full name, %d - Day of the month as a zero-padded decimal number, %Y - Year with century as a decimal number.
    date_label.config(text=current_date) # text=current_date sets the text of the label to

    window.after(1000, update) # after() method is used to schedule a function to be called after a given number of milliseconds. In this case, it calls the update() function every 1000 milliseconds (1 second) to update the time displayed on the label.
    
window = Tk()

time_label = Label(window, font=("Arial", 50), bg="black", fg="#00FF00")
time_label.pack()

day_label = Label(window, font=("Ink Free", 25))
day_label.pack()

date_label = Label(window, font=("Ink Free", 30))
date_label.pack()

update()

window.mainloop()