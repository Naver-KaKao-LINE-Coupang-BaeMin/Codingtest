import sys
input = sys.stdin.readline

c, n = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [0]+[sys.maxsize for _ in range(c+100)]
for cc, cus in cost:
    for i in range(cus, c+101):
        dp[i] = min(dp[i], dp[i-cus]+cc)
print(min(dp[c:]))


