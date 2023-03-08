import sys
input = sys.stdin.readline
n,m = map(int, input().split())
maps = [list(input().strip()) for _ in range(n)]
ans = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer_list = []
stars = [[False for _ in range(m)] for _ in range(n)]

def solve(x,y):
    for k in range(1,m+1):
        for i in range(4):
            nx = x + dx[i] * k
            ny = y + dy[i] * k
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == '*':
                pass
            else:
                return
        stars[x][y] = False
        answer_list.append([x+1,y+1,k])
        for i in range(4):
            nx = x + dx[i] * k
            ny = y + dy[i] * k
            stars[nx][ny] = False
        

def make_cross(x,y):
    return solve(x,y)

for i in range(n):
    for j in range(m):
        if maps[i][j] == '*':
            stars[i][j] = True

for i in range(0,n):
    for j in range(0,m):
        if(maps[i][j] == '*'):
            make_cross(i,j)
            
for i in stars:
    for j in i:
        if j:
            print(-1)
            exit(0)
            
print(len(answer_list))
for x,y,cnt in answer_list:
    print(x,y,cnt, sep=' ')


