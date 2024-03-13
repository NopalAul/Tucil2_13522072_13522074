import numpy as np
import matplotlib.pyplot as plt

def bezier_quadratic_brute_force(P0, P1, P2, iterations):
    # Membuat array untuk menyimpan titik-titik pada kurva
    points = []

    # Iterasi melalui berbagai nilai parameter t
    for t in np.linspace(0, 1, iterations):
        # Hitung titik pada kurva menggunakan rumus kurva Bezier
        B_t = (1 - t)**2 * P0 + 2 * (1 - t) * t * P1 + t**2 * P2
        # Tambahkan titik ke dalam array
        points.append(B_t)

    return points

def plot_bezier_curve(P0, P1, P2, iterations):
    # Menghasilkan kurva Bezier kuadratik menggunakan algoritma brute force
    points = bezier_quadratic_brute_force(P0, P1, P2, iterations)

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
iterations = 5

plot_bezier_curve(P0, P1, P2, iterations)
