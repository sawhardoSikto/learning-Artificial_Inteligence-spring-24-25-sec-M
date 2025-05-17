def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            num = float(input(f"Enter number for [{i+1}][{j+1}]: "))
            row.append(num)
        matrix.append(row)
    return matrix

def multiply(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(B)):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        result.append(row)
    return result


print("Matrix Multiplication")
print("--------------------")


print("\nFirst Matrix:")
rows1 = int(input("Enter rows: "))
cols1 = int(input("Enter columns: "))
print("Enter numbers for first matrix:")
A = input_matrix(rows1, cols1)


print("\nSecond Matrix:")
rows2 = int(input("Enter rows: "))

cols2 = int(input("Enter columns: "))
print("Enter numbers for second matrix:")
B = input_matrix(rows2, cols2)


if cols1 != rows2:
    print("\nError: Cannot multiply! Columns of first matrix must equal rows of second matrix")
else:
    
    result = multiply(A, B)
    print("\nResult:")
    for row in result:
        print(row)