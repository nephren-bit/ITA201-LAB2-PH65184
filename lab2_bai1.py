# Tinh to hop tuyen tinh v = c1*b1 + c2*b2 + ... theo co so B
def compute_linear_combination(B, c):
    dim = len(B[0])
    v = [0.0] * dim
    for i in range(len(B)):
        for j in range(dim):
            v[j] += c[i] * B[i][j]
    return v


if __name__ == "__main__":
    B = [
        [1, 0],  # b1
        [1, 1]   # b2
    ]
    c = [-2, 7]
    print(f"Vector ket qua v: {compute_linear_combination(B, c)}")
