import sys
from string import ascii_lowercase, ascii_uppercase
import heapq
input = sys.stdin.readline

'''
    지금 위치에서 인접한 정수 좌표 중 높이 차가 T보다 크지 않은 곳만 간다 => 작거나 같다
    높이가 낮은 곳이나 같으면 1초, 크면 높이 차의 제곱만큼
'''
n,m,t,d = map(int, input().split())
alphabet = {i:w for w,i in enumerate(ascii_uppercase)}
for w,i in enumerate(ascii_lowercase,start=26):
    alphabet[i] = w
map = [input().strip() for _ in range(n)]
dy = [1,-1,0,0]
dx = [0,0,1,-1]
inf = float('inf')


def dijkstra(startx,starty):
    ''' 
        두개로 가능한가? 시작 노드가? => dp를 노드 하나가 아닌 두개의 좌표로 dp => times
    '''
    times = [[inf for _ in range(m)] for _ in range(n)]
    times[starty][startx] = 0
    q = []
    heapq.heappush(q,[0, startx, starty])
    while q:
        ct, x, y = heapq.heappop(q)
        height = alphabet[map[y][x]] # 현재 높이
        if times[y][x] < ct:
            continue
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            nt = ct
            if 0<=nx<m and 0<=ny<n:# 범위 해당되는가
                nheight = alphabet[map[ny][nx]]
                if abs(nheight-height) <= t: # t이하인가(높이 차가)
                    # 이제 계산 시작
                    if nheight <= height:
                        nt += 1
                    else:
                        nt += (nheight-height)**2
                    if times[ny][nx] > nt:
                        times[ny][nx] = nt
                        heapq.heappush(q,[nt,nx,ny])
    return times
times = dijkstra(0,0) # 0,0에서 출발해서 어디까지 가는 그 시간 겟
# 이게 d이하인 것들로 다익스트라를 돌자
reverse = []
for i in range(n):
    for j in range(m):
        if times[i][j] <= d:
            heapq.heappush(reverse,[-alphabet[map[i][j]],j,i])
'''
    이제 reverse에서 하나씩 빼가면서 역으로 시간을 체크해보자
    아 이게 플로이드가 더 쉬웠네 
'''
ans = []
while reverse:
    ct,x,y = heapq.heappop(reverse)
    new_times = dijkstra(x,y)
    if new_times[0][0] + times[y][x] <= d:
        print(alphabet[map[y][x]])
        break