from random import randint as ra
n = int(input('Введите порядок матрицы: '))
mat = [[ra(-30, 30) for i in range(n)] for j in range(n)]
mn = 10**10
minsum = 0

for x in mat:
    if min(x) < mn:
        minsum, mn = sum(x), min(x)

#

minproz = [10**10, 0]
matt = [[mat[i][j] for i in range(n)] for j in range(n)]

for x in matt:
    if all(abs(i) < 11 for i in x):
        p = 1
        for i in x:
            p *= i
        if minproz[0] > p:
            minproz[0], minproz[1] = p, matt.index(x)

matt[minproz[1]], matt[minproz[1] - 1] = matt[minproz[1] - 1], matt[minproz[1]]

mat = [[matt[n-i-1][j] for i in range(n)] for j in range(n)]

print(minsum, *mat, sep='\n')
