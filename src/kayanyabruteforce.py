import numpy as np
import matplotlib.pyplot as plt

def de_casteljau(points, t):
    # Basis case: jika hanya satu titik tersisa, kembalikan titik tersebut
    if len(points) == 1:
        return points[0]

    # Lakukan interpolasi linear antara semua pasangan titik berurutan
    new_points = []
    for i in range(len(points) - 1):
        new_points.append((1 - t) * points[i] + t * points[i + 1])

    # Rekursi pada submasalah dengan titik-titik baru
    return de_casteljau(new_points, t)

def bezier_curve_divide_and_conquer(points, iterations):
    # Array untuk menyimpan titik-titik pada kurva Bezier
    curve_points = []

    # Iterasi melalui berbagai nilai parameter t
    for t in np.linspace(0, 1, iterations):
        # Hitung titik pada kurva menggunakan algoritma divide and conquer
        curve_point = de_casteljau(points, t)
        curve_points.append(curve_point)

    return curve_points

# Contoh penggunaan
points = np.array([[0, 0], [2, 5], [5, 3], [7, 8], [10, 15]])  # Contoh dengan 5 titik
iterations = 10  # Jumlah iterasi

# Membuat kurva Bezier
curve_points = bezier_curve_divide_and_conquer(points, iterations)

# Memisahkan koordinat x dan y
x = [point[0] for point in curve_points]
y = [point[1] for point in curve_points]

# Plot kurva Bezier
plt.plot(x, y, marker='o', linestyle='-')

# Plot titik kontrol
plt.scatter([point[0] for point in points], [point[1] for point in points], color='red')

# Menambahkan label
plt.title('Bezier Curve')
plt.xlabel('X')
plt.ylabel('Y')

# Menampilkan plot
plt.grid(True)
plt.show()