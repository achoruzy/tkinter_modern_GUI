import tkinter as tk
import tkinter.tix as tx
from PIL import Image, ImageTk
import os
import sys

# tkinter apps needs to have a root window class
# for root wm (window manager) methods may be used to setup app window appearance

version = 'modulo v.0.01'

colors = {
    'bg': '#22313F',
    'working_bg': '#34495E',
    'menu_bg': '#2C3E50',
    'button_hoover': '#67809F',
    'button_activebg': '#34495E',
    'button_activefg': '#67809F',
    'button_fg': '#19B5FE',
    'infobox_fb': '#95A5A6',
    'infobox_afb': '#DADFE1',
    'infobox_abg': '#2C3E50'
}

fonts = {
    'menu_normal': ('roboto.ttf', 9),
    'menu_medium': ('roboto.ttf', 10),
    'menu_large': ('roboto.ttf', 12),
    'infobox_normal': ('roboto.ttf', 8)
}

# App window setup
root = tx.Tk()
root.wm_minsize(width=400, height=300)
root.configure(bg=colors['bg'])
root.geometry('800x600')
root.title('inDust modulo')
root.overrideredirect(0)
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

    @staticmethod
    def popup_on_mouse_enter(widget, text_str: str):
        """Function adds pop-up tooltip message"""
        tip = tx.Balloon(root)
        tip.message.configure(fg=colors['infobox_fb'])
        for sub in tip.subwidgets_all():
            sub.configure(bg=colors['bg'])
        tip.label.forget()
        tip.bind_widget(widget, balloonmsg=text_str)


# Application setup - inside app window
class MainWindow:
    def __init__(self, root):
        # Main Frame
        self.main_window = tk.Frame(root)
        self.main_window.config(bg=colors['bg'])
        self.main_window.pack(side='top', fill='both', expand=True)

        # Top Bar
        self.top_bar = tk.Frame(self.main_window)
        self.top_bar.config(bg=colors['bg'],
                            height=24)
        self.top_bar.pack(side='top', fill='x', expand=False)

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

        # Working Frame
        self.working = tk.Frame(self.main_window)
        self.working.config(bg=colors['working_bg'])
        self.working.pack(side='top', fill='both', expand=True)

        # Working Top Menu Frame
        self.working_top_menu = tk.Frame(self.working)
        self.working_top_menu.config(bg=colors['menu_bg'],
                                     width=38)
        self.working_top_menu.pack(side='top', fill='x', expand=False)

        # Widgets
        self.main_frame_widgets()
        self.top_bar_widgets()
        self.infobox_widgets()
        self.left_menu_widgets()
        self.working_top_menu_widgets()

    # Self methods

    def main_frame_widgets(self):
        pass

    def top_bar_widgets(self):
        # BUTTON 1 - FILE
        button_1 = tk.Button(self.top_bar)

        button_1.config(bd=0,
                        bg=colors['bg'],
                        activebackground=colors['button_hoover'],
                        activeforeground=colors['infobox_afb'],
                        text='File',
                        fg=colors['infobox_fb'],
                        font=fonts['menu_normal'],
                        relief='flat',
                        command=check_button)

        # Booton 1 hoover actions
        def event_enter_b1():
            Hoover.bg_on_mouse_enter(button_1, colors['infobox_abg'])

        def event_leave_b1():
            Hoover.bg_on_mouse_leave(button_1, colors['bg'])

        button_1.bind("<Enter>", lambda x: event_enter_b1())
        button_1.bind("<Leave>", lambda x: event_leave_b1())

        button_1.pack(side='left', padx=6, pady=1)

        # BUTTON 2 - EDIT
        button_2 = tk.Button(self.top_bar)

        button_2.config(bd=0,
                        bg=colors['bg'],
                        activebackground=colors['button_hoover'],
                        activeforeground=colors['infobox_afb'],
                        text='Edit',
                        fg=colors['infobox_fb'],
                        font=fonts['menu_normal'],
                        relief='flat',
                        command=check_button)

        # Booton 1 hoover actions
        def event_enter_b2():
            Hoover.bg_on_mouse_enter(button_2, colors['infobox_abg'])

        def event_leave_b2():
            Hoover.bg_on_mouse_leave(button_2, colors['bg'])

        button_2.bind("<Enter>", lambda x: event_enter_b2())
        button_2.bind("<Leave>", lambda x: event_leave_b2())

        button_2.pack(side='left', padx=6, pady=1)

        # BUTTON 3 - VIEW
        button_3 = tk.Button(self.top_bar)

        button_3.config(bd=0,
                        bg=colors['bg'],
                        activebackground=colors['button_hoover'],
                        activeforeground=colors['infobox_afb'],
                        text='View',
                        fg=colors['infobox_fb'],
                        font=fonts['menu_normal'],
                        relief='flat',
                        command=check_button)

        # Booton 1 hoover actions
        def event_enter_b3():
            Hoover.bg_on_mouse_enter(button_3, colors['infobox_abg'])

        def event_leave_b3():
            Hoover.bg_on_mouse_leave(button_3, colors['bg'])

        button_3.bind("<Enter>", lambda x: event_enter_b3())
        button_3.bind("<Leave>", lambda x: event_leave_b3())

        button_3.pack(side='left', padx=6, pady=1)

        # BUTTON 4 - HELP
        button_4 = tk.Button(self.top_bar)

        button_4.config(bd=0,
                        bg=colors['bg'],
                        activebackground=colors['button_hoover'],
                        activeforeground=colors['infobox_afb'],
                        text='Help',
                        fg=colors['infobox_fb'],
                        font=fonts['menu_normal'],
                        relief='flat',
                        command=check_button)

        # Booton 1 hoover actions
        def event_enter_b4():
            Hoover.bg_on_mouse_enter(button_4, colors['infobox_abg'])

        def event_leave_b4():
            Hoover.bg_on_mouse_leave(button_4, colors['bg'])

        button_4.bind("<Enter>", lambda x: event_enter_b4())
        button_4.bind("<Leave>", lambda x: event_leave_b4())

        button_4.pack(side='left', padx=6, pady=1)

        # BUTTON 0 - Exit
        button_0 = tk.Button(self.top_bar)

        button_0.config(bd=0,
                        bg=colors['bg'],
                        activebackground=colors['button_hoover'],
                        activeforeground=colors['infobox_afb'],
                        text='Exit',
                        fg=colors['infobox_fb'],
                        font=fonts['menu_normal'],
                        relief='flat',
                        command=tk._exit)

        # Booton 1 hoover actions
        def event_enter_b0():
            Hoover.bg_on_mouse_enter(button_0, colors['infobox_abg'])

        def event_leave_b0():
            Hoover.bg_on_mouse_leave(button_0, colors['bg'])

        button_0.bind("<Enter>", lambda x: event_enter_b0())
        button_0.bind("<Leave>", lambda x: event_leave_b0())

        button_0.pack(side='right', padx=6, pady=1)

    def infobox_widgets(self):
        # BUTTON 1 - VERSION
        button_1 = tk.Button(self.infobox)

        button_1.config(bd=0,
                        bg=colors['bg'],
                        activebackground=colors['button_hoover'],
                        activeforeground=colors['infobox_afb'],
                        text=version,
                        fg=colors['infobox_fb'],
                        font=fonts['infobox_normal'],
                        relief='flat',
                        command=check_button)

        # Booton 1 hoover actions
        def event_enter_b1():
            Hoover.bg_on_mouse_enter(button_1, colors['infobox_abg'])

        def event_leave_b1():
            Hoover.bg_on_mouse_leave(button_1, colors['bg'])

        button_1.bind("<Enter>", lambda x: event_enter_b1())
        button_1.bind("<Leave>", lambda x: event_leave_b1())

        button_1.pack(side='left', padx=6, pady=1)

        # BUTTON 2 - STATUS
        button_2 = tk.Button(self.infobox)

        button_2.config(bd=0,
                        bg=colors['bg'],
                        activebackground=colors['button_hoover'],
                        activeforeground=colors['infobox_afb'],
                        text='Status: '+'OFFLINE',
                        fg=colors['infobox_fb'],
                        font=fonts['infobox_normal'],
                        relief='flat',
                        command=check_button)

        # Booton 1 hoover actions
        def event_enter_b2():
            Hoover.bg_on_mouse_enter(button_2, colors['infobox_abg'])

        def event_leave_b2():
            Hoover.bg_on_mouse_leave(button_2, colors['bg'])

        button_2.bind("<Enter>", lambda x: event_enter_b2())
        button_2.bind("<Leave>", lambda x: event_leave_b2())

        button_2.pack(side='right', padx=6, pady=1)

    def left_menu_widgets(self):
        # BUTTON 1 - SEARCH
        button_1 = tk.Button(self.left_menu)

        button_1_load = Image.open('assets/check_50.png')
        root.button_1_img = ImageTk.PhotoImage(button_1_load)

        button_1_hov_load = Image.open('assets/check_100.png')
        root.button_1_hov_img = ImageTk.PhotoImage(button_1_hov_load)

        button_1.config(bd=0,
                        bg=colors['menu_bg'],
                        activebackground=colors['button_activebg'],
                        image=root.button_1_img,
                        relief='flat',
                        command=check_button)

        # Button 1 hoover actions
        button_1_tipmsg = 'Structure members'
        Hoover.popup_on_mouse_enter(button_1, button_1_tipmsg)

        def event_enter_b1():
            Hoover.image_on_mouse_enter(button_1, root.button_1_hov_img)

        def event_leave_b1():
            Hoover.image_on_mouse_leave(button_1, root.button_1_img)

        button_1.bind("<Enter>", lambda x: event_enter_b1())
        button_1.bind("<Leave>", lambda x: event_leave_b1())

        button_1.pack(side='top', pady=4, padx=4)

        # BUTTON 2 - PROFILE
        button_2 = tk.Button(self.left_menu)

        button_2_load = Image.open('assets/result_50.png')
        root.button_2_img = ImageTk.PhotoImage(button_2_load)

        button_2_hov_load = Image.open('assets/result_100.png')
        root.button_2_hov_img = ImageTk.PhotoImage(button_2_hov_load)

        button_2.config(bd=0,
                        bg=colors['menu_bg'],
                        activebackground=colors['button_activebg'],
                        image=root.button_2_img,
                        relief='flat',
                        command=check_button)

        # Button 2 hoover actions
        button_2_tipmsg = 'Analysis'
        Hoover.popup_on_mouse_enter(button_2, button_2_tipmsg)

        def event_enter_b2():
            Hoover.image_on_mouse_enter(button_2, root.button_2_hov_img)

        def event_leave_b2():
            Hoover.image_on_mouse_leave(button_2, root.button_2_img)

        button_2.bind("<Enter>", lambda x: event_enter_b2())
        button_2.bind("<Leave>", lambda x: event_leave_b2())

        button_2.pack(side='top', pady=4, padx=4)

        # BUTTON 3 - GRAPH
        button_3 = tk.Button(self.left_menu)

        button_3_load = Image.open('assets/graph_50.png')
        root.button_3_img = ImageTk.PhotoImage(button_3_load)

        button_3_hov_load = Image.open('assets/graph_100.png')
        root.button_3_hov_img = ImageTk.PhotoImage(button_3_hov_load)

        button_3.config(bd=0,
                        bg=colors['menu_bg'],
                        activebackground=colors['button_activebg'],
                        image=root.button_3_img,
                        relief='flat',
                        command=check_button)

        # Button 3 hoover actions
        button_3_tipmsg = 'Result'
        Hoover.popup_on_mouse_enter(button_3, button_3_tipmsg)

        def event_enter_b3():
            Hoover.image_on_mouse_enter(button_3, root.button_3_hov_img)

        def event_leave_b3():
            Hoover.image_on_mouse_leave(button_3, root.button_3_img)

        button_3.bind("<Enter>", lambda x: event_enter_b3())
        button_3.bind("<Leave>", lambda x: event_leave_b3())

        button_3.pack(side='top', pady=4, padx=4)

        # BUTTON 4 - SHIP
        button_4 = tk.Button(self.left_menu)

        button_4_load = Image.open('assets/ship_50.png')
        root.button_4_img = ImageTk.PhotoImage(button_4_load)

        button_4_hov_load = Image.open('assets/ship_100.png')
        root.button_4_hov_img = ImageTk.PhotoImage(button_4_hov_load)

        button_4.config(bd=0,
                        bg=colors['menu_bg'],
                        activebackground=colors['button_activebg'],
                        image=root.button_4_img,
                        relief='flat',
                        command=check_button)

        # Button 4 hoover actions
        button_4_tipmsg = 'Class methods'
        Hoover.popup_on_mouse_enter(button_4, button_4_tipmsg)

        def event_enter_b4():
            Hoover.image_on_mouse_enter(button_4, root.button_4_hov_img)

        def event_leave_b4():
            Hoover.image_on_mouse_leave(button_4, root.button_4_img)

        button_4.bind("<Enter>", lambda x: event_enter_b4())
        button_4.bind("<Leave>", lambda x: event_leave_b4())

        button_4.pack(side='top', pady=4, padx=4)

        # BUTTON 0 - BOTTOM OPTIONS
        button_0 = tk.Button(self.left_menu)

        button_0_load = Image.open('assets/options_50.png')
        root.button_0_img = ImageTk.PhotoImage(button_0_load)

        button_0_hov_load = Image.open('assets/options_100.png')
        root.button_0_hov_img = ImageTk.PhotoImage(button_0_hov_load)

        button_0.config(bd=0,
                        bg=colors['menu_bg'],
                        activebackground=colors['button_activebg'],
                        image=root.button_0_img,
                        relief='flat',
                        command=check_button)

        # Button 0 hoover actions
        button_0_tipmsg = 'Settings'
        Hoover.popup_on_mouse_enter(button_0, button_0_tipmsg)

        def event_enter_b0():
            Hoover.image_on_mouse_enter(button_0, root.button_0_hov_img)

        def event_leave_b0():
            Hoover.image_on_mouse_leave(button_0, root.button_0_img)

        button_0.bind("<Enter>", lambda x: event_enter_b0())
        button_0.bind("<Leave>", lambda x: event_leave_b0())

        button_0.pack(side='bottom', pady=4, padx=4)

    def working_top_menu_widgets(self):
        # BUTTON 1
        button_1 = tk.Button(self.working_top_menu)
        button_1.config(bd=0,
                        bg=colors['working_bg'],
                        activebackground=colors['button_hoover'],
                        activeforeground=colors['infobox_afb'],
                        text='Profile library',
                        fg=colors['infobox_fb'],
                        font=fonts['menu_normal'],
                        relief='flat',
                        command=check_button)

        # Booton 1 hoover actions
        def event_enter_b1():
            Hoover.bg_on_mouse_enter(button_1, colors['button_hoover'])

        def event_leave_b1():
            Hoover.bg_on_mouse_leave(button_1, colors['working_bg'])

        button_1.bind("<Enter>", lambda x: event_enter_b1())
        button_1.bind("<Leave>", lambda x: event_leave_b1())

        button_1.pack(side='left', padx=4)

        # BUTTON 2
        button_2 = tk.Button(self.working_top_menu)
        button_2.config(bd=0,
                        bg=colors['working_bg'],
                        activebackground=colors['button_hoover'],
                        activeforeground=colors['infobox_afb'],
                        text='Material library',
                        fg=colors['infobox_fb'],
                        font=fonts['menu_normal'],
                        relief='flat',
                        command=check_button)

        # Booton 2 hoover actions
        def event_enter_b2():
            Hoover.bg_on_mouse_enter(button_2, colors['button_hoover'])

        def event_leave_b2():
            Hoover.bg_on_mouse_leave(button_2, colors['working_bg'])

        button_2.bind("<Enter>", lambda x: event_enter_b2())
        button_2.bind("<Leave>", lambda x: event_leave_b2())

        button_2.pack(side='left', padx=4)


# Functions
def check_button():
    print('button works!')


# Runtime
if __name__ == '__main__':
    main_frame = MainWindow(root)
    root.mainloop()
