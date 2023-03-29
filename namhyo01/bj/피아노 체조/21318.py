import sys
input = sys.stdin.readline
n = int(input())
level = [0]+list(map(int, input().split()))
q = int(input())
dp = [0 for _ in range(n+1)]

for i in range(1,n):
    if level[i] > level[i+1]:
        dp[i+1] = dp[i] + 1
    else:
        dp[i+1] = dp[i]

for _ in range(q):
    xx,yy = map(int, input().split())
    print((dp[yy]-dp[xx]))



