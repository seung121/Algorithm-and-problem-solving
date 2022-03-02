import sys
n = 31
d = [16, 10, 5, 1]
k = 4
C = [sys.maxsize for i in range(n)]      # 값 초기화
C[0] = 0

for j in range(0, n):
    for i in range(1, k):
        if (d[i] <= j) and (C[j - d[i]] + 1 < C[j]):
            C[j] = C[j - d[i]] + 1

print(C[n-1])
