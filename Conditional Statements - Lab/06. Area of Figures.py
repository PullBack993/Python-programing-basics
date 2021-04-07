import math
type = input()


if type == "square":
    square_side = float(input())
    square_area = square_side * square_side
    print(f"{square_area:.3f}")
elif type == "rectangle":
    width = float(input())
    length = float(input())

    rectangle_area = width * length
    print(f'{rectangle_area:.3f}')
elif type == "circle":
    r = float(input())
    circle_area = math.pi * r * r
    print(f'{circle_area:.3f}')
elif type == "triangle":
    triangle_side = float(input())
    triangle_width = float(input())
    triangle_area = (triangle_side * triangle_width) / 2
    print(f'{triangle_area:.3f}')
