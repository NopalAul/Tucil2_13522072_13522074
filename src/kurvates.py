import numpy as np
import matplotlib.pyplot as plt

def bezier_quadratic(P0, P1, P2, iterations):
    if iterations == 0:
        return [P0, P1, P2]
    
    # Menemukan titik kontrol tengah
    Q0 = (P0 + P1) / 2
    Q1 = (P1 + P2) / 2
    R = (Q0 + Q1) / 2
    
    # Rekursi pada submasalah
    left_points = bezier_quadratic(P0, Q0, R, iterations - 1)
    right_points = bezier_quadratic(R, Q1, P2, iterations - 1)
    
    # Menggabungkan hasil dari kedua submasalah
    return left_points[:-1] + right_points

def plot_bezier_curve(P0, P1, P2, iterations):
    # Menghasilkan kurva Bezier kuadratik
    points = bezier_quadratic(P0, P1, P2, iterations)
    
    # Memisahkan koordinat x dan y
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    
    # Plot kurva Bezier
    plt.plot(x, y, marker='o', linestyle='-')
    
    # Plot titik kontrol
    plt.scatter([P0[0], P1[0], P2[0]], [P0[1], P1[1], P2[1]], color='red')
    
    # Menambahkan label
    plt.title('Bezier Curve')
    plt.xlabel('X')
    plt.ylabel('Y')
    
    # Menampilkan plot
    plt.grid(True)
    plt.show()

# Contoh penggunaan
P0 = np.array([0, 0])
P1 = np.array([1.5, 4])
P2 = np.array([4, 0])
iterations = 2

plot_bezier_curve(P0, P1, P2, iterations)
