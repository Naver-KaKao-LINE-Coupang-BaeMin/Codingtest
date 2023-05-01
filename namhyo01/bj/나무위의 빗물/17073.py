import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,w = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
'''
    leaf node 개수를 구하라는 문제
'''
check = [False for i in range(n+1)]
check[1] = True
cnt = 0
def dfs(root):
    global cnt, check
    leaf = True
    for n in graph[root]:
        if not check[n]:
            leaf = False
            check[n] = True
            dfs(n)
    if leaf:
        cnt+=1
    
dfs(1)
print(w/cnt)