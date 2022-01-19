def uniao(A, B):
    if len(A) > len(B):
        tam = len(A)
    else:
        tam = len(B)
    C = set()
    for i in range(tam):
        C.add(A[i])
        C.add(B[i])
    return C

A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
B = [7, 8, 9, 10, 11, 12, 13, 14, 15]

print(uniao(A, B))