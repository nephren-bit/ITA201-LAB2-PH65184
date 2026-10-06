# Tim co so cua Ker(f) va so chieu Nullity qua he thuan nhat A.x = 0
def rref(matrix, eps=1e-9):
    A = [list(map(float, row)) for row in matrix]
    m = len(A)
    n = len(A[0])
    pivot_cols = []
    r = 0
    for c in range(n):
        if r >= m:
            break
        # Chon dong co tri tuyet doi lon nhat lam pivot
        max_row = max(range(r, m), key=lambda i: abs(A[i][c]))
        if abs(A[max_row][c]) < eps:
            continue
        A[r], A[max_row] = A[max_row], A[r]

        # Chuan hoa pivot ve 1
        pivot = A[r][c]
        A[r] = [val / pivot for val in A[r]]

        # Khu cac phan tu khac trong cot pivot
        for i in range(m):
            if i != r and abs(A[i][c]) > eps:
                factor = A[i][c]
                A[i] = [A[i][j] - factor * A[r][j] for j in range(n)]
        pivot_cols.append(c)
        r += 1
    return A, pivot_cols


def find_kernel_basis_2x3(A):
    R, pivot_cols = rref(A)
    n = len(A[0])
    free_cols = [j for j in range(n) if j not in pivot_cols]

    # Moi bien tu do sinh ra 1 vector co so cua Ker(f)
    basis = []
    for free in free_cols:
        x = [0.0] * n
        x[free] = 1.0
        for row_idx, p in enumerate(pivot_cols):
            x[p] = -R[row_idx][free]
        basis.append([round(val, 4) + 0.0 for val in x])

    dim_ker = len(free_cols)  # Nullity = n - rank
    return basis, dim_ker, R


def mat_vec_mul(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]


if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    basis, dim_ker, R = find_kernel_basis_2x3(A)
    print("RREF(A):")
    for row in R:
        print([round(val, 4) + 0.0 for val in row])
    print(f"Co so cua Ker(f): {basis}")
    print(f"dim(Ker) = Nullity = {dim_ker}")
    print(f"Rank = {len(A[0]) - dim_ker}  (Rank + Nullity = {len(A[0])})")
    for v in basis:
        print(f"Kiem tra A.x = {[round(val, 6) + 0.0 for val in mat_vec_mul(A, v)]}")
