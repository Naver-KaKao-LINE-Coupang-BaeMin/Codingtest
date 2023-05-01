import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = sys.maxsize



n,m = map(int, input().split())
'''
    0번째 분기점이 현재 있는 곳
    n-1번째 분기점이 넥서스가 있는곳
    그 외는 전부 중간 거점
    그러나 적 챔피언이나 와드, 미니언, 포탑 등 상대에게 걸리는 곳은 못감
    상대 넥서스까지 갈 수 있는 최소 시간은?
    bfs인가 아니면 다익스트라인가 => 못간다는 것을 생각해보자
    다익스트라가 맞네
'''
A = list(map(int, input().split()))
A[-1] = 0
graph = [[] for _ in range(n+1)]
dis = [INF for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())           
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q = []
    heappush(q,[0,start])
    dis[start] = 0
    while q:
        c, node = heappop(q)
        if dis[node] < c: continue
        for newNode, newC in graph[node]:
            cost = newC + c
            if cost < dis[newNode] and A[newNode] == 0:
                dis[newNode] = cost
                heappush(q,[cost, newNode])
dijkstra(0)
print(dis[n-1] if dis[n-1] != INF else -1)

