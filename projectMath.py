
def matrixMultiplication(A, B, modulo):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        return
    else:
        output = [[0 for row in range(colsB)] for col in range(rowsA)]
        for i in range(rowsA):
            for j in range(colsB):
                for k in range(colsA):
                    output[i][j] += A[i][k] * B[k][j]
                    output[i][j] %= modulo
        return output

def matrixDeterminant(A, modulo):
    size = len(A)
    det = 0
    if size == 2:
        det = A[0][0] * A[1][1] - A[0][1]*A[1][0]
        det %= modulo
    else:
        for i in range(size):
            temp = 1
            for j in range(size):
                temp *= A[(i+j) % size][j]
                temp %= modulo
            det += temp
        det %= modulo
        for i in range(size - 1, -1 , -1):
            temp = 1
            for j in range(size):
                temp *= A[(i-j) % size][j]
                temp %= modulo
            det -= temp
        det %= modulo
    return det

def matrixTransposition(A):
    output = [[0 for row in range(len(A))] for col in range(len(A[0]))]
    for i in range(len(output[0])):
        for j in range(len(output)):
            output[j][i] = A[i][j]
    return output

def matrixMultiplicationByConst(A, const, modulo):
    for i in range(len(A)):
        for j in range(len(A)):
            A[i][j] *= const
            A[i][j] %= modulo

def matrixOfComplements(A, modulo):
    output = [[0 for row in range(len(A))] for col in range(len(A))]
    for i in range(len(output)):
        for j in range(len(output)):
            tempMatrix = [[0 for row in range(len(output) - 1)] for col in range(len(output) - 1)]
            tempI = 0
            for k in range(len(A)):
                if k == i:
                    continue
                else:
                    tempJ = 0
                    for l in range(len(A)):
                        if l == j:
                            continue
                        else:
                            tempMatrix[tempI][tempJ] = A[k][l]
                            tempJ += 1
                tempI += 1
            output[i][j] = matrixDeterminant(tempMatrix, modulo)
            if (i + j) % 2 != 0:
                output[i][j] *= -1
                output[i][j] %= modulo
    return output

def inversionModulo(number, modulo):
    for i in range(1, modulo):
        if (i * number) % modulo == 1:
            return i

def matrixInversion(matrix, modulo):
    output = matrixOfComplements(matrix, modulo)
    # print("Macierz dopelnien alg")
    # print(output)
    output = matrixTransposition(output)
    # print("Macierz dopelnien alg transponowana")
    # print(output)
    detMatrix = matrixDeterminant(matrix, modulo)
    # print("Wyznacznik " + str(detMatrix))
    invDetMatrix = inversionModulo(detMatrix, modulo)
    # print("Odwrotnosc Wyznacznika " + str(detMatrix))
    matrixMultiplicationByConst(output, invDetMatrix, modulo)
    return output