import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
maps = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = {}
checked = [[1,2,3],[4,5,6],[7,8,0]]
for _ in range(3):
    maps.append(list(map(int, input().split()))) # 퍼즐 설정
x = y = 0
flag = False
for i in range(3):
    for j in range(3):
        if maps[i][j] == 0:
            x,y = j,i
            flag = True
            break
    if flag:
        break

def check(m):
    if checked == m:
        return True
    return False


def bfs(x,y,maps):
    map = deepcopy(maps)
    queue = deque([])
    queue.append([x,y,map,0])
    while queue:
        x,y,m,cnt = queue.popleft()
        if check(m):
            return cnt
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<3 and 0<=ny<3:
                nm = deepcopy(m)
                nm[y][x],nm[ny][nx] = nm[ny][nx],0
                if not visited.get(str(nm),False):
                    visited[str(nm)] = True
                    queue.append([nx,ny,nm,cnt+1])
    return -1


visited[str(maps)] = True
print(bfs(x,y,maps))

