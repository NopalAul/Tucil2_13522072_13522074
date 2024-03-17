import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

def generate_control_points(points):
    control_points = []
    for i in range(len(points) - 1):
        control_points.append((points[i] + points[i + 1]) / 2)
    if len(control_points) > 1:
        recursive_control_points = generate_control_points(control_points)
        control_points.extend(recursive_control_points)
    return control_points

def divide_and_conquer(points, iterations):
    if iterations == 0:
        return [points[0], points[-1]]

    control_points = generate_control_points(points)
    mid_point = control_points[-1]

    array_left_points = []
    array_left_points.append(points[0])
    array_left_points.append(control_points[0])

    len_points = len(points)
    i = len_points - 1
    while i < len(control_points):
        array_left_points.append(control_points[i])
        len_points -= 1
        i += len_points - 1

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

    left_points = divide_and_conquer(array_left_points, iterations - 1)
    right_points = divide_and_conquer(array_right_points, iterations - 1)

    return left_points[:-1] + [mid_point] +  right_points

def animate_curve(frame):
    global points, iterations, ax, canvas

    curve_points = divide_and_conquer(points, frame + 1)

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

def plot_bezier_curve():
    global points, iterations
    iterations = int(iteration_entry.get())

    # if len(points) == 3:
    ani = animation.FuncAnimation(fig, animate_curve, frames=iterations, repeat=False)
    # elif len(points) == 4:
    #     ani = animation.FuncAnimation(fig, animate_curve, frames=iterations, repeat=False)
    # elif len(points) == 5:
    #     ani = animation.FuncAnimation(fig, animate_curve, frames=iterations, repeat=False)

    canvas.draw()

def add_point():
    x = float(x_entry.get())
    y = float(y_entry.get())
    point = np.array([x, y])
    points.append(point)
    print(f'np points: {point}')
    print(f'points: {points}')
    point_listbox.insert(tk.END, f"({x}, {y})")

def reset_points():
    global points
    points = []
    point_listbox.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("Bezier Curve Plotter")

# Labels
tk.Label(root, text="X:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, text="Y:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, text="Iterations:").grid(row=2, column=0, padx=5, pady=5, sticky="e")

# Entries
x_entry = tk.Entry(root)
x_entry.grid(row=0, column=1, padx=5, pady=5)
y_entry = tk.Entry(root)
y_entry.grid(row=1, column=1, padx=5, pady=5)
iteration_entry = tk.Entry(root)
iteration_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Point", command=add_point)
add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")
plot_button = tk.Button(root, text="Plot Bezier Curve", command=plot_bezier_curve)
plot_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")
reset_button = tk.Button(root, text="Reset Points", command=reset_points)
reset_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Point Listbox
point_listbox = tk.Listbox(root)
point_listbox.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Figure
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=2, rowspan=6, padx=5, pady=5, sticky="nsew")

# Global Variables
points = []

root.mainloop()



'''
Divide artinya membagi, membagi membagi persoalan menjadi beberapa upa-persoalan yang memiliki kemiripan dengan persoalan semula namun berukuran lebih kecil 
Conquer dalam hal ini berarti menyelesaikan (solve) masing-masing upa-persoalan (secara langsung jika sudah berukuran kecil atau secara rekursif jika masih berukuran besar).
Dengan demikian, algoritma divide and conquer merupakan algoritma rekursif yang memecah masalah menjadi submasalah yang lebih kecil, menyelesaikan submasalah tersebut, dan menggabungkan solusi dari submasalah tersebut untuk memecahkan masalah asal. Algoritma ini sering digunakan dalam berbagai konteks, seperti algoritma pengurutan (misalnya merge sort dan quick sort), algoritma pencarian (misalnya binary search), dan algoritma geometri (misalnya algoritma untuk menghitung jarak terdekat antara titik-titik dalam ruang dua dimensi).
'''