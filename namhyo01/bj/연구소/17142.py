import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

n,m = map(int, input().split())
maps = []
virus = [] # 바이러스 존재들
dy = [0,0,1,-1]
dx = [1,-1,0,0]

maps_cnt = 0


def check(map):
    for i in map:
        for j in i:
            if j==0:
                return False
    return True

def bfs(viruses,map):
    queue = deque([])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    for y,x in viruses:
        queue.append([y,x])
        visited[y][x] = 0  # 시간 체크용
    ret = 0
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<n and 0<=nx<n and visited[ny][nx]==-1:
                if map[ny][nx] == 0:
                    map[ny][nx] = 2
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append([ny,nx])
                    ret = max(ret,visited[ny][nx])         
                if map[ny][nx] == 2: # 바이러스가 활성화되는거니 시간 체크x
                    queue.append([ny,nx]) 
                    visited[ny][nx] = visited[y][x] + 1
    if check(map):
        return ret
    else:
        return float('inf')

for _ in range(n):
    maps.append(list(map(int,input().split())))
for i in range(len(maps)):
    for j in range(len(maps[i])):
        if maps[i][j] == 2:
            virus.append([i,j])
'''
    10C5가 최대일듯 => 109876/54321 => 84 가능할듯
'''
ans = float('inf')
for chose in combinations(virus,m):
    map = deepcopy(maps)
    ans = min(ans,bfs(chose,map))
print(-1 if ans == float('inf') else ans)