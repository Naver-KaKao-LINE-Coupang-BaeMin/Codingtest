import sys
input = sys.stdin.readline

n,l,r = map(int, input().split())
dy = [0,0,1,-1]
dx = [1,-1,0,0]
'''
    땅이 n*n
    각 땅에 나라 1개
    인구이동 방법
    1. 국경선을 공유시 두 나라 인구 차이가 >=l <=r이면 국경선을 연다
    2. 위 조건에 의해 열어야 하는 국경선이 모두 열리면 인구 이동
    3. 인접한 칸만을 이용해 이동가능하면 연합이라 한다.
    4. 연합을 이루는 각 칸의 인구수 연합의 인구수/연합을 이루는 칸의 개수 (소수점은 버린다)
    5. 연합을 해체, 국경선 닫는다.
'''
maps = []
checked = [[False for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    maps.append(list(map(int, input().split())))
def bfs(y,x,num):
    global visited
    queue = [[y,x]]
    country = [[y,x]]
    while True:
        nqueue = []
        for y,x in queue:
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]
                if 0<=ny<n and 0<=nx<n:
                    if visited[ny][nx]==0 and l<=abs(maps[y][x]-maps[ny][nx])<=r:
                        visited[ny][nx] = num
                        nqueue.append([ny,nx])
                        country.append([ny,nx])
        if not nqueue:
            break
        queue = nqueue
    return country

def checkGroup(num):
    group_sum = 0
    group_cnt = 0
    group = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == num:
                group.append([i,j])
                group_cnt += 1
                group_sum += maps[i][j]
    group_avg = group_sum//group_cnt
    for y,x in group:
        maps[y][x] = group_avg

day = 0
while True:
    minus_maps = []
    num = 1
    flag = False
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                visited[i][j] = num
                country = bfs(i,j,num)
                num+=1
                if len(country) > 1:
                    flag = True
                    group_sum = sum([maps[y1][x1] for y1,x1 in country]) // len(country)
                    for y,x in country:
                        maps[y][x] = group_sum
    if not flag: # 기저조건
        break
    # 연합검사
    # break
    # for i in range(1,num):
    #     checkGroup(i)
    day += 1
print(day)
