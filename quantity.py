from tkinter import *

quantity = None

window = Tk()
window.title("Reading Tracker")
window.geometry("500x370")
window.config(bg="#2C2F33")
window.resizable(False, False)

# ---------------- DISPLAY ---------------- #

canvas = Canvas(
    window,
    width=400,
    height=120,
    bg="#2C2F33",
    highlightthickness=0
)
canvas.pack(pady=20)

canvas.create_rectangle(
    50, 25, 350, 95,
    fill="#23272A",
    outline="#7289DA",
    width=3
)

current_quantity = 0

text_id = canvas.create_text(
    200,
    60,
    text="0",
    font=("Segoe UI", 32, "bold"),
    fill="white"
)

# ---------------- FUNCTIONS ---------------- #

def increase():
    global current_quantity
    current_quantity += 1
    canvas.itemconfig(text_id, text=int(current_quantity))

def decrease():
    global current_quantity
    if current_quantity > 0:
        current_quantity -= 1
        canvas.itemconfig(text_id, text=int(current_quantity))

def done():
    global quantity
    quantity = current_quantity

    print("Selected Quantity:", quantity)

    window.quit()
    window.destroy()

# ---------------- TITLE ---------------- #

Label(
    window,
    text="Pages Read Today",
    font=("Segoe UI", 16, "bold"),
    bg="#2C2F33",
    fg="white"
).pack()

# ---------------- BUTTONS ---------------- #

button_frame = Frame(window, bg="#2C2F33")
button_frame.pack(pady=20)

minus_btn = Button(
    button_frame,
    text="-",
    font=("Segoe UI", 18, "bold"),
    width=6,
    height=2,
    bg="#E74C3C",
    fg="white",
    relief="flat",
    command=decrease
)
minus_btn.grid(row=0, column=0, padx=15)

plus_btn = Button(
    button_frame,
    text="+",
    font=("Segoe UI", 18, "bold"),
    width=6,
    height=2,
    bg="#2ECC71",
    fg="white",
    relief="flat",
    command=increase
)
plus_btn.grid(row=0, column=1, padx=15)

# ---------------- DONE BUTTON ---------------- #

done_btn = Button(
    window,
    text="DONE",
    font=("Segoe UI", 14, "bold"),
    width=18,
    height=2,
    bg="#7289DA",
    fg="white",
    relief="flat",
    command=done
)
done_btn.pack(pady=10)

window.mainloop()

