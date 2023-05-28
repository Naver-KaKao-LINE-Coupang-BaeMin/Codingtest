import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,d = map(int, input().split())
    graph[a].append([b,d])
    graph[b].append([a,d])
visited = [False for _ in range(n+1)]
visited[r] = True
stump = branch = 0
flag = False
def dfs(node, st, br):
    global stump, branch, flag
    branch = max(branch,br) # => 매번 br을 갱신
    stump = max(stump,st) # => 매번 가지 갱신
    
    if not flag and len(graph[node]) > 2 - int(node == r):
        flag = True # => 기가노드이니깐 가지의 길이를 구하자
    if not flag:
        if graph[node]:
            for nn, cost in graph[node]:
                if not visited[nn]:
                    visited[nn] = True
                    dfs(nn, st + cost, br) # 기둥의 길이를 더하자
    else: # 기둥은끝, 가지길이 체크
        for nn, cost in graph[node]:
            if not visited[nn]:
                visited[nn] = True
                dfs(nn,st,br+cost) # 가지길이를 더하자
        
dfs(r,0,0)
print(stump,branch)