import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]
'''
    최소일수 => bfs
'''

m,n,h = map(int, input().split())
maps = [[[-3 for _ in range(h)]for _ in range(m)]for _ in range(n)]
rotten = deque([])
apples = 0
new_apple = 0
for k in range(h):
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(len(temp)):
            maps[i][j][k] = temp[j]
            if temp[j] == 1:
                rotten.append([i,j,k,0])
                new_apple += 1
            if temp[j] != -1:
                apples+=1
if apples == new_apple:
    print(0)
    exit(0)
while rotten:
    i,j,k,day = rotten.popleft()
    for a in range(6):
        ni = i + dx[a]
        nj = j + dy[a]
        nk = k + dz[a]
        if 0<=ni<n and 0<=nj<m and 0<=nk<h and maps[ni][nj][nk]==0:
            maps[ni][nj][nk]= maps[i][j][k] + 1
            rotten.append([ni,nj,nk,day+1])
day = 0
for i in maps:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
            day = max(day,k) 
print(day-1)


    