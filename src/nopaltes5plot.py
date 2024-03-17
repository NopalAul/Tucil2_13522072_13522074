import numpy as np
import matplotlib.pyplot as plt

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

# Contoh penggunaan
# points = np.array([[0, 0], [1.5, 4], [4, 0]])
points = np.array([[0, 0], [1.5, 4], [4, 0], [5,3]])
iterations = 3
result = divide_and_conquer(points, iterations)

# Visualisasi plot kurva
result = np.array(result)
plt.plot(result[:, 0], result[:, 1], '-o', label='Bezier Curve')
plt.scatter(points[:, 0], points[:, 1], color='red', label='Control Points')
plt.title('Bezier Curve with Control Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
