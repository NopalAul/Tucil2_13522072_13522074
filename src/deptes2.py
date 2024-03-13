import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

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
