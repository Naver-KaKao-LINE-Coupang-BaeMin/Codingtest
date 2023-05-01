import sys
from heapq import heappush, heappop
input = sys.stdin.readline


INF = sys.maxsize
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
dis = [INF for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q = []
    heappush(q,[0,start]) # 다익스트라
    dis[start] = 0
    while q:
        c, node = heappop(q)
        if dis[node] < c: continue
        for newNode, newC in graph[node]:
            cost = c + newC
            if cost < dis[newNode]:
                dis[newNode] = cost
                heappush(q,[cost, newNode])

dijkstra(1)
print(dis[n])