# Nangs Realm
import tkinter as tk
from PIL import Image, ImageTk
from code.widgets import *

root = None
window_width = None
main_frame = None
r_page = None
l_page = None
r_page_width = None
l_page_width = None

nav_buttons = {}

def build_window():
    global root, window_width, r_page_width, l_page_width
    root = tk.Tk()
    root.title("Snapf-Nang Bank")
    # Size and Location
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = int(screen_width * 0.69)
    window_height = int(screen_height * 0.69)
    window_x = (screen_width - window_width) // 2
    window_y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
    # Sections
    r_page_width = 600
    l_page_width = window_width - r_page_width
    return root


def build_main_frame():
    global main_frame
    # Set Up
    main_frame = tk.Frame(root, bg=color_gray)
    main_frame.pack(fill="both", expand=True)
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(0, weight=2)
    main_frame.grid_columnconfigure(1, weight=2, minsize=r_page_width)
    
    build_right_login()
    open_login_page()


def insert_title_image(page):
    img_size = int(0.7*l_page_width)
    img_data_raw = Image.open("data/img/BG.png")
    img_data = img_data_raw.resize((img_size, img_size))
    img_file = ImageTk.PhotoImage(img_data)
    img = tk.Label(page, image=img_file, bg=color_gray)
    img.image = img_file
    img.place(relx=0.5, rely=0.5, anchor="center")


def highlight_active_button(active_button):
    # Reset all Button Styles
    for b in nav_buttons.values():
        b.configure(style="Custom.TButton")
    # Highlight Active Button
    nav_buttons[active_button].configure(style="Active.Custom.TButton")


def build_right_login():
    global r_page
    if r_page:
        r_page.destroy()  # Remove current Right Page
    r_page = tk.Frame(main_frame, bg=color_space_gray, width=r_page_width)
    r_page.grid(row=0, column=1, sticky="nsew")
    r_page.grid_propagate(False)
    # Extra Frame to center Buttons
    nav_frame = tk.Frame(r_page, bg=color_space_gray)
    nav_frame.pack(expand=True, fill="both")
    nav_frame.grid_rowconfigure(0, weight=1)
    nav_frame.grid_rowconfigure(4, weight=1)
    nav_frame.grid_columnconfigure(0, weight=1)
    # Buttons
    def button(frame, row, col, text, command):
        b = ttk.Button(frame, text=text, style="Custom.TButton", command=command)
        b.grid(row=row, column=col, sticky="ew", pady=10, padx=10)
        nav_buttons[text] = b
    style = button_style(root)
    button(nav_frame, 2, 0, "Login", open_login_page)
    button(nav_frame, 3, 0, "Register", open_register_page)


def build_right_navigation():
    global r_page
    if r_page:
        r_page.destroy()  # Remove current Right Page
    r_page = tk.Frame(main_frame, bg=color_space_gray, width=r_page_width)
    r_page.grid(row=0, column=1, sticky="nsew")
    r_page.grid_propagate(False)
    # Extra Frame to center Buttons
    nav_frame = tk.Frame(r_page, bg=color_space_gray)
    nav_frame.pack(expand=True, fill="both")
    nav_frame.grid_rowconfigure(0, weight=1)
    nav_frame.grid_rowconfigure(4, weight=1)
    nav_frame.grid_columnconfigure(0, weight=1)
    # Buttons
    def button(frame, row, col, text, command):
        b = ttk.Button(frame, text=text, style="Custom.TButton", command=command)
        b.grid(row=row, column=col, sticky="ew", pady=10, padx=10)
    style = button_style(root)
    button(nav_frame, 0, 0, "Balance", open_balance_page)
    button(nav_frame, 2, 0, "Deposit", open_deposit_page)
    button(nav_frame, 3, 0, "Withdrawal", open_withdrawal_page)
    button(nav_frame, 4, 0, "Transfer", open_transfer_page)


def open_login_page():
    global l_page
    if l_page:
        l_page.destroy()  # Remove current Left Page
    
    highlight_active_button("Login")

    login_page = tk.Frame(main_frame, bg=color_gray, width=l_page_width)
    login_page.grid(row=0, column=0, sticky="nsew")
    login_page.grid_propagate(False)

    insert_title_image(login_page)

    label = tk.Label(login_page, text="Login Page", bg=color_gray, fg=color_white)
    label.place(relx=0.5, rely=0.5, anchor="center")
    
    l_page = login_page  # Update global Reference


def open_register_page():
    global l_page
    if l_page:
        l_page.destroy()  # Remove current Left Page
    
    highlight_active_button("Register")

    register_page = tk.Frame(main_frame, bg=color_gray, width=l_page_width)
    register_page.grid(row=0, column=0, sticky="nsew")
    register_page.grid_propagate(False)

    insert_title_image(register_page)

    label = tk.Label(register_page, text="Register Page", bg=color_gray, fg=color_white)
    label.place(relx=0.5, rely=0.5, anchor="center")
    
    l_page = register_page  # Update global Reference


def open_balance_page():
    global l_page
    l_page.destroy()  # Remove current Left Page

    highlight_active_button("Balance")

    balance_page = tk.Frame(main_frame, bg=color_gray, width=l_page_width)
    balance_page.grid(row=0, column=0, sticky="nsew")
    balance_page.grid_propagate(False)

    insert_title_image(balance_page)

    label = tk.Label(balance_page, text="Balance Page", bg=color_gray, fg=color_white)
    label.place(relx=0.5, rely=0.5, anchor="center")
    
    l_page = balance_page  # Update global Reference


def open_deposit_page():
    global l_page
    l_page.destroy()  # Remove current Left Page

    highlight_active_button("Deposit")

    deposit_page = tk.Frame(main_frame, bg=color_gray, width=l_page_width)
    deposit_page.grid(row=0, column=0, sticky="nsew")
    deposit_page.grid_propagate(False)

    insert_title_image(deposit_page)

    label = tk.Label(deposit_page, text="Deposit Page", bg=color_gray, fg=color_white)
    label.place(relx=0.5, rely=0.5, anchor="center")
    
    l_page = deposit_page  # Update global Reference


def open_withdrawal_page():
    global l_page
    l_page.destroy()  # Remove current Left Page

    highlight_active_button("Withdrawal")

    withdrawal_page = tk.Frame(main_frame, bg=color_gray, width=l_page_width)
    withdrawal_page.grid(row=0, column=0, sticky="nsew")
    withdrawal_page.grid_propagate(False)

    insert_title_image(withdrawal_page)

    label = tk.Label(withdrawal_page, text="Withdrawal Page", bg=color_gray, fg=color_white)
    label.place(relx=0.5, rely=0.5, anchor="center")
    
    l_page = withdrawal_page  # Update global Reference


def open_transfer_page():
    global l_page
    l_page.destroy()  # Remove current Left Page

    highlight_active_button("Transfer")
    
    transfer_page = tk.Frame(main_frame, bg=color_gray, width=l_page_width)
    transfer_page.grid(row=0, column=0, sticky="nsew")
    transfer_page.grid_propagate(False)

    insert_title_image(transfer_page)
    
    label = tk.Label(transfer_page, text="Transfer Page", bg=color_gray, fg=color_white)
    label.place(relx=0.5, rely=0.5, anchor="center")
    
    l_page = transfer_page  # Update global Reference


def start_snapf_nang():
    build_window()
    build_main_frame()
    tk.mainloop()
