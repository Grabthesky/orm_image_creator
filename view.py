import sys
import os
from controller import select_file, select_output_path, create_orm
import tkinter as tk
from PIL import Image, ImageTk

# Styles
color_dark = "#223241"
color_main = "#2B3E50"
color_light = "#3F5B76"
color_detail = "#6795C2"
color_detail_white = "#95B7D8"
color_white = "#eeeeee"
color_black = "#000000"
color_red = "#C04242"
color_red_light = "#E07676"

# Image variables
red_channel_file_path = None
green_channel_file_path = None
blue_channel_file_path = None
alpha_channel_file_path = None

def resource_path(relative_path):
    """Devuelve la ruta absoluta para archivos dentro del exe PyInstaller"""
    try:
        # Si estamos en el exe
        base_path = sys._MEIPASS
    except AttributeError:
        # Si estamos en desarrollo
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def change_color(event, color):
    event.widget.config(bg=color)

def btn_get_file(save_to):
    temp_file_path = select_file()

    if save_to == 0:
        global red_channel_file_path
        red_channel_file_path = temp_file_path
        if temp_file_path:
            img = open_and_resize_image(temp_file_path)
            red_canvas.create_image(0, 0, anchor="nw", image=img)
            red_canvas.image = img
        else:
            red_canvas.image = None
        print(f"Red path : {red_channel_file_path}")
    elif save_to == 1:
        global green_channel_file_path
        green_channel_file_path = temp_file_path
        if temp_file_path:
            img = open_and_resize_image(temp_file_path)
            green_canvas.create_image(0, 0, anchor="nw", image=img)
            green_canvas.image = img
        else:
            green_canvas.image = None
        print(f"Green path : {green_channel_file_path}")
    elif save_to == 2:
        global blue_channel_file_path
        blue_channel_file_path = temp_file_path
        if temp_file_path:
            img = open_and_resize_image(temp_file_path)
            blue_canvas.create_image(0, 0, anchor="nw", image=img)
            blue_canvas.image = img
        else:
            blue_canvas.image = None
        print(f"Blue path : {blue_channel_file_path}")
    elif save_to == 3:
        global alpha_channel_file_path
        alpha_channel_file_path = temp_file_path
        if temp_file_path:
            img = open_and_resize_image(temp_file_path)
            alpha_canvas.create_image(0, 0, anchor="nw", image=img)
            alpha_canvas.image = img
        else:
            alpha_canvas.image = None
        print(f"Alpha path : {alpha_channel_file_path}")

def reset_image(reest_to):
    if reest_to == 0:
        global red_channel_file_path
        red_channel_file_path = None
        red_canvas.image = None
    elif reest_to == 1:
        global green_channel_file_path
        green_channel_file_path = None
        green_canvas.image = None
    elif reest_to == 2:
        global blue_channel_file_path
        blue_channel_file_path = None
        blue_canvas.image = None
    elif reest_to == 3:
        global alpha_channel_file_path
        alpha_channel_file_path = None
        alpha_canvas.image = None


def open_and_resize_image(path):
    # Open and resize image
    img = Image.open(path)
    img = img.resize((preview_size[0], preview_size[1]))  # tsize of the preview
    return ImageTk.PhotoImage(img)

def convert_to_orm():
    print(f"Convert to ORM: \n{red_channel_file_path},")
    status_string.set("Creating ORM image")
    output_path = select_output_path()
    if output_path:
        try:
            create_orm(red_channel_file_path, green_channel_file_path, blue_channel_file_path, alpha_channel_file_path, output_path)
            status_string.set("ORM image created")
        except Exception as e:
           
            status_string.set("Arror creating ORM image")


def show_interface():
    window.mainloop()

# Config
preview_size = [100,100]

# -------------------------------------------------------
# ---------- Window creation and configuration ----------
# -------------------------------------------------------

# Window
window = tk.Tk()
window.title("ORM packer")
window.iconbitmap(resource_path("src/icon.ico"))
window.config(bg = color_main)

# Window size and position
window_width = 350
window_height = 600

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{x}+{y}") # width x height + posx + posy

# Main frame
main_frame = tk.Frame(
    master=window,
    bg=color_main,
    width=300,
    height=400
    )
main_frame.pack(
    padx=10, 
    pady=10
    )

# Close button
close_img = tk.PhotoImage(file=resource_path("src/close.png"))

# Red channel ambien occlusion
red_frame = tk.Frame(
    master=main_frame,
    bg=color_main
)
red_frame.pack(
    padx=10,
    pady=10,
    fill="x"
)

btn_red_channel = tk.Button(
    master=red_frame, 
    text="Red channel", 
    background=color_light,
    border=0,
    fg=color_white,
    pady=7,
    width=15,
    command=lambda: btn_get_file(0)
    )
btn_red_channel.bind("<Enter>", lambda e: change_color(e, color_detail))
btn_red_channel.bind("<Leave>", lambda e: change_color(e, color_light))
btn_red_channel.pack(
    padx=10, 
    pady=10,
    side=tk.LEFT
    )

btn_red_reset = tk.Button(
	red_frame, 
	image=close_img,
	bg=color_light,
	cursor="hand2",
    border=0,
    command=lambda: reset_image(0)
	)
btn_red_reset.bind("<Enter>", lambda e: change_color(e, color_red))
btn_red_reset.bind("<Leave>", lambda e: change_color(e, color_light))
btn_red_reset.pack(
    side=tk.LEFT
    )

red_preview = tk.Frame(
    red_frame, 
    bg=color_black,
    width=100, 
    height=100
    )
red_preview.pack(
    padx=10,
    side=tk.RIGHT
    )

red_canvas = tk.Canvas(
    red_preview, 
    width=100, 
    height=100, 
    bg=color_black, 
    highlightthickness=0
    )
red_canvas.pack()

# Green channel roughness
gree_frame = tk.Frame(
    master=main_frame,
    bg=color_main
)
gree_frame.pack(
    padx=10,
    pady=10,
    fill="x"
)

btn_green_channel = tk.Button(
    master=gree_frame, 
    text="Green channel", 
    background=color_light,
    border=0,
    fg=color_white,
    pady=7,
    width=15,
    command=lambda: btn_get_file(1)
    )
btn_green_channel.bind("<Enter>", lambda e: change_color(e, color_detail))
btn_green_channel.bind("<Leave>", lambda e: change_color(e, color_light))
btn_green_channel.pack(
    padx=10, 
    pady=10,
    side=tk.LEFT
    )

btn_green_reset = tk.Button(
	gree_frame, 
	image=close_img,
	bg=color_light,
	cursor="hand2",
    border=0,
    command=lambda: reset_image(1)
	)
btn_green_reset.bind("<Enter>", lambda e: change_color(e, color_red))
btn_green_reset.bind("<Leave>", lambda e: change_color(e, color_light))
btn_green_reset.pack(
    side=tk.LEFT
    )

gree_preview = tk.Frame(
    gree_frame, 
    bg=color_black, 
    width=100, 
    height=100)
gree_preview.pack(
    padx=10,
    side=tk.RIGHT
    )

green_canvas = tk.Canvas(
    gree_preview, 
    width=100, 
    height=100, 
    bg=color_black, 
    highlightthickness=0
    )
green_canvas.pack()

# Blue channel metalic
blue_frame = tk.Frame(
    master=main_frame,
    bg=color_main
)
blue_frame.pack(
    padx=10,
    pady=10,
    fill="x"
)

btn_blue_channel = tk.Button(
    master=blue_frame, 
    text="Blue channel", 
    background=color_light,
    border=0,
    fg=color_white,
    pady=7,
    width=15,
    command=lambda: btn_get_file(2)
    )
btn_blue_channel.bind("<Enter>", lambda e: change_color(e, color_detail))
btn_blue_channel.bind("<Leave>", lambda e: change_color(e, color_light))
btn_blue_channel.pack(
    padx=10, 
    pady=10,
    side=tk.LEFT
    )

btn_blue_reset = tk.Button(
	blue_frame, 
	image=close_img,
	bg=color_light,
	cursor="hand2",
    border=0,
    command=lambda: reset_image(2)
	)
btn_blue_reset.bind("<Enter>", lambda e: change_color(e, color_red))
btn_blue_reset.bind("<Leave>", lambda e: change_color(e, color_light))
btn_blue_reset.pack(
    side=tk.LEFT
    )

blue_preview = tk.Frame(
    blue_frame, 
    bg=color_black, 
    width=100, 
    height=100)
blue_preview.pack(
    padx=10,
    side=tk.RIGHT
    )

blue_canvas = tk.Canvas(
    blue_preview, 
    width=100, 
    height=100, 
    bg=color_black, 
    highlightthickness=0
    )
blue_canvas.pack()

# Alpha channel Alpha/Emission/Height
alpha_frame = tk.Frame(
    master=main_frame,
    bg=color_main
)
alpha_frame.pack(
    padx=10,
    pady=10,
    fill="x"
)

btn_alpha_channel = tk.Button(
    master=alpha_frame, 
    text="Alpha channel", 
    background=color_light,
    border=0,
    fg=color_white,
    pady=7,
    width=15,
    command=lambda: btn_get_file(3)
    )
btn_alpha_channel.bind("<Enter>", lambda e: change_color(e, color_detail))
btn_alpha_channel.bind("<Leave>", lambda e: change_color(e, color_light))
btn_alpha_channel.pack(
    padx=10, 
    pady=10,
    side=tk.LEFT
    )

btn_alpha_reset = tk.Button(
	alpha_frame, 
	image=close_img,
	bg=color_light,
	cursor="hand2",
    border=0,
    command=lambda: reset_image(3)
	)
btn_alpha_reset.bind("<Enter>", lambda e: change_color(e, color_red))
btn_alpha_reset.bind("<Leave>", lambda e: change_color(e, color_light))
btn_alpha_reset.pack(
    side=tk.LEFT
    )

alpha_preview = tk.Frame(
    alpha_frame, 
    bg=color_black, 
    width=100, 
    height=100)
alpha_preview.pack(
    padx=10,
    side=tk.RIGHT
    )

alpha_canvas = tk.Canvas(
    alpha_preview, 
    width=100, 
    height=100, 
    bg=color_black, 
    highlightthickness=0
    )
alpha_canvas.pack()

# Convert button
conver_btn = tk.Button(
    master=main_frame,
    text="Convert",
    border=0,
    bg=color_red,
    fg=color_white,
    padx=50,
    pady=7,
    command=convert_to_orm
)
conver_btn.bind("<Enter>", lambda e: change_color(e, color_red_light))
conver_btn.bind("<Leave>", lambda e: change_color(e, color_red))
conver_btn.pack(
    pady=10
)

# Status label
status_string = tk.StringVar()
status_string.set("Select the images to convert")
status_label = tk.Label(
    bg=color_main,
    fg=color_detail_white,
    text="Select the images to convert",
    textvariable=status_string,
    master=main_frame
)
status_label.pack()