import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[False for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
dfsList = []
bfsList = []

visited = [False for _ in range(n+1)]
def dfs(node):
    dfsList.append(node)
    visited[node] = True
    for i in range(1,n+1):
        if graph[node][i] and not visited[i]:
            dfs(i)
def bfs(node):
    '''
        deque =>
        <================//xxxxxxxx
    '''
    bfsList.append(node)
    queue = deque([node])
    visited[node] = True
    while queue:
        nn = queue.popleft()
        for i in range(1,n+1):
            if graph[nn][i] and not visited[i]:
                visited[i] = True
                queue.append(i)
                bfsList.append(i)

def bfs2(node):
    visited[node] = True
    bfsList.append(node)
    queue = [node]
    while True:
        nextq = []
        for q in queue:
            for i in range(1,n+1):
                if graph[q][i] and not visited[i]:
                    visited[i] = True
                    nextq.append(i)
                    bfsList.append(i)
        if not nextq:
            break
        queue = nextq