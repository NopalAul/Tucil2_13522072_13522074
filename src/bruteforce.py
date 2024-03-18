import numpy as np
import matplotlib.pyplot as plt
from time import process_time

#################### ALGORITMA ####################
def bezier_linear(points, t):
    # Basis case: jika hanya satu titik tersisa, kembalikan titik tersebut
    if len(points) == 1:
        return points[0]

    # Lakukan interpolasi linear antara semua pasangan titik berurutan (kurva Bézier linier)
    new_points = []
    for i in range(len(points) - 1):
        new_points.append((1 - t) * points[i] + t * points[i + 1])

    # Rekursi dengan titik-titik baru
    return bezier_linear(new_points, t)

def bezier_curve_brute_force(points, iterations):
    # Kalkulasi titik dari iterasi yang diberikan
    # Dari ekivalensi parameter iteration pada Divide and Conquer
    n_point = (2 ** iterations) + 1

    print("ALGORITMA BRUTE FORCE")
    print(f'Jumlah iterasi  : {iterations} (ekivalensi iterasi DnC)')
    print(f'Jumlah titik    : {n_point}')

    # Array untuk menyimpan titik-titik pada kurva Bezier
    curve_points = []

    # Iterasi parameter t sesuai jumlah titik
    for t in np.linspace(0, 1, n_point):
        curve_point = bezier_linear(points, t)
        curve_points.append(curve_point)

    return curve_points

# input titik dan iterasi 
points_input = input("Masukkan titik-titik kontrol (pisahkan dengan spasi, misal: 0,0 1.5,4 4,0 5,-3): ")
points = np.array([[float(coord) for coord in point.split(',')] for point in points_input.split()])
iterations = int(input("Masukkan jumlah iterasi: "))
print()

# Start time
start = process_time()
# Membuat kurva Bezier
curve_points = bezier_curve_brute_force(points, iterations)
# End time
end = process_time()
timer = round(end - start, 2) * 1000
print(f'Waktu eksekusi  : {timer} ms')


#################### PLOT KURVA ####################
# Memisahkan koordinat x dan y
x = [point[0] for point in curve_points]
y = [point[1] for point in curve_points]

# Plot kurva Bezier
plt.plot(x, y, marker='o', linestyle='-')

# Plot titik kontrol
plt.scatter([point[0] for point in points], [point[1] for point in points], color='red')

# Label nama
plt.title('Bezier Curve')
plt.xlabel('X')
plt.ylabel('Y')

# Menampilkan plot
plt.grid(True)
plt.show()