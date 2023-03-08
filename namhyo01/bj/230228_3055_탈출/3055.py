import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
r,c = map(int, input().split())
maps = [list(input().strip()) for _ in range(r)]
visited = [[False for _ in range(c+1)] for _ in range(r+1)]
dx = [0,0,1,-1] # 이동
dy = [1,-1,0,0] # 이동
pet = deque()
water = deque()
cnt = 0
def water_comes():
    #water_moves = deepcopy(water)
    for i in range(len(water)):
        x,y = water.popleft()
        for j in range(4):
            nx = x+dx[j]
            ny = y+dy[j]
            if 0<=nx<r and 0<=ny<c:
                if not visited[nx][ny] and maps[nx][ny]=='.':
                    visited[nx][ny] = True
                    maps[nx][ny] = '*'
                    water.append([nx,ny])


for i in range(r):
    for j in range(c):
        if maps[i][j] == '*': # 물이라면
            water.append([i,j])
            visited[i][j] = True
        elif maps[i][j] == 'X': #돌이라면
            visited[i][j] = True
        elif maps[i][j] == 'S': # 고슴도치
            pet.append([i,j])
            visited[i][j] = True

            
while pet:
    water_comes() #물이 먼저!
    cnt+=1
    for _ in range(len(pet)):
        x,y = pet.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<r and 0<=ny<c:
                if maps[nx][ny] == 'D': #찾음
                    print(cnt)
                    exit(0)
                if not visited[nx][ny] and maps[nx][ny] == '.':
                    pet.append([nx,ny])
                    visited[nx][ny] = True
print('KAKTUS')
    
    
            
            
            
            
            
            
            
            