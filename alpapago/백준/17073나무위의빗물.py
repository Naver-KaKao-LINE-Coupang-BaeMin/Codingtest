import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, w = map(int,input().split())

adj = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

# queue
visited = [False]*(n+1)

cnt = 0

def dfs(v):
    global cnt
    visited[v] = True

    flag = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)
            flag = False

    if flag:
        cnt+=1

    return cnt

print(w/dfs(1))
