import sys
input = sys.stdin.readline

n,m = map(int, input().split())
maps = []
ans = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
checked = [[False for _ in range(m+1)] for _ in range(n+1)]
for _ in range(n):
    maps.append(list(map(int, input().split())))

'''
    테트로미노를 설정해야겠다. => 어떻게?
    일단 모양별로 나눠보자
    xxxx
    x
    x
    x
    x
    xx
    xx
    x
    x
    xx
    xx
     x
     x
'''

def dfs(i,j,cnt,sum):
    ans = 0
    if cnt == 3:
        return sum
    
    checked[i][j] = True
    for k in range(4):
        x = j + dx[k]
        y = i + dy[k]
        if 0<=x<m and 0<=y<n and not checked[y][x]:
            checked[y][x] = True
            ans = max(dfs(y,x, cnt+1, sum+maps[y][x]),ans)
            checked[y][x] = False
    checked[i][j] = False
    return ans

def firstshape(i,j): # ㅜ
    if i+1<n and 1<=j<m-1:
        return maps[i][j] + maps[i][j-1] + maps[i][j+1] + maps[i+1][j]
    return 0

def secondshape(i,j): # ㅏ
    if 1<=i<n-1 and j+1<m:
        return maps[i][j] + maps[i][j+1] + maps[i-1][j] + maps[i+1][j]
    return 0

def thirdshape(i,j): # ㅗ
    if i-1>=0 and 1<=j<m-1:
        return maps[i][j] + maps[i][j-1] + maps[i][j+1] + maps[i-1][j]
    return 0

def fourthshape(i,j): # ㅓ
    if j-1>=0 and 1<=i<n-1:
        return maps[i][j] + maps[i][j-1] + maps[i+1][j] + maps[i-1][j]
    return 0

def woo(i,j):
    return max(firstshape(i,j),secondshape(i,j),thirdshape(i,j),fourthshape(i,j))

for i in range(n):
    for j in range(m):
        ans = max(dfs(i,j,0,maps[i][j]),ans,woo(i,j))

print(ans)