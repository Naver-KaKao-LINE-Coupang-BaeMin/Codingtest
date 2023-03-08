import sys

input = sys.stdin.readline
t = int(input())
param = []
graph = [[-1 for _ in range(1001)] for _ in range(1001)]
check = []
def dfs(i):
    check[i] = True
    if not check[graph[i][0]]:
        dfs(graph[i][0])
        
for _ in range(t):
    n = int(input())
    param = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    check = [False for _ in range(n+1)]
    ans = 0
    for idx, p in enumerate(param):
        graph[idx+1] += [p]
    for i in range(1,n+1):
        if not check[i]:
            dfs(i)
            ans+=1
    print(ans)