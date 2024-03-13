import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from time import process_time
import os
import sys


################### ALGORITMA ###################
def bezier_quadratic_divide_and_conquer(P0, P1, P2, iterations):
    if iterations == 0:
        return [P0, P2]

    # Menemukan titik kontrol tengah
    Q0 = (P0 + P1) / 2
    Q1 = (P1 + P2) / 2
    R = (Q0 + Q1) / 2

    # Rekursi pada submasalah
    left_points = bezier_quadratic_divide_and_conquer(P0, Q0, R, iterations - 1)
    right_points = bezier_quadratic_divide_and_conquer(R, Q1, P2, iterations - 1)

    # Menggabungkan hasil dari kedua submasalah
    return left_points[:-1] + [R] + right_points

def bezier_cubic_divide_and_conquer(P0, P1, P2, P3, iterations):
    if iterations == 0:
        return [P0, P3]

    # Menemukan titik kontrol tengah
    Q0 = (P0 + P1) / 2
    Q1 = (P1 + P2) / 2
    Q2 = (P2 + P3) / 2
    R0 = (Q0 + Q1) / 2
    R1 = (Q1 + Q2) / 2
    S = (R0 + R1) / 2

    # Rekursi pada submasalah
    left_points = bezier_cubic_divide_and_conquer(P0, Q0, R0, S, iterations - 1)
    right_points = bezier_cubic_divide_and_conquer(S, R1, Q2, P3, iterations - 1)

    # Menggabungkan hasil dari kedua submasalah
    return left_points[:-1] + [S] + right_points

def bezier_quartic_divide_and_conquer(P0, P1, P2, P3, P4, iterations):
    if iterations == 0:
        return [P0, P4]

    # Menemukan titik kontrol tengah
    Q0 = (P0 + P1) / 2
    Q1 = (P1 + P2) / 2
    Q2 = (P2 + P3) / 2
    Q3 = (P3 + P4) / 2
    R0 = (Q0 + Q1) / 2
    R1 = (Q1 + Q2) / 2
    R2 = (Q2 + Q3) / 2
    S0 = (R0 + R1) / 2
    S1 = (R1 + R2) / 2
    T = (S0 + S1) / 2

    # Rekursi pada submasalah
    left_points = bezier_quartic_divide_and_conquer(P0, Q0, R0, S0, T, iterations - 1)
    right_points = bezier_quartic_divide_and_conquer(T, S1, R2, Q3, P4, iterations - 1)

    # Menggabungkan hasil dari kedua submasalah
    return left_points[:-1] + [T] + right_points

def animate_curve(frame):
    global points, iterations, ax, canvas

    # Start time
    start = process_time()

    if len(points) == 3:
        P0 = np.array(points[0])
        P1 = np.array(points[1])
        P2 = np.array(points[2])
        curve_points = bezier_quadratic_divide_and_conquer(P0, P1, P2, frame + 1)
    elif len(points) == 4:
        P0 = np.array(points[0])
        P1 = np.array(points[1])
        P2 = np.array(points[2])
        P3 = np.array(points[3])
        curve_points = bezier_cubic_divide_and_conquer(P0, P1, P2, P3, frame + 1)
    elif len(points) == 5:
        P0 = np.array(points[0])
        P1 = np.array(points[1])
        P2 = np.array(points[2])
        P3 = np.array(points[3])
        P4 = np.array(points[4])
        curve_points = bezier_quartic_divide_and_conquer(P0, P1, P2, P3, P4, frame + 1)

    x = [point[0] for point in curve_points]
    y = [point[1] for point in curve_points]

    # Plot kurva Bezier
    ax.clear()
    ax.plot(x, y, marker='o', linestyle='-')

    # Plot titik kontrol
    ax.scatter([point[0] for point in points], [point[1] for point in points], color='red')

    # Menambahkan label
    ax.set_title('Bezier Curve (Iteration {})'.format(frame + 1))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    canvas.draw()

    # End time
    end = process_time()
    timer = round((end - start)*1000, 2)
    time_result.config(text=f"{timer} ms")

def plot_bezier_curve():
    global points, iterations
    iterations = int(iteration_entry.get())

    if len(points) == 3:
        ani = animation.FuncAnimation(fig, animate_curve, frames=iterations, repeat=False)
    elif len(points) == 4:
        ani = animation.FuncAnimation(fig, animate_curve, frames=iterations, repeat=False)
    elif len(points) == 5:
        ani = animation.FuncAnimation(fig, animate_curve, frames=iterations, repeat=False)

    canvas.draw()

def add_point():
    x = float(x_entry.get())
    y = float(y_entry.get())
    points.append([x, y])
    point_listbox.insert(END, f"({x}, {y})")

def reset_points():
    global points
    points = []
    point_listbox.delete(0, END)


# ASSETS PATH
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


################### TKINTER GUI ###################
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
Label(page2, image=title2_img, bg='#FBFEFE').place(x=443, y=73)

# Back button
back_path = resource_path("assets/back2.png")
back_img = PhotoImage(file=back_path)
back_button = Button(page2, image=back_img, bg='#FBFEFE', bd=0, command=lambda: show_frame(page1)).place(x=84, y=84)

# Input X
x_input_path = resource_path("assets/x.png")
x_input_img = PhotoImage(file=x_input_path)
Label(page2, image=x_input_img, bg='#FBFEFE').place(x=84, y=170)
x_entry = Entry(page2, width=3, font=('Arial', 12), border=0, bg='#F8EDEE')
x_entry.place(x=218, y=184)

# Input Y
y_input_path = resource_path("assets/y.png")
y_input_img = PhotoImage(file=y_input_path)
Label(page2, image=y_input_img, bg='#FBFEFE').place(x=84, y=240)
y_entry = Entry(page2, width=3, font=('Arial', 12), border=0, bg='#F8EDEE')
y_entry.place(x=218, y=254)

# Add point button
add_point_path = resource_path("assets/addpoint.png")
add_point_img = PhotoImage(file=add_point_path)
add_point_button = Button(page2, image=add_point_img, bg='#FBFEFE', bd=0, command=add_point)
add_point_button.place(x=73, y=297)

# Point container
point_container_path = resource_path("assets/pointcontainer.png")
point_container_img = PhotoImage(file=point_container_path)
Label(page2, image=point_container_img, bg='#FBFEFE').place(x=49, y=361)
point_listbox = Listbox(page2, width=26, height=11, font=('Arial', 12), border=0, bg='#F8EDEE')
point_listbox.place(x=56, y=372)

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
Label(page2, image=hasil_img, bg='#FBFEFE').place(x=339, y=162)

# Waktu eksekusi
time_path = resource_path("assets/time.png")
time_img = PhotoImage(file=time_path)
Label(page2, image=time_img, bg='#FBFEFE').place(x=700, y=599)
time_result = Label(page2, text="", font=('Arial', 12), bg='#F8EDEE')
time_result.place(x=780, y=648)

# Figure
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=page2)
canvas.get_tk_widget().place(x=350, y=171, width=558, height=395)

# Global Variables
points = []

# END
window.mainloop()