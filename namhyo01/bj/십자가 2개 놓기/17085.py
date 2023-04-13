import sys
from copy import deepcopy
input = sys.stdin.readline

n,m = map(int, input().split())
maps = [list(input().strip()) for _ in range(n)]
answer = 0

able = []

def findMaxSize(y,x):
    start = 0
    ans = []
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    while True:
        flag = False
        for i in range(4):
            ny = dy[i]*start + y 
            nx = dx[i]*start + x
            if not (0<=ny <n and 0<=nx<m and maps[ny][nx] == '#'):
                flag = True
        if flag: return ans
        ans.append((y,x,start))
        start += 1

def checkArea(y,x,size,y2,x2,size2):
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    checks = []
    for j in range(size+1):
        for i in range(4):
            ny = y+dy[i]*j
            nx = x+dx[i]*j
            checks.append([ny,nx])
    for j in range(size2+1):
        for i in range(4):
            ny = y2+dy[i]*j
            nx = x2+dx[i]*j
            if [ny,nx] in checks:
                return False
    return True

for i in range(n):
    for j in range(m):
        if maps[i][j] == '#':
            able.extend(findMaxSize(i,j))
for y,x,size in able:
    for y2,x2,size2 in able:
        if y==y2 and x==x2: continue
        area = (1+size*4) * (1+size2*4)
        if area > answer and checkArea(y,x,size,y2,x2,size2):
            answer = area
print(answer)



# def check(y,x,map):
#     dy = [1,0,-1,0]
#     dx = [0,1,0,-1]
#     for i in range(4):
#         ny = y+dy[i]
#         nx = x+dx[i]
#         if 0<=ny<n and 0<=nx<m:
#             if map[ny][nx] == '1':
#                 return False
#     return True

# def isable(y,x,map, num):
#     start = 1
#     dy = [1,0,-1,0]
#     dx = [0,1,0,-1]
#     map[y][x] = num
#     ans = 0
#     while True:
#         for i in range(4):
#             ny = dy[i]*start + y 
#             nx = dx[i]*start + x
#             if not (0<=ny <n and 0<=nx<m and map[ny][nx] == '#'):
#                 return ans, map
#         for i in range(4): map[y+dy[i]*start][x+dx[i]*start] = num
#         ans += 4
#         start += 1

# for i in range(n):
#     for j in range(m):
#         temp = deepcopy(maps)
#         if maps[i][j] == '#':
#             size, nm = isable(i,j,temp,'1')
#             for k in range(n):
#                 for l in range(m):
#                     nnm = deepcopy(nm)
#                     if nm[k][l] == '#':
#                         ns,tt = isable(k,l,nnm,'2')
#                         answer = max((size+1)*(ns+1), answer)
# print(answer)
'''
    6 8
    ...#..#..
    ...#..#..
    .########
    ...#..#..
    ...#..#..

'''