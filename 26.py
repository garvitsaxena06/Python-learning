#to take a matrix by user
matrix = []
m = int(input("Enter m: "))
n = int(input("Enter n: "))
print("Enter matrix m x n: ")
for i in range(m):
    arr = []
    for j in range(n):
        arr.append(int(input()))
    matrix.append(arr)
print(matrix)
