#!/usr/bin/env python3

# Aleksandr Verevkin
# Pomodoro Timer for productivity Project using tkinter
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
single_marks = ""
total_marks = ""
timer = "after#0"  # None, string to avoid highlighting


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():  # Reset timer button
    global reps
    global single_marks
    global total_marks
    global timer
    reps = 0
    single_marks = ""
    total_marks = ""
    if timer:
        window.after_cancel(timer)
    l_checkmarks.config(text=single_marks)
    l_total_checkmarks.config(text=total_marks)
    l_timer.config(text="Timer")
    canvas.itemconfig(canvas_text, text="25:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():  # Start timer button
    global reps
    reps += 1
    if reps % 8 == 0:
        count = LONG_BREAK_MIN
        l_timer.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count = SHORT_BREAK_MIN
        l_timer.config(text="Short Break", fg=PINK)
    else:
        count = WORK_MIN
        l_timer.config(text="Work", fg=GREEN)
    countdown(count * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):  # Countdown activity function
    canvas.itemconfig(canvas_text, text=f"{count // 60}:{count % 60:02}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        global single_marks
        global total_marks
        if reps % 2:
            single_marks += "✓"
        elif not reps % 8:
            single_marks = ""
            total_marks += "✓"
            l_total_checkmarks.config(text=total_marks)
        l_checkmarks.config(text=single_marks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
# Main window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# Tomato picture
tomato_pic = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_pic)
canvas_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# Timer label
l_timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, highlightthickness=0, bg=YELLOW, width=12)
l_timer.grid(column=1, row=0)
# Check marks label
l_checkmarks = Label(fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 35, "bold"))
l_checkmarks.grid(column=1, row=3)
# 2 hours checkmarks label
l_total_checkmarks = Label(fg=RED, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 35, "bold"))
l_total_checkmarks.grid(column=1, row=4)
# Start button label
b_start = Button(text="Start", command=start_timer)
b_start.grid(column=0, row=2)
# Reset button label
b_reset = Button(text="Reset", command=reset_timer)
b_reset.grid(column=2, row=2)

window.mainloop()
