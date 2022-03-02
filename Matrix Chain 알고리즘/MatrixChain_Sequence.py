import sys

d = [10, 20, 5, 15, 30]
n = len(d)
C = [[0 for col in range(n)] for row in range(n)]
S = 0


def sequence(s):
    if s == 0:
        print("곱셈 순서는 A*(B*C*D)가 이상적입니다.")
    elif s == 1:
        print("곱셈 순서는 (A*B)*(C*D)가 이상적입니다.")
    elif s == 2:
        print("곱셈 순서는 (A*B*C)*D가 이상적입니다.")

for L in range(1, n):
    for i in range(1, n - L):
        j = i + L
        C[i][j] = sys.maxsize
        for k in range(i, j):
            temp = C[i][k] + C[k + 1][j] + (d[i - 1] * d[k] * d[j])
            if temp < C[i][j]:
                S = k
                C[i][j] = temp

print("최소 곱셈 횟수 :", C[1][n - 1])
sequence(S)