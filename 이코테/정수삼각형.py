import collections
import sys

a = int(input())
b = []
for _ in range(a):
    b.append(list(map(int,sys.stdin.readline().split())))
memo = [[-1] * (i + 1) for i in range(a)]

memo[0][0] = b[0][0]

def tri(r, c):
    if not (0 <= r < a and 0 <= c < len(b[r])):
        return 0

    if memo[r][c] != -1:
        return memo[r][c]

    memo[r][c] = max(tri(r - 1, c - 1), tri(r - 1, c)) + b[r][c]
    return memo[r][c]


for col in range(a):
    tri(a - 1, col)
print(max(memo[a - 1]))
