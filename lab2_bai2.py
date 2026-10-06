# Kiem tra 2 vector 2D co phu thuoc tuyen tinh (cung phuong) hay khong
def is_linearly_dependent_2d(v1, v2):
    det = v1[0] * v2[1] - v1[1] * v2[0]
    if abs(det) < 1e-9:
        return True
    return False


if __name__ == "__main__":
    print(is_linearly_dependent_2d([2, 4], [4, 8]))  # True  -> phu thuoc
    print(is_linearly_dependent_2d([2, 4], [1, 5]))  # False -> doc lap
