import math


# Ap dung ma tran 2x2 len tung diem 2D
def apply_matrix(points, M):
    result = []
    for x, y in points:
        new_x = M[0][0] * x + M[0][1] * y
        new_y = M[1][0] * x + M[1][1] * y
        result.append([round(new_x, 2) + 0.0, round(new_y, 2) + 0.0])
    return result


# Co gian: S = [[sx, 0], [0, sy]]
def scale_points(points, sx, sy):
    S = [[sx, 0], [0, sy]]
    return apply_matrix(points, S)


# Xoay quanh goc toa do: R = [[cos, -sin], [sin, cos]]
def rotate_points(points, angle_degrees):
    rad = math.radians(angle_degrees)
    R = [[math.cos(rad), -math.sin(rad)],
         [math.sin(rad), math.cos(rad)]]
    return apply_matrix(points, R)


if __name__ == "__main__":
    square = [[0, 0], [2, 0], [2, 2], [0, 2]]
    print(f"Diem ban dau:      {square}")
    print(f"Co gian (2, 0.5):  {scale_points(square, 2, 0.5)}")
    print(f"Xoay 90 do:        {rotate_points(square, 90)}")
    print(f"Xoay 45 do:        {rotate_points(square, 45)}")
