# Copyright (c) 2021 Arkadiusz Choruży
# License: MIT

import tkinter as tk
import tkinter.tix as tx
from PIL import Image, ImageTk

# tkinter apps needs to have a root window class
# for root wm (window manager) methods may be used to setup app window appearance

version = '0.004'

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
root.title('inDust modulo')
root.config(bd=2)
root.overrideredirect(1)
root.wm_resizable(True, True)
root.iconbitmap('assets/favicon.ico')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f'800x600+{int(screen_width/4)}+{int(screen_height/4)}')


class Hoover:
    """Hoover class provides static methods for mouse cursor hoovering functions such as button color change on hoovering."""
    
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

    @staticmethod
    def floating_window(root, widget):
        """ Function alows to drag windows/widgets using mouse """

        def start_move(event):
            root.x = event.x
            root.y = event.y

        def stop_move(event):
            root.x = None
            root.y = None

        def do_move(event):
            dx = event.x - root.x
            dy = event.y - root.y
            x = root.winfo_x() + dx
            y = root.winfo_y() + dy
            root.geometry(f"+{x}+{y}")

        widget.bind("<ButtonPress-1>", start_move)
        widget.bind("<ButtonRelease-1>", stop_move)
        widget.bind("<B1-Motion>", do_move)


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
        button_1 = tk.Menubutton(self.top_bar)

        button_1.config(bd=0,
                        bg=colors['bg'],
                        activebackground=colors['button_hoover'],
                        activeforeground=colors['infobox_afb'],
                        text='File',
                        fg=colors['infobox_fb'],
                        font=fonts['menu_normal'],
                        relief='flat')

        # Button 1 subbutons
        button_1.menu = tk.Menu(button_1)
        button_1["menu"] = button_1.menu
        button_1.menu.configure(bg=colors['menu_bg'],
                                bd=0,
                                activebackground=colors['button_hoover'],
                                activeforeground=colors['infobox_afb'],
                                fg=colors['infobox_fb'],
                                font=fonts['menu_normal'],
                                relief='flat',
                                tearoff=0)

        button_1.menu.add_command(label='New File',
                                  compound=tk.LEFT, command=check_button,
                                  accelerator="Ctrl+N", underline=0)
        button_1.menu.add_separator()
        button_1.menu.add_command(label='Open File',
                                  compound=tk.LEFT, command=check_button,
                                  accelerator="Ctrl+O", underline=0)
        button_1.menu.add_separator()
        button_1.menu.add_command(label='Exit',
                                  compound=tk.LEFT, command=check_button,
                                  accelerator="Alt+F4", underline=0)

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
        button_t0 = tk.Button(self.top_bar)

        button_t0_load = Image.open('assets/close_50.png')
        root.button_t0_img = ImageTk.PhotoImage(button_t0_load)

        button_t0_hov_load = Image.open('assets/close_100.png')
        root.button_t0_hov_img = ImageTk.PhotoImage(button_t0_hov_load)

        button_t0.config(bd=0,
                         bg=colors['bg'],
                         activebackground=colors['button_hoover'],
                         width=40,
                         image=root.button_t0_img,
                         relief='flat',
                         command=tk._exit)

        # Booton 0 hoover actions
        def event_enter_bt0():
            Hoover.bg_on_mouse_enter(button_t0, 'red')
            Hoover.image_on_mouse_enter(button_t0, root.button_t0_hov_img)

        def event_leave_bt0():
            Hoover.bg_on_mouse_leave(button_t0, colors['bg'])
            Hoover.image_on_mouse_leave(button_t0, root.button_t0_img)

        button_t0.bind("<Enter>", lambda x: event_enter_bt0())
        button_t0.bind("<Leave>", lambda x: event_leave_bt0())

        button_t0.pack(side='right', padx=0, pady=0)

        # BUTTON 00 - Maximize
        button_t00 = tk.Button(self.top_bar)

        button_t00_load = Image.open('assets/fullwin_50.png')
        root.button_t00_img = ImageTk.PhotoImage(button_t00_load)

        button_t00_hov_load = Image.open('assets/fullwin_100.png')
        root.button_t00_hov_img = ImageTk.PhotoImage(button_t00_hov_load)

        button_t00.config(bd=0,
                          bg=colors['bg'],
                          activebackground=colors['button_hoover'],
                          width=40,
                          image=root.button_t00_img,
                          relief='flat'
                          )

        # Booton 00 hoover actions
        def event_enter_bt00():
            Hoover.bg_on_mouse_enter(button_t00, colors['menu_bg'])
            Hoover.image_on_mouse_enter(button_t00, root.button_t00_hov_img)

        def event_leave_bt00():
            Hoover.bg_on_mouse_leave(button_t00, colors['bg'])
            Hoover.image_on_mouse_leave(button_t00, root.button_t00_img)

        button_t00.bind("<Enter>", lambda x: event_enter_bt00())
        # button_t00.bind("<Clicked>", button_t00.config(
        #     command=root.geometry(f'{screen_width}x{screen_height}+0+0')))
        button_t00.bind("<Leave>", lambda x: event_leave_bt00())

        button_t00.pack(side='right', padx=0, pady=0)

        # BUTTON 000 - Minimize
        button_t000 = tk.Button(self.top_bar)

        button_t000_load = Image.open('assets/minimize_50.png')
        root.button_t000_img = ImageTk.PhotoImage(button_t000_load)

        button_t000_hov_load = Image.open('assets/minimize_100.png')
        root.button_t000_hov_img = ImageTk.PhotoImage(button_t000_hov_load)

        button_t000.config(bd=0,
                           bg=colors['bg'],
                           activebackground=colors['button_hoover'],
                           width=40,
                           image=root.button_t000_img,
                           relief='flat',
                           command=root.iconify)

        # Booton 000 hoover actions
        def event_enter_bt000():
            Hoover.bg_on_mouse_enter(button_t000, colors['menu_bg'])
            Hoover.image_on_mouse_enter(button_t000, root.button_t000_hov_img)

        def event_leave_bt000():
            Hoover.bg_on_mouse_leave(button_t000, colors['bg'])
            Hoover.image_on_mouse_leave(button_t000, root.button_t000_img)

        button_t000.bind("<Enter>", lambda x: event_enter_bt000())
        button_t000.bind("<Leave>", lambda x: event_leave_bt000())

        button_t000.pack(side='right', padx=0, pady=0)

        # -----------------

        # TITLE / GRAB WINDOW

        title_label = tk.Label(self.top_bar)
        title_label.config(bg=colors['bg'],
                           text='Modulo',
                           fg=colors['infobox_fb'],
                           font=fonts['menu_normal'],
                           justify='center')
        title_label.pack(fill='x')

        Hoover.floating_window(root, title_label)

        # -----------------

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
        button_1_tipmsg = 'Click for more information about the software.'
        Hoover.popup_on_mouse_enter(button_1, button_1_tipmsg)

        def event_enter_b1():
            Hoover.bg_on_mouse_enter(button_1, colors['infobox_abg'])

        def event_leave_b1():
            Hoover.bg_on_mouse_leave(button_1, colors['bg'])

        button_1.bind("<Enter>", lambda x: event_enter_b1())
        button_1.bind("<Leave>", lambda x: event_leave_b1())

        button_1.pack(side='left', padx=6, pady=1)

        # STATUS DOT

        dot_red = Image.open('assets/dot_red.png')
        root.dot_red = ImageTk.PhotoImage(dot_red)

        status_dot = tk.Label(self.infobox)
        status_dot.config(bd=0,
                          bg=colors['bg'],
                          activebackground=colors['button_hoover'],
                          activeforeground=colors['infobox_afb'],
                          image=root.dot_red,
                          fg=colors['infobox_fb'],
                          font=fonts['infobox_normal']
                          )

        status_dot.pack(side='left', padx=1, pady=1)

        # BUTTON 2 - STATUS
        button_2 = tk.Button(self.infobox)

        button_2.config(bd=0,
                        bg=colors['bg'],
                        activebackground=colors['button_hoover'],
                        activeforeground=colors['infobox_afb'],
                        text='OFFLINE',
                        fg=colors['infobox_fb'],
                        font=fonts['infobox_normal'],
                        relief='flat',
                        command=check_button)

        # Booton 2 hoover actions
        button_2_tipmsg = 'Connection to the server status is: ' + \
            'OFFLINE'+'. Click for action.'
        Hoover.popup_on_mouse_enter(button_2, button_2_tipmsg)

        def event_enter_b2():
            Hoover.bg_on_mouse_enter(button_2, colors['infobox_abg'])

        def event_leave_b2():
            Hoover.bg_on_mouse_leave(button_2, colors['bg'])

        button_2.bind("<Enter>", lambda x: event_enter_b2())
        button_2.bind("<Leave>", lambda x: event_leave_b2())

        button_2.pack(side='left', padx=3, pady=1)

    def left_menu_widgets(self):
        # BUTTON 1 - ENTRY DATA
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
        button_1_tipmsg = 'Entry data'
        Hoover.popup_on_mouse_enter(button_1, button_1_tipmsg)

        def event_enter_b1():
            Hoover.image_on_mouse_enter(button_1, root.button_1_hov_img)

        def event_leave_b1():
            Hoover.image_on_mouse_leave(button_1, root.button_1_img)

        button_1.bind("<Enter>", lambda x: event_enter_b1())
        button_1.bind("<Leave>", lambda x: event_leave_b1())

        button_1.pack(side='top', pady=4, padx=4)

        # BUTTON 2 - ANALYSIS
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

        # BUTTON 0 - USER OPTIONS
        button_00 = tk.Button(self.left_menu)

        button_00_load = Image.open('assets/user_50.png')
        root.button_00_img = ImageTk.PhotoImage(button_00_load)

        button_00_hov_load = Image.open('assets/user_100.png')
        root.button_00_hov_img = ImageTk.PhotoImage(button_00_hov_load)

        button_00.config(bd=0,
                         bg=colors['menu_bg'],
                         activebackground=colors['button_activebg'],
                         image=root.button_00_img,
                         relief='flat',
                         command=check_button)

        # Button 00 hoover actions
        button_00_tipmsg = 'User options'
        Hoover.popup_on_mouse_enter(button_00, button_00_tipmsg)

        def event_enter_b00():
            Hoover.image_on_mouse_enter(button_00, root.button_00_hov_img)

        def event_leave_b00():
            Hoover.image_on_mouse_leave(button_00, root.button_00_img)

        button_00.bind("<Enter>", lambda x: event_enter_b00())
        button_00.bind("<Leave>", lambda x: event_leave_b00())

        button_00.pack(side='bottom', pady=4, padx=4)

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
