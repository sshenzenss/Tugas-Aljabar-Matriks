def kofaktor_matriks(A):
    n = len(A)
    kof = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            minor = []
            for x in range(n):
                if x == i:
                    continue
                row = []
                for y in range(n):
                    if y == j:
                        continue
                    row.append(A[x][y])
                minor.append(row)
            
            det_minor = minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
            kof[i][j] = ((-1) ** (i+j)) * det_minor
    return kof

def adjoin(A):
    n = len(A)
    adj = [[0 for _ in range(n)] for _ in range(n)]

    kof = kofaktor_matriks(A)

    for i in range(n):
        for j in range(n):
            adj[j][i] = kof[i][j]
    return adj
