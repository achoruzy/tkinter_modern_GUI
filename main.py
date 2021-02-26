import tkinter as tk
from PIL import Image, ImageTk

# tkinter apps needs to have a root window class
# for root wm (window manager) methods may be used to setup app window appearance

colors = {
    'bg': '#22313F',
    'working_bg': '#34495E',
    'menu_bg': '#2C3E50',
    'button_hoover': '#67809F',
    'button_activebg': '#34495E',
    'button_activefg': '#67809F',
    'button_fg': '#19B5FE'
}

fonts = {
    'menu_normal': ('roboto.ttf', 10),
    'menu_large': ('roboto.ttf', 14),
    'infobox_normal': ('roboto.ttf', 8)
}

# App window setup
root = tk.Tk()
root.wm_minsize(width=400, height=300)
root.configure(bg=colors['bg'])
root.geometry('800x600')
root.title('inDust modulo')
# root.wm_resizable(False, False)
root.iconbitmap('assets/favicon.ico')


class Hoover:
    @staticmethod
    def bg_on_mouse_enter(widget, hoover_color):
        """Cast the function using:
        widget.bind("<Enter>", lambda x: bg_on_mouse_enter(widget, bg_color))"""
        widget.config(bg=hoover_color)

    @staticmethod
    def bg_on_mouse_leave(widget, bg_color):
        """Cast the function using:
        widget.bind("<Leave>", lambda x: bg_on_mouse_leave(widget, bg_color))"""
        widget.config(bg=bg_color)

    @staticmethod
    def image_on_mouse_enter(widget, hoover_image):
        """Cast the function using:
        widget.bind("<Enter>", lambda x: image_on_mouse_enter(widget, image_color))"""
        widget.config(image=hoover_image)

    @staticmethod
    def image_on_mouse_leave(widget, image):
        """Cast the function using:
        widget.bind("<Leave>", lambda x: image_on_mouse_leave(widget, image_color))"""
        widget.config(image=image)


# Application setup - inside app window
class MainWindow:
    def __init__(self, root):
        # Main Frame
        self.main_window = tk.Frame(root)
        self.main_window.config(bg=colors['bg'])
        self.main_window.pack(side='top', fill='both', expand=True)

        # Bottom Infobox Frame
        self.infobox = tk.Frame(self.main_window)
        self.infobox.config(bg=colors['bg'],
                            height=16)
        self.infobox.pack(side='bottom', fill='x', expand=False)

        # Left Menu Frame
        self.left_menu = tk.Frame(self.main_window)
        self.left_menu.config(bg=colors['menu_bg'],
                              width=38)
        self.left_menu.pack(side='left', fill='y', expand=False)

        # Top Menu Frame
        self.top_menu = tk.Frame(self.main_window)
        self.top_menu.config(bg=colors['menu_bg'],
                             width=38)
        self.top_menu.pack(side='top', fill='x', expand=False)

        # Working Frame
        self.working = tk.Frame(self.main_window)
        self.working.config(bg=colors['working_bg'])
        self.working.pack(side='top', fill='both', expand=True)

        # Widgets
        self.main_frame_widgets()
        self.infobox_widgets()
        self.left_menu_widgets()
        self.top_menu_widgets()

    # Class methods

    def main_frame_widgets(self):
        pass

    def infobox_widgets(self):
        label_version = tk.Label(self.infobox, text='Infobox v.0.001',
                                 fg='#19B5FE', bg=colors['bg'],
                                 font=fonts['infobox_normal'])
        label_version.pack(side='left')

    def left_menu_widgets(self):
        # Button Search
        button_1 = tk.Button(self.left_menu)

        button_1_load = Image.open('assets/search.png')
        root.button_1_img = ImageTk.PhotoImage(button_1_load)

        button_1_hoov_load = Image.open('assets/search_hoover.png')
        root.button_1_hoov_img = ImageTk.PhotoImage(button_1_hoov_load)

        button_1.config(bd=1,
                        bg=colors['menu_bg'],
                        activebackground=colors['button_activebg'],
                        image=root.button_1_img,
                        relief='flat',
                        command=check_button)

        button_1.bind("<Enter>", lambda x: Hoover.image_on_mouse_enter(
            button_1, root.button_1_hoov_img))
        button_1.bind("<Leave>", lambda x: Hoover.image_on_mouse_leave(
            button_1, root.button_1_img))

        button_1.pack(side='top', pady=4, padx=4)

        # Button Profile
        button_2 = tk.Button(self.left_menu)

        button_2_load = Image.open('assets/hprof.png')
        root.button_2_img = ImageTk.PhotoImage(button_2_load)

        button_2_hoov_load = Image.open('assets/search_hoover.png')
        root.button_2_hoov_img = ImageTk.PhotoImage(button_2_hoov_load)

        button_2.config(bd=1,
                        bg=colors['menu_bg'],
                        activebackground=colors['button_activebg'],
                        image=root.button_2_img,
                        relief='flat',
                        command=check_button)

        button_2.bind("<Enter>", lambda x: Hoover.bg_on_mouse_enter(
            button_2, colors['button_hoover']))
        button_2.bind("<Leave>", lambda x: Hoover.bg_on_mouse_leave(
            button_2, colors['menu_bg']))

        button_2.pack(side='top', pady=4, padx=4)

    def top_menu_widgets(self):
        button_1 = tk.Button(self.top_menu)
        button_1.config(text="TOP",
                        bd=1,
                        bg=colors['menu_bg'],
                        font=fonts['menu_normal'],
                        fg=colors['button_fg'],
                        activebackground=colors['button_activebg'],
                        activeforeground='red',
                        relief='flat',
                        command=check_button)
        button_1.pack(side='left')


# Functions
def check_button():
    print('button works!')


# Runtime
if __name__ == '__main__':
    main_frame = MainWindow(root)
    root.mainloop()
