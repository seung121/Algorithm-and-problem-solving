v = [10, 40, 30, 50]
wt = [5, 4, 6, 3]
C = 10
n = len(v)

K = [[0 for x in range(C + 1)] for x in range(n + 1)]

for i in range(n + 1):
    for w in range(C + 1):
        if i == 0 or w == 0:
            K[i][w] == 0
        elif wt[i - 1] <= w:
            K[i][w] = max(v[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
        else:
            K[i][w] = K[i - 1][w]

print(K[n][C])
