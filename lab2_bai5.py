import math

# Vi sao toa do dong nhat 3x3 giup GPU xu ly song song nhanh hon trong Deep Learning:
# - Phep tinh tien (x + tx, y + ty) KHONG phai la anh xa tuyen tinh trong R^2, nen khong
#   bieu dien duoc bang ma tran 2x2. Khi them toa do thu 3 = 1, tinh tien tro thanh phep
#   nhan ma tran 3x3 -> moi bien doi (co gian, xoay, tinh tien) deu la phep nhan ma tran.
# - Nho do co the GOP ca chuoi bien doi thanh 1 ma tran duy nhat M = T * R * S (tinh 1 lan),
#   thay vi ap dung tung buoc len tung diem.
# - Toan bo N diem cua batch anh / bounding box duoc xep thanh ma tran 3 x N, roi chi can
#   1 phep nhan ma tran M (3x3) x P (3xN). GPU co hang nghin nhan toi uu cho phep nhan ma
#   tran (GEMM), xu ly dong thoi moi diem ma khong can re nhanh (if/else) hay vong lap tuan tu.

def mat_mul(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    return [[sum(A[i][k] * B[k][j] for k in range(p)) for j in range(m)] for i in range(n)]


# Tao ma tran affine 3x3: Co gian -> Xoay -> Tinh tien  =>  M = T * R * S
def create_affine_matrix(sx, sy, angle_deg, tx, ty):
    rad = math.radians(angle_deg)
    S = [[sx, 0, 0],
         [0, sy, 0],
         [0, 0, 1]]
    R = [[math.cos(rad), -math.sin(rad), 0],
         [math.sin(rad), math.cos(rad), 0],
         [0, 0, 1]]
    T = [[1, 0, tx],
         [0, 1, ty],
         [0, 0, 1]]
    return mat_mul(T, mat_mul(R, S))


# Chuyen [x, y] -> [x, y, 1], nhan ma tran, tra ve toa do 2D moi
def transform_bounding_box(bbox, affine_matrix):
    result = []
    for x, y in bbox:
        p = [x, y, 1]
        new_p = [sum(affine_matrix[i][j] * p[j] for j in range(3)) for i in range(3)]
        result.append([round(new_p[0] / new_p[2], 2) + 0.0, round(new_p[1] / new_p[2], 2) + 0.0])
    return result


if __name__ == "__main__":
    bbox = [[10, 10], [50, 10], [50, 30], [10, 30]]
    M = create_affine_matrix(sx=1.5, sy=1.5, angle_deg=30, tx=100, ty=50)
    print("Ma tran affine 3x3:")
    for row in M:
        print([round(val, 4) for val in row])
    print(f"Bounding box ban dau: {bbox}")
    print(f"Bounding box moi:     {transform_bounding_box(bbox, M)}")
