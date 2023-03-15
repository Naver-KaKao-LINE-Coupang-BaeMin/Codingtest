import sys

input = sys.stdin.readline
N, M = map(int, input().split())

region = [[0] * M]
for _ in range(N):
    region.append([0] + list(map(int, input().split())))
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + region[i][j]

K = int(input())
for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    popul = 0
    print(dp[y2][x2] - dp[y1 - 1][x2] - dp[y2][x1 - 1] + dp[y1 - 1][x1 - 1])
