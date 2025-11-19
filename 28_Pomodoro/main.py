import tkinter as tk
from PIL import ImageTk, Image
import os
import time


#########################################
#########################################
# GLOBAL VARIABLES
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25       # 25 default
SHORT_BREAK_MIN = 5 #5 
LONG_BREAK_MIN = 20 # 20
reps = 0
timer = None

# pomodoro = ["WORK", "SHORT_BREAK", "WORK", "SHORT_BREAK", "WORK", "SHORT_BREAK","WORK", "LONG_BREAK"]

stop_running = False

#################################################
#################################################
#  Functions

def reset_timer():
    global timer, reps
    window.after_cancel(timer)

    task_name.configure(text="TIMER", foreground=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    reps = 0

    ticks.configure(text="", foreground=GREEN)



def countdown(count):
    global reps, timer
    minutes = count//60
    seconds = count%60
    min_str = ""
    sec_str = ""
    if minutes < 10:
        min_str = f"0{minutes}"
    else:
        min_str = f"{minutes}"
    if seconds < 10:
        sec_str = f"0{seconds}"
    else:
        sec_str = f"{seconds}"
    canvas.itemconfig(timer_text, text=f"{min_str}:{sec_str}")
    if count > 0:
        timer = window.after(10, countdown, count-1)
    else:
        start_timer()
        tick_marks = ""
        for _ in range(int(reps/2)):
            tick_marks += "✓"
        
        ticks.configure(text=tick_marks, foreground=GREEN)

        

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        task_name.configure(text="LONG-BREAK", foreground=RED)
        countdown(long_break_sec)
        reset_timer()
    elif reps%2 == 0:
        task_name.configure(text="SHORT BREAK", foreground=PINK)
        countdown(short_break_sec)
    else:
        task_name.configure(text="WORK", foreground=GREEN)
        countdown(work_sec)
        
###########################################################
###########################################################
####     MAIN FUNCTION

window = tk.Tk()
window.title("Pomodoro App")
# window.minsize(width=500, height=500)
window.configure(padx=100, pady=50, bg=YELLOW)


task_name = tk.Label(text="TIMER", font=("Arial", 24, "bold"), background=YELLOW, foreground=GREEN)
task_name.grid(column=1, row=0)


canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=photo_image)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# timer_label = tk.Label(text="25:00",font=("Arial", 24, "bold"),background=PINK, foreground=GREEN)
# timer_label.grid(column=1, row=2)

start_button = tk.Button(text="Start",highlightthickness=8, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset",highlightthickness=8, command=reset_timer)
reset_button.grid(column=3, row=2)

ticks = tk.Label(text="", fg=GREEN)
ticks.grid(column=1, row=3)

window.mainloop()