import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
dis = [-1 for _ in range(n+1)]
dis[1] = 0 # 루트노드이니
def dfs(root, w):
    for node, weight in graph[root]: # 자식 노드들을 돌면서
        if dis[node] == -1: # 갱신이 된적이 없다면
            dis[node] = weight + w # 부모랑 자기자신 cost합
            dfs(node,dis[node])
dfs(1,0)
n1 = dis.index(max(dis)) # 하나 최대 길이 노드 뽑음 => 이거 기준 하나 더 뽑자
dis = [-1 for _ in range(n+1)]
dis[n1] = 0
dfs(n1, 0)
print(max(dis))