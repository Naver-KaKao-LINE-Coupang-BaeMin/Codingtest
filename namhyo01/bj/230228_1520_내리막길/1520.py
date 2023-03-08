import sys
input = sys.stdin.readline

m,n = map(int, input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
maps = []
dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
for _ in range(m):
    maps.append(list(map(int, input().split())))
    
'''
    한번 지나간 곳들은 +1씩 해주고 다음 그곳에 가는애들은 그 횟수만큼 주면 될거같은데?
'''    
def dfs(x,y):
    if dp[y][x] != -1:
        return dp[y][x] # 이미 저장되어있으면 그쪽 가는길은 그 횟수가 지정되있는 것이다. 맞나?
    if x == n-1 and y==m-1:
        return 1 # 횟수 하나 증가 
    dp[y][x] = 0 # 한번이라도 왔으니
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
           if maps[y][x] > maps[ny][nx]:
                dp[y][x] += dfs(nx,ny)
    return dp[y][x]
dfs(0,0)
print(dp[0][0]) # 아 역으로 안했으니 00이 다 쌓이는 곳이군
