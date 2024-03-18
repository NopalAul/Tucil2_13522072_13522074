import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from tkinter import *
from tkinter import messagebox
from time import process_time
import os
import sys


################### ALGORITMA ###################
# Pembuat titik kontrol tengah
def generate_control_points(points):
    control_points = []
    for i in range(len(points) - 1):
        control_points.append((points[i] + points[i + 1]) / 2)
    if len(control_points) > 1:
        recursive_control_points = generate_control_points(control_points)
        control_points.extend(recursive_control_points)
    return control_points

# Divide and Conquer kurva Bezier
def divide_and_conquer(points, iterations):
    global all_points

    # Basis case
    if iterations == 0:
        return [points[0], points[-1]]

    # Membuat titik kontrol tengah
    control_points = generate_control_points(points)
    mid_point = control_points[-1]

    all_points.append(control_points)

    # Kumpulan titik bagian kiri
    array_left_points = []
    array_left_points.append(points[0])
    array_left_points.append(control_points[0])

    len_points = len(points)
    i = len_points - 1
    while i < len(control_points):
        array_left_points.append(control_points[i])
        len_points -= 1
        i += len_points - 1

    # Kumpulan titik bagian kanan
    array_right_points = []
    control_points.reverse()
    array_right_points.append(control_points[0])
    array_right_points.append(control_points[1])

    start_index = 3
    i = start_index
    while i < len(control_points):
        array_right_points.append(control_points[i])
        i += start_index
        start_index += 1
    
    array_right_points.append(points[-1])

    # Rekursi pada bagian kiri dan kanan
    left_points = divide_and_conquer(array_left_points, iterations - 1)
    right_points = divide_and_conquer(array_right_points, iterations - 1)

    # Menggabungkan hasil dari kedua submasalah
    return left_points[:-1] + [mid_point] +  right_points

# Animasi proses pembentukan plot kurva Bezier
def animate_curve(frame):
    global points, all_points, iterations, ax, canvas

    # Start time
    start = process_time()
    curve_points = divide_and_conquer(points, frame + 1)
    # End time
    end = process_time()
    timer = round((end - start)*1000, 2)
    time_result.config(text=f"{timer} ms")

    ax.clear()

    # Plot titik kontrol
    ax.plot([point[0] for point in points], [point[1] for point in points], marker='o', linestyle='--', color='red')

    for point in all_points:
        x = [point[0] for point in point]
        y = [point[1] for point in point]
        ax.plot(x, y, marker='o', linestyle='-', alpha=0.5)
    all_points.clear()

    # Plot kurva Bezier
    x = [point[0] for point in curve_points]
    y = [point[1] for point in curve_points]
    ax.plot(x, y, marker='o', linestyle='-', color='blue')

    # Menambahkan label
    ax.set_title('Bezier Curve (Iteration {})'.format(frame + 1))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    canvas.draw()

# Plot kurva Bezier
def plot_bezier_curve():
    global points, all_points, iterations
    # Validasi titik
    if len(points) < 3:
        messagebox.showerror("Error", "Please input at least 3 points")
        return
    
    # Validasi input
    iteration_str = iteration_entry.get()
    if iteration_str == '':
        messagebox.showerror("Error", "Please input the number of iterations")
        return
    try:
        iterations = int(iteration_str)
    except ValueError:
        messagebox.showerror("Error", "Iterations must be a number")
        return

    # Membuat plot kurva Bezier
    ani = animation.FuncAnimation(fig, animate_curve, frames=iterations, repeat=False)

    canvas.draw()

# Menambahkan titik kontrol masukan
def add_point():
    x_str = x_entry.get()
    y_str = y_entry.get()

    # Validasi input
    if x_str == '':
        messagebox.showerror("Error", "Please input X coordinate")
        return
    if y_str == '':
        messagebox.showerror("Error", "Please input Y coordinate")
        return
    try:
        x = float(x_str)
        y = float(y_str)
    except ValueError:
        messagebox.showerror("Error", "X and Y must be a number")
        return
    point = np.array([x, y])
    points.append(point)
    point_listbox.insert(END, f"({x}, {y})")

# Menghapus ulang semua titik kontrol
def reset_points():
    global points, all_points
    points = []
    all_points = []
    point_listbox.delete(0, END)




################### TKINTER GUI ###################
# ASSETS PATH
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Main window
window = Tk()
widht = 990
height = 704
x = (window.winfo_screenwidth()//2) - (widht//2) 
y = (window.winfo_screenheight()//2) - (height//2)
window.geometry(f'{widht}x{height}+{x}+{y}')
window.resizable(False, False)
window.title('BJIR - bézier curve generator')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

page1 = Frame(window)
page2 = Frame(window)

for frame in (page1, page2):
    frame.grid(row=0, column=0, sticky='nsew')

# Munculkan page lain
def show_frame(frame):
    frame.tkraise()

show_frame(page1)


############## PAGE 1: HOME ##############
# Background
page1.configure(bg='#FBFEFE')

# Title
img_path = resource_path("assets/bjirlogo.png")
img_title = PhotoImage(file=img_path)
Label(page1, image=img_title, bg='#FBFEFE').pack(pady=(160, 0))

# Subtitle
subtitle_path = resource_path("assets/bjir.png")
subtitle_img = PhotoImage(file=subtitle_path)
Label(page1, image=subtitle_img, bg='#FBFEFE').pack(pady=(50, 0))

# Try me button
try_path = resource_path("assets/tryme.png")
try_img = PhotoImage(file=try_path)
try_button = Button(page1, image=try_img, bg='#FBFEFE', bd=0, command=lambda: show_frame(page2)).place(relx=0.5, rely=0.65, anchor=CENTER)


############## PAGE 2: GENERATOR ##############
# Background
page2.configure(bg='#FBFEFE')

# Title
title2_path = resource_path("assets/generator.png")
title2_img = PhotoImage(file=title2_path)
Label(page2, image=title2_img, bg='#FBFEFE').place(x=408, y=73)

# Back button
back_path = resource_path("assets/back2.png")
back_img = PhotoImage(file=back_path)
back_button = Button(page2, image=back_img, bg='#FBFEFE', bd=0, command=lambda: show_frame(page1)).place(x=52, y=84)

# Input X
x_input_path = resource_path("assets/x.png")
x_input_img = PhotoImage(file=x_input_path)
Label(page2, image=x_input_img, bg='#FBFEFE').place(x=52, y=170)
x_entry = Entry(page2, width=3, font=('Arial', 12), border=0, bg='#F8EDEE')
x_entry.place(x=188, y=184)

# Input Y
y_input_path = resource_path("assets/y.png")
y_input_img = PhotoImage(file=y_input_path)
Label(page2, image=y_input_img, bg='#FBFEFE').place(x=52, y=240)
y_entry = Entry(page2, width=3, font=('Arial', 12), border=0, bg='#F8EDEE')
y_entry.place(x=188, y=254)

# Add point button
add_point_path = resource_path("assets/addpoint.png")
add_point_img = PhotoImage(file=add_point_path)
add_point_button = Button(page2, image=add_point_img, bg='#FBFEFE', bd=0, command=add_point)
add_point_button.place(x=41, y=297)

# Point container
point_container_path = resource_path("assets/pointcontainer.png")
point_container_img = PhotoImage(file=point_container_path)
Label(page2, image=point_container_img, bg='#FBFEFE').place(x=52, y=361)
point_listbox = Listbox(page2, width=18, height=10, font=('Arial', 12), border=0, bg='#F8EDEE')
point_listbox.place(x=58, y=372)

# Iteration
iteration_path = resource_path("assets/iteration.png")
iteration_img = PhotoImage(file=iteration_path)
Label(page2, image=iteration_img, bg='#FBFEFE').place(x=49, y=620)
iteration_entry = Entry(page2, width=3, font=('Arial', 12), border=0, bg='#F8EDEE')
iteration_entry.place(x=183, y=634)

# Generate button
generate_path = resource_path("assets/generate.png")
generate_img = PhotoImage(file=generate_path)
generate_button = Button(page2, image=generate_img, bg='#FBFEFE', bd=0, command=plot_bezier_curve)
generate_button.place(x=245, y=600)

# Reset button
reset_path = resource_path("assets/reset.png")
reset_img = PhotoImage(file=reset_path)
reset_button = Button(page2, image=reset_img, bg='#FBFEFE', bd=0, command=reset_points)
reset_button.place(x=465, y=600)

# Container hasil
hasil_path = resource_path("assets/hasil.png")
hasil_img = PhotoImage(file=hasil_path)
Label(page2, image=hasil_img, bg='#FBFEFE').place(x=272, y=133)

# Waktu eksekusi
time_path = resource_path("assets/time.png")
time_img = PhotoImage(file=time_path)
Label(page2, image=time_img, bg='#FBFEFE').place(x=700, y=599)
time_result = Label(page2, text="", font=('Arial', 12), bg='#F8EDEE')
time_result.place(x=780, y=648)

# Figure
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=page2)
canvas.get_tk_widget().place(x=280, y=140, width=630, height=430)

# Global Variables
points = []
all_points = []

# END
window.mainloop()