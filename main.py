from tkinter import *
import math
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


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_reset)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Long Break", font=(FONT_NAME, 20, 'bold'), foreground=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Short Break", font=(FONT_NAME, 20, 'bold'), foreground=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", font=(FONT_NAME, 20, 'bold'), foreground=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_reset
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Panoromo")
window.config(padx=100, pady=50, background=YELLOW)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(row=1, column=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


timer = Label(text="Timer", font=(FONT_NAME, 20, 'bold'), foreground=GREEN)
timer.grid(row=0, column=1)

start = Button(text="Start", font=(FONT_NAME, 20, 'bold'), foreground=PINK, highlightthickness=0, command=start_timer)
start.grid(row=3, column=0)

reset = Button(text="Reset", font=(FONT_NAME, 20, 'bold'), foreground=RED, highlightthickness=0, command=reset_timer)
reset.grid(row=3, column=2)

check_mark = Label(text="", font=(FONT_NAME, 20, 'bold'), foreground=GREEN)
check_mark.grid(row=4, column=1)

window.mainloop()
