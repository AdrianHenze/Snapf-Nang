from tkinter import ttk

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


def default_button_style(root):
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Default.TButton",
                    background=color_space_gray,
                    foreground=color_button_text_gray,
                    borderwidth=-1,
                    relief="sunken",
                    focusthickness=0,
                    focuscolor=color_space_gray,
                    font=("Helvetica", 24),
                    padding=(0, 0))
    style.map("Default.TButton",
          foreground=[('active', color_white),
                      ('pressed', color_white)],
          background=[('active', color_button_gray),
                      ('pressed', color_black)])
    style.configure("Active.Default.TButton",
                    background=color_button_gray,
                    foreground=color_white,
                    borderwidth=0,
                    focusthickness=0,
                    focuscolor=color_space_gray,
                    font=("Helvetica", 24),
                    padding=(0, 0))
    return style


def nav_button_style(root):
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Custom.TButton",
                    background=color_space_gray,
                    foreground=color_button_text_gray,
                    borderwidth=0,
                    focusthickness=0,
                    focuscolor=color_space_gray,
                    font=("Helvetica", 36),
                    padding=(0, 30))
    style.map("Custom.TButton",
          foreground=[('active', color_white),
                      ('pressed', color_white)],
          background=[('active', color_button_gray),
                      ('pressed', color_black)])
    style.configure("Active.Custom.TButton",
                    background=color_button_gray,
                    foreground=color_gold,
                    borderwidth=0,
                    focusthickness=0,
                    focuscolor=color_space_gray,
                    font=("Helvetica", 36),
                    padding=(0, 50))
    return style

def logout_button_style(root):
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Logout.TButton",
                    background=color_space_gray,
                    foreground=color_dark_red,
                    borderwidth=0,
                    focusthickness=0,
                    focuscolor=color_space_gray,
                    font=("Helvetica", 24),
                    padding=(0, 20))
    style.map("Logout.TButton",
          foreground=[('active', color_red),
                      ('pressed', color_red)],
          background=[('active', color_black),
                      ('pressed', color_black)])
    style.configure("Active.Logout.TButton",
                    background=color_button_gray,
                    foreground=color_white,
                    borderwidth=0,
                    focusthickness=0,
                    focuscolor=color_space_gray,
                    font=("Helvetica", 24),
                    padding=(0, 50))
    return style
