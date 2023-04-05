import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
maps = []
likes = []
dp = {}
dy = [1,-1,0,0,1,-1,1,-1]
dx = [0,0,1,-1,1,1,-1,-1]
for _ in range(n):
    maps.append(input().strip())
for _ in range(k):
    s = input().strip()
    likes.append(s)
    dp[s] = 0 # 숫자세기 몇번인지
def dfs(y,x,string):
    if len(string) > 5:
        return
    if string in likes:
        dp[string] += 1
    for i in range(8):
        ny = y+dy[i]
        nx = x+dx[i]
        if ny < 0:
            ny = n-1
        if nx < 0:
            nx = m-1
        if ny >= n:
            ny = 0
        if nx >= m:
            nx = 0
        dfs(ny,nx,string+maps[ny][nx])
for i in range(n):
    for j in range(m):
        dfs(i,j,maps[i][j])
for i in likes:
    print(dp[i])
