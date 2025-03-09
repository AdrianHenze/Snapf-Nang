# Nangs Realm
import tkinter as tk
from PIL import Image, ImageTk
from code.widgets import *

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


def build_frame1():
    # Set Up
    frame1 = tk.Frame(root, bg=color_gray)
    frame1.pack(fill="both", expand=True)
    r_page_width = 600
    l_page_width = window_width - r_page_width
    frame1.grid_rowconfigure(0, weight=1)
    frame1.grid_columnconfigure(0, weight=2)
    frame1.grid_columnconfigure(1, weight=2, minsize=r_page_width)

    def build_right_page():
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
        style = button_style(root)
        button(nav_frame, 0, 0, "Deposit", button_test_function)
        button(nav_frame, 3, 0, "Withdrawal", button_test_function)
        button(nav_frame, 4, 0, "Balance", button_test_function)

    def build_left_page():
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
    
    build_right_page()
    build_left_page()


def start_snapf_nang():
    build_frame1()
    tk.mainloop()
