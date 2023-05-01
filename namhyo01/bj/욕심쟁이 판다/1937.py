import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
dy = [1,-1,0,0]
dx = [0,0,1,-1]
dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
'''
    더 많은 대나무가 있는 대로만 이동
'''
maps = [list(map(int, input().split())) for _ in range(n)]

def dfs(y,x):
    if dp[y][x] != -1: return dp[y][x]
    dp[y][x] = 1
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<n and 0<=nx<n and maps[y][x] < maps[ny][nx]:
            dp[y][x] = max(dp[y][x], dfs(ny,nx)+1)
    return dp[y][x]
ans = 0

for i in range(n):
    for j in range(n):
        ans = max(ans,dfs(i,j))


print(ans)