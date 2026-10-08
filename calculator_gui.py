import tkinter as tk
import math


# ---------------- WINDOW ----------------

root = tk.Tk()
root.title("Calculator Pro")
root.geometry("520x650")
root.resizable(False, False)

dark_mode = True


# ---------------- FUNCTIONS ----------------

def add_value(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def backspace():
    value = display.get()
    display.delete(0, tk.END)
    display.insert(0, value[:-1])


def calculate():
    try:
        expression = display.get()

        # Allow only calculator characters
        allowed = "0123456789+-*/().% "

        if not all(char in allowed for char in expression):
            raise ValueError

        # Percentage
        expression = expression.replace("%", "/100")

        result = eval(expression, {"__builtins__": {}}, {})

        display.delete(0, tk.END)
        display.insert(0, str(result))

        history.insert(
            tk.END,
            f"{expression} = {result}"
        )

    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Cannot divide by zero")

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def square():
    try:
        value = float(display.get())
        result = value ** 2

        display.delete(0, tk.END)
        display.insert(0, str(result))

        history.insert(
            tk.END,
            f"{value}² = {result}"
        )

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def square_root():
    try:
        value = float(display.get())

        if value < 0:
            raise ValueError

        result = math.sqrt(value)

        display.delete(0, tk.END)
        display.insert(0, str(result))

        history.insert(
            tk.END,
            f"√{value} = {result}"
        )

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def plus_minus():
    try:
        value = float(display.get())
        result = -value

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def clear_history():
    history.delete(0, tk.END)


def keyboard_input(event):
    key = event.keysym

    if event.char in "0123456789+-*/().%":
        add_value(event.char)

    elif key == "Return":
        calculate()

    elif key == "BackSpace":
        backspace()

    elif key == "Escape":
        clear()


def change_theme():
    global dark_mode

    dark_mode = not dark_mode

    if dark_mode:
        bg = "#202124"
        fg = "white"
        button_bg = "#303134"
        display_bg = "#303134"

    else:
        bg = "#f2f2f2"
        fg = "black"
        button_bg = "#ffffff"
        display_bg = "#ffffff"

    root.configure(bg=bg)
    display.configure(
        bg=display_bg,
        fg=fg,
        insertbackground=fg
    )

    for button in all_buttons:
        button.configure(
            bg=button_bg,
            fg=fg,
            activebackground=bg,
            activeforeground=fg
        )


# ---------------- DISPLAY ----------------

display = tk.Entry(
    root,
    font=("Arial", 28),
    justify="right",
    bd=10,
    relief=tk.RIDGE
)

display.pack(
    padx=15,
    pady=15,
    fill="x"
)


# ---------------- BUTTON FRAME ----------------

button_frame = tk.Frame(root)
button_frame.pack()


all_buttons = []


def create_button(text, row, column, command):
    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 16),
        width=5,
        height=2,
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=4,
        pady=4
    )

    all_buttons.append(button)


# ---------------- BUTTONS ----------------

create_button("AC", 0, 0, clear)
create_button("⌫", 0, 1, backspace)
create_button("%", 0, 2, lambda: add_value("%"))
create_button("/", 0, 3, lambda: add_value("/"))

create_button("√", 1, 0, square_root)
create_button("x²", 1, 1, square)
create_button("±", 1, 2, plus_minus)
create_button("*", 1, 3, lambda: add_value("*"))

create_button("7", 2, 0, lambda: add_value("7"))
create_button("8", 2, 1, lambda: add_value("8"))
create_button("9", 2, 2, lambda: add_value("9"))
create_button("-", 2, 3, lambda: add_value("-"))

create_button("4", 3, 0, lambda: add_value("4"))
create_button("5", 3, 1, lambda: add_value("5"))
create_button("6", 3, 2, lambda: add_value("6"))
create_button("+", 3, 3, lambda: add_value("+"))

create_button("1", 4, 0, lambda: add_value("1"))
create_button("2", 4, 1, lambda: add_value("2"))
create_button("3", 4, 2, lambda: add_value("3"))
create_button("=", 4, 3, calculate)

create_button("0", 5, 0, lambda: add_value("0"))
create_button(".", 5, 1, lambda: add_value("."))
create_button("(", 5, 2, lambda: add_value("("))
create_button(")", 5, 3, lambda: add_value(")"))


# ---------------- HISTORY ----------------

history_label = tk.Label(
    root,
    text="Calculation History",
    font=("Arial", 14)
)

history_label.pack(pady=(15, 5))

history = tk.Listbox(
    root,
    height=5,
    font=("Arial", 12)
)

history.pack(
    padx=15,
    fill="x"
)


# ---------------- EXTRA BUTTONS ----------------

extra_frame = tk.Frame(root)
extra_frame.pack(pady=10)

theme_button = tk.Button(
    extra_frame,
    text="Dark / Light Mode",
    font=("Arial", 12),
    command=change_theme
)

theme_button.grid(row=0, column=0, padx=5)

clear_history_button = tk.Button(
    extra_frame,
    text="Clear History",
    font=("Arial", 12),
    command=clear_history
)

clear_history_button.grid(row=0, column=1, padx=5)


# ---------------- KEYBOARD ----------------

root.bind("<Key>", keyboard_input)


# ---------------- START ----------------

change_theme()

root.mainloop()