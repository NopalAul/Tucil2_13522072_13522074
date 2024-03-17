import numpy as np
import matplotlib.pyplot as plt

def bezier_n_divide_and_conquer(points, iterations):
    def generate_control_points(points):
        control_points = []
        for i in range(len(points) - 1):
            print((points[i] + points[i + 1]) / 2)
            control_points.append((points[i] + points[i + 1]) / 2)
        # make the midpoint for control_points if the length of points is more than 1
        if len(control_points) > 1:
            recursive_control_points = generate_control_points(control_points)
            control_points.extend(recursive_control_points)
            # control_points = generate_control_points(control_points)
        print(f'control_points: {control_points}')
        return control_points
    
    # def generate_control_points(points):
    #     control_points = []
    #     for i in range(len(points) - 1):
    #         print((points[i] + points[i + 1]) / 2)
    #         control_points.append((points[i] + points[i + 1]) / 2)
    #     # make the midpoint for control_points if the length of points is more than 1
    #     if len(control_points) > 1:
    #         recursive_control_points = generate_control_points(control_points)
    #         control_points.extend(recursive_control_points)
    #         # control_points = generate_control_points(control_points)
    #     print(f'control_points: {control_points}')
    #     return control_points

    def divide_and_conquer(points, iterations):
        if iterations == 0:
            return [points[0], points[-1]]

        control_points = generate_control_points(points)
        # new_points = [points[0]]
        # for i in range(len(control_points)):
        #     new_points.append(control_points[i])
        # new_points.append(points[-1])

        left_points = divide_and_conquer(points[:len(control_points) // 2 + 1], iterations - 1)
        right_points = divide_and_conquer(points[len(control_points) // 2:], iterations - 1)

        return left_points[:-1] + right_points

    return divide_and_conquer(points, iterations)

# Contoh penggunaan
points = np.array([[0, 0], [1.5, 4], [4, 0]])
# points = np.array([[0, 0], [1.5, 4], [4, 0], [5,3]])
iterations = 1
result = bezier_n_divide_and_conquer(points, iterations)
print("Titik pada kurva Bezier:", result)
