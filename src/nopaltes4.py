import numpy as np
import matplotlib.pyplot as plt

# def bezier_n_divide_and_conquer(points, iterations):
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


def divide_and_conquer(points, iterations):
    if iterations == 0:
        return [points[0], points[-1]]

    control_points = generate_control_points(points)
    

    # mid point
    mid_point = control_points[-1]
    print(f'mid_point: {mid_point}')

    # left points
    array_left_points = []
    array_left_points.append(points[0]) # P0
    array_left_points.append(control_points[0]) # Q0

    len_points = len(points) # 4
    i = len_points-1 # 3
    while i < len(control_points): #  3 < 6
        array_left_points.append(control_points[i]) # controlpoints[3] R0 
        len_points -= 1 # 4 - 1 = 3
        i += len_points-1 # 3 + (3 - 1) = 5

    print(f'left_points: {array_left_points}')
    
    # right points
    array_right_points = []
    control_points.reverse()
    print(f'control points reverse: {control_points}')
    array_right_points.append(control_points[0]) # S
    array_right_points.append(control_points[1]) # R1

    start_index = 3
    i = start_index # 3
    while i < len(control_points): # 6 < 10
        array_right_points.append(control_points[i]) # controlpoints[3] Q2  
        i += start_index # 6 + 4 = 10
        start_index += 1 # 5
    
    array_right_points.append(points[-1]) # P3

    print(f'right_points: {array_right_points}')


    left_points = divide_and_conquer(array_left_points, iterations - 1)
    right_points = divide_and_conquer(array_right_points, iterations - 1)

    return left_points[:-1] + [mid_point] +  right_points

    # return divide_and_conquer(points, iterations)

# Contoh penggunaan
points = np.array([[0, 0], [1.5, 4], [4, 0]])
# points = np.array([[0, 0], [1.5, 4], [4, 0], [5,3]])
iterations = 1
result = divide_and_conquer(points, iterations)
print(f'hasil: {result}')