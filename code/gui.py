# Nangs Realm
import tkinter as tk
from PIL import Image, ImageTk
from code.widgets import *
from code.button_event import *

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
    
    build_right_login_registration()
    open_login_page()


def insert_title_image(page):
    img_size = int(0.75*l_page_width)
    img_data_raw = Image.open("data/img/BG.png")
    img_data = img_data_raw.resize((img_size, img_size))
    img_file = ImageTk.PhotoImage(img_data)
    img = tk.Label(page, image=img_file, bg=color_gray)
    img.image = img_file
    img.place(relx=0.5, rely=0.5, anchor="center")


def highlight_active_button(active_button):
    # Reset all Button Styles
    for _, b in nav_buttons.items():
        b.configure(style="Custom.TButton")
    # Highlight Active Button
    if active_button in nav_buttons:
        nav_buttons[active_button].configure(style="Active.Custom.TButton")
    else:
        pass


def default_button(frame, row, col, text, command):
    b = ttk.Button(frame, text=text, style="Default.TButton", command=command)
    if text == "Show Transaction History" or text == "Show Balance":
        b.grid(row=row, column=col, sticky="ew", pady=(10,10), padx=(10,10), ipady=10)
    else:
        b.grid(row=row, column=col, sticky="ew", pady=(30,30), padx=(10,50), ipady=10)


def nav_button(frame, row, col, text, command):
    if text == "Logout":
        style = "Logout.TButton"
    else:
        style = "Custom.TButton"
    b = ttk.Button(frame, text=text, style=style, command=command)
    b.grid(row=row, column=col, sticky="ew", pady=10, padx=10)
    if text != "Logout":
        nav_buttons[text] = b


def build_right_login_registration():
    global r_page
    nav_buttons.clear()
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
    style = nav_button_style(root)
    nav_button(nav_frame, 2, 0, "Login", open_login_page)
    nav_button(nav_frame, 3, 0, "Register", open_register_page)


def build_right_navigation():
    global r_page
    nav_buttons.clear()
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
    def logout():
        logout_if()
        build_right_login_registration()
        open_login_page()
    style = nav_button_style(root)
    nav_button(nav_frame, 0, 0, "Balance", open_balance_page)
    nav_button(nav_frame, 2, 0, "Deposit", open_deposit_page)
    nav_button(nav_frame, 3, 0, "Withdrawal", open_withdrawal_page)
    nav_button(nav_frame, 4, 0, "Transfer", open_transfer_page)
    style = logout_button_style(root)
    nav_button(nav_frame, 5, 0, "Logout", logout)


def open_login_page():
    global l_page
    if l_page:
        l_page.destroy()  # Remove current Left Page
    
    highlight_active_button("Login")

    login_page = tk.Frame(main_frame, bg=color_gray, width=l_page_width)
    login_page.grid(row=0, column=0, sticky="nsew")
    login_page.grid_propagate(False)

    insert_title_image(login_page)

    input_frame = tk.Frame(login_page, bg=color_space_gray, relief="ridge", borderwidth=10)
    input_frame.place(relx=0.5, rely=0.5, anchor="center")
    input_frame.pack_propagate(False)
    # Username
    name_label = tk.Label(input_frame, text="Username:", bg=color_space_gray, fg=color_text_gray, font=("Helvetica", 24))
    name_label.grid(row=0, column=0, sticky="e", pady=(50,10), padx=(50,10))
    name_entry = tk.Entry(input_frame, bg=color_textfield_gray, fg=color_white, font=("Helvetica", 24))
    name_entry.grid(row=0, column=1, sticky="w", pady=(50,10), padx=(10,50))
    # Password
    pw_label = tk.Label(input_frame, text="Passwort:", bg=color_space_gray, fg=color_text_gray, font=("Helvetica", 24))
    pw_label.grid(row=1, column=0, sticky="e", pady=(10,10), padx=(50,10))
    pw_entry = tk.Entry(input_frame, show="*", bg=color_textfield_gray, fg=color_white, font=("Helvetica", 24))
    pw_entry.grid(row=1, column=1, sticky="w", pady=(10,10), padx=(10,50))
    # Login
    def login():
        rc = is_valid_login(name_entry.get(), pw_entry.get())
        if rc == -1:
            print("ERROR: Not an account.")
        elif rc == -2:
            print("ERROR: Wrong password.")
        elif rc == -3:
            print("ERROR: Missing information.")
        else:
            build_right_navigation()
            open_balance_page()
    # Login Button
    style = default_button_style(root)
    default_button(input_frame, 2, 1, "Login", login)

    l_page = login_page  # Update global Reference


def open_register_page():
    global l_page
    l_page.destroy()  # Remove current Left Page
    
    highlight_active_button("Register")

    register_page = tk.Frame(main_frame, bg=color_gray, width=l_page_width)
    register_page.grid(row=0, column=0, sticky="nsew")
    register_page.grid_propagate(False)

    insert_title_image(register_page)

    input_frame = tk.Frame(register_page, bg=color_space_gray, relief="ridge", borderwidth=10)
    input_frame.place(relx=0.5, rely=0.5, anchor="center")
    input_frame.pack_propagate(False)
    # Username
    name_label = tk.Label(input_frame, text="Username:", bg=color_space_gray, fg=color_text_gray, font=("Helvetica", 24))
    name_label.grid(row=0, column=0, sticky="e", pady=(50,10), padx=(50,10))
    name_entry = tk.Entry(input_frame, bg=color_textfield_gray, fg=color_white, font=("Helvetica", 24))
    name_entry.grid(row=0, column=1, sticky="w", pady=(50,10), padx=(10,50))
    # Password
    pw_label = tk.Label(input_frame, text="Passwort:", bg=color_space_gray, fg=color_text_gray, font=("Helvetica", 24))
    pw_label.grid(row=1, column=0, sticky="e", pady=(10,10), padx=(50,10))
    pw_entry = tk.Entry(input_frame, show="*", bg=color_textfield_gray, fg=color_white, font=("Helvetica", 24))
    pw_entry.grid(row=1, column=1, sticky="w", pady=(10,10), padx=(10,50))
    # Year of Birth
    year_label = tk.Label(input_frame, text="Year of Birth:", bg=color_space_gray, fg=color_text_gray, font=("Helvetica", 24))
    year_label.grid(row=2, column=0, sticky="e", pady=(10,10), padx=(50,10))
    year_entry = tk.Entry(input_frame, bg=color_textfield_gray, fg=color_white, font=("Helvetica", 24))
    year_entry.grid(row=2, column=1, sticky="w", pady=(10,10), padx=(10,50))
    # Register
    def register():
        if is_valid_registration(name_entry.get(),pw_entry.get(),year_entry.get()):
            build_right_navigation()
            open_balance_page()
    # Register Button
    style = default_button_style(root)
    default_button(input_frame, 3, 1, "Register", register)
    
    l_page = register_page  # Update global Reference


def open_balance_page():
    global l_page
    l_page.destroy()  # Remove current Left Page

    highlight_active_button("Balance")

    balance_page = tk.Frame(main_frame, bg=color_gray, width=l_page_width)
    balance_page.grid(row=0, column=0, sticky="nsew")
    balance_page.grid_propagate(False)

    insert_title_image(balance_page)

    input_frame = tk.Frame(balance_page, bg=color_space_gray, relief="ridge", borderwidth=10)
    input_frame.place(relx=0.5, rely=0.5, anchor="center")
    input_frame.pack_propagate(False)
    # Amount
    balance_str = get_balance_if() + " €"
    amount_label = tk.Label(input_frame, text=balance_str, bg=color_space_gray, fg=color_text_gray, font=("Helvetica", 40))
    amount_label.grid(row=0, column=0, sticky="n", pady=(50,50), padx=(50,50))
    # Button
    def show_transactions():
        open_transactions_page()
    style = default_button_style(root)
    default_button(input_frame, 1, 0, "Show Transaction History", show_transactions)

    l_page = balance_page  # Update global Reference


def open_transactions_page():
    global l_page
    l_page.destroy()  # Remove current Left Page

    transactions_page = tk.Frame(main_frame, bg=color_gray, width=l_page_width)
    transactions_page.grid(row=0, column=0, sticky="nsew")
    transactions_page.grid_propagate(False)
    
    insert_title_image(transactions_page)

    transactions_page.grid_rowconfigure(0, weight=1)
    transactions_page.grid_rowconfigure(1, weight=0)
    transactions_page.grid_columnconfigure(0, weight=1)

    # Transaction List
    canvas = tk.Canvas(transactions_page, bg=color_space_gray, highlightthickness=0)
    canvas.grid(row=0, column=0, sticky="nsew")
    v_scroll = tk.Scrollbar(transactions_page, orient="vertical", command=canvas.yview)
    v_scroll.grid(row=0, column=1, sticky="ns")
    canvas.configure(yscrollcommand=v_scroll.set)
    input_frame = tk.Frame(canvas, bg=color_space_gray, relief="ridge", borderwidth=10)
    window_id = canvas.create_window((0,0), window=input_frame, anchor="center")
    def on_canvas_configure(event):
        canvas.coords(window_id, event.width/2, event.height/2)
        canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.bind("<Configure>", on_canvas_configure)
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    input_frame.bind("<Configure>", on_frame_configure)
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
    canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))
    balance_str = get_transactions_if()
    amount_label = tk.Label(input_frame, text=balance_str, bg=color_space_gray, fg=color_text_gray, font=("Helvetica", 24))
    amount_label.grid(row=0, column=0, sticky="e", pady=(50,50), padx=(50,50))
    
    # Button
    button_area = tk.Frame(transactions_page, bg=color_space_gray, height=100)
    button_area.grid(row=1, column=0, columnspan=2, sticky="ew")
    button_area.grid_propagate(False)
    button_area.grid_columnconfigure(0, weight=1)
    def show_balance():
        open_balance_page()
    style = default_button_style(root)
    default_button(button_area, 1, 0, "Show Balance", show_balance)

    l_page = transactions_page  # Update global Reference


def open_deposit_page():
    global l_page
    l_page.destroy()  # Remove current Left Page

    highlight_active_button("Deposit")

    deposit_page = tk.Frame(main_frame, bg=color_gray, width=l_page_width)
    deposit_page.grid(row=0, column=0, sticky="nsew")
    deposit_page.grid_propagate(False)

    insert_title_image(deposit_page)

    input_frame = tk.Frame(deposit_page, bg=color_space_gray, relief="ridge", borderwidth=10)
    input_frame.place(relx=0.5, rely=0.5, anchor="center")
    input_frame.pack_propagate(False)
    # Amount
    amount_label = tk.Label(input_frame, text="Money amount:", bg=color_space_gray, fg=color_text_gray, font=("Helvetica", 24))
    amount_label.grid(row=0, column=0, sticky="e", pady=(50,10), padx=(50,10))
    amount_entry = tk.Entry(input_frame, bg=color_textfield_gray, fg=color_white, font=("Helvetica", 24))
    amount_entry.grid(row=0, column=1, sticky="w", pady=(50,10), padx=(10,50))
    # Button
    def deposit():
        deposit_if(amount_entry.get())
        amount_entry.delete(0, tk.END)
    style = default_button_style(root)
    default_button(input_frame, 1, 1, "Deposit", deposit)

    l_page = deposit_page  # Update global Reference


def open_withdrawal_page():
    global l_page
    l_page.destroy()  # Remove current Left Page

    highlight_active_button("Withdrawal")

    withdrawal_page = tk.Frame(main_frame, bg=color_gray, width=l_page_width)
    withdrawal_page.grid(row=0, column=0, sticky="nsew")
    withdrawal_page.grid_propagate(False)

    insert_title_image(withdrawal_page)

    input_frame = tk.Frame(withdrawal_page, bg=color_space_gray, relief="ridge", borderwidth=10)
    input_frame.place(relx=0.5, rely=0.5, anchor="center")
    input_frame.pack_propagate(False)
    # Amount
    amount_label = tk.Label(input_frame, text="Money amount:", bg=color_space_gray, fg=color_text_gray, font=("Helvetica", 24))
    amount_label.grid(row=0, column=0, sticky="e", pady=(50,10), padx=(50,10))
    amount_entry = tk.Entry(input_frame, bg=color_textfield_gray, fg=color_white, font=("Helvetica", 24))
    amount_entry.grid(row=0, column=1, sticky="w", pady=(50,10), padx=(10,50))
    # Button
    def withdrawal():
        withdrawal_if(amount_entry.get())
        amount_entry.delete(0, tk.END)
    style = default_button_style(root)
    default_button(input_frame, 1, 1, "Withdraw", withdrawal)

    l_page = withdrawal_page  # Update global Reference


def open_transfer_page():
    global l_page
    l_page.destroy()  # Remove current Left Page

    highlight_active_button("Transfer")
    
    transfer_page = tk.Frame(main_frame, bg=color_gray, width=l_page_width)
    transfer_page.grid(row=0, column=0, sticky="nsew")
    transfer_page.grid_propagate(False)

    insert_title_image(transfer_page)

    input_frame = tk.Frame(transfer_page, bg=color_space_gray, relief="ridge", borderwidth=10)
    input_frame.place(relx=0.5, rely=0.5, anchor="center")
    input_frame.pack_propagate(False)
    # Recipient
    rec_label = tk.Label(input_frame, text="Recipient name:", bg=color_space_gray, fg=color_text_gray, font=("Helvetica", 24))
    rec_label.grid(row=0, column=0, sticky="e", pady=(50,10), padx=(50,10))
    rec_entry = tk.Entry(input_frame, bg=color_textfield_gray, fg=color_white, font=("Helvetica", 24))
    rec_entry.grid(row=0, column=1, sticky="w", pady=(50,10), padx=(10,50))
    # Betrag
    amount_label = tk.Label(input_frame, text="Money amount:", bg=color_space_gray, fg=color_text_gray, font=("Helvetica", 24))
    amount_label.grid(row=1, column=0, sticky="e", pady=(10,10), padx=(50,10))
    amount_entry = tk.Entry(input_frame, bg=color_textfield_gray, fg=color_white, font=("Helvetica", 24))
    amount_entry.grid(row=1, column=1, sticky="w", pady=(10,10), padx=(10,50))
    # Payment Reference
    ref_label = tk.Label(input_frame, text="Ref. (optional):", bg=color_space_gray, fg=color_text_gray, font=("Helvetica", 24))
    ref_label.grid(row=2, column=0, sticky="e", pady=(10,10), padx=(50,10))
    ref_entry = tk.Entry(input_frame, bg=color_textfield_gray, fg=color_white, font=("Helvetica", 24))
    ref_entry.grid(row=2, column=1, sticky="w", pady=(10,10), padx=(10,50))
    # Button
    def transfer():
        transfer_if(rec_entry.get(), amount_entry.get(), ref_entry.get())
        rec_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        ref_entry.delete(0, tk.END)
    style = default_button_style(root)
    default_button(input_frame, 3, 1, "Transfer", transfer)
    
    l_page = transfer_page  # Update global Reference


def start_snapf_nang():
    build_window()
    build_main_frame()
    tk.mainloop()
