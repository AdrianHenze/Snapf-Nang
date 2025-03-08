# Nangs Realm
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Colors #1
color_black = "#0D0D0D"
color_space_gray = "#171717"
color_gray = "#212121"
color_button_gray = "#2F2F2F"
color_textfield_gray = "#303030"
color_button_text_gray = "#B4B4B4"
color_text_gray = "#D6D6D6"
color_white = "#FFFFFF"

# Colors #2
color_red = "#EF4444"
color_dark_red = "#B91C1C"
color_gold = "#DB9F1E"
color_orange = "#E36E30"
color_lime = "#3DCB40"
color_green = "#10A37F"
color_turquoise = "#27C0A6"
color_cyan = "#16B7DB"
color_steel_blue = "#6490F0"
color_blue = "#0285FF"
color_dark_blue = "#1D53BF"
color_pink = "#E659C2"
color_purple = "#875BE1"

# Window
root = tk.Tk()
root.title("Snapf-Nang Bank")

# Window Size and Location
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.69)
window_height = int(screen_height * 0.69)
window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


def button_style():
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Custom.TButton",
                    background=color_space_gray,
                    foreground=color_button_text_gray,
                    borderwidth=0,
                    focusthickness=0,
                    focuscolor=color_space_gray,
                    font=("Helvetica", 36),
                    padding=(0, 50))
    # Hover and Press
    style.map("Custom.TButton",
          foreground=[('active', color_white),
                      ('pressed', color_white)],
          background=[('active', color_button_gray),
                      ('pressed', color_black)])
    return style


def build_frame1():
    frame1 = tk.Frame(root, bg=color_gray)
    frame1.pack(fill="both", expand=True)

    # Set Up
    r_page_width = 600
    l_page_width = window_width - r_page_width

    frame1.grid_rowconfigure(0, weight=1)
    frame1.grid_columnconfigure(0, weight=2)
    frame1.grid_columnconfigure(1, weight=2, minsize=r_page_width)

    # Right Side
    r_page = tk.Frame(frame1, bg=color_space_gray, width=r_page_width)
    r_page.grid(row=0, column=1, sticky="nsew")
    r_page.grid_propagate(False)

    # Frame to center Buttons on Right Side
    nav_frame = tk.Frame(r_page, bg=color_space_gray)
    nav_frame.pack(expand=True, fill="both")
    nav_frame.grid_rowconfigure(0, weight=1)
    nav_frame.grid_rowconfigure(4, weight=1)
    nav_frame.grid_columnconfigure(0, weight=1)

    # Buttons
    def button_test_function(text):
        print(text)
    def button(frame, row, col, text, command):
        b = ttk.Button(frame, text=text, style="Custom.TButton", command=lambda: command(text))
        b.grid(row=row, column=col, sticky="ew", pady=10, padx=10)
    style = button_style()
    button(nav_frame, 0, 0, "Deposit", button_test_function)
    button(nav_frame, 3, 0, "Withdrawal", button_test_function)
    button(nav_frame, 4, 0, "Balance", button_test_function)

    # Left Side
    l_page = tk.Frame(frame1, bg=color_gray, width=l_page_width)
    l_page.grid(row=0, column=0, sticky="nsew")
    l_page.grid_propagate(False)
    # Image
    img_size = int(0.7*l_page_width)
    img_data_raw = Image.open("data/img/BG.png")
    img_data = img_data_raw.resize((img_size, img_size))
    img_file = ImageTk.PhotoImage(img_data)
    img = tk.Label(l_page, image=img_file, bg=color_gray)
    img.image = img_file
    img.place(relx=0.5, rely=0.5, anchor="center")


def start_snapf_nang():
    build_frame1()
    tk.mainloop()
