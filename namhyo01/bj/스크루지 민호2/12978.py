import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
dp = [[0,1] for _ in range(n+1)] # 경찰서를 세우지 않는 경우, 세우는 경우

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]

def dfs(node):
    global visited

    for n in graph[node]:
        if not visited[n]:
            visited[n] = True
            dfs(n)
            # 경찰서를 세운다면 근처는 있어도 되고 없어도 된다
            dp[node][1] += min(dp[n][0],dp[n][1])
            dp[node][0] += dp[n][1] # 얜 무조건 있어야 한다
visited[1] = True
dfs(1)
print(min(dp[1]))
