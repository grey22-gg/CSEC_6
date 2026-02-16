matrix = []

for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

x = 1

for i in range(5):         
    for j in range(5):      
        if matrix[i][j] == x:
            y = i
            z = j
a =abs(2-y)
b = abs(2-z)
c = a+b
print(c)
