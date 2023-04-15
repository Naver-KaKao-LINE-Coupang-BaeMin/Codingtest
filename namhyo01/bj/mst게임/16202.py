import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int, input().split())
edges = []
parent = [i for i in range(n+1)]
def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]
def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        parent[max(a,b)] = min(a,b)

for i in range(1,m+1):
    a,b = map(int, input().split())
    edges.append([i,a,b])
edges.sort()
edges = deque(edges)
ans = []
flag = False
for i in range(k):
    parent = [i for i in range(n+1)]
    if flag: 
        ans.append(0)
        continue
    temp = []
    for edge in edges:
        c,a,b = edge
        if find(a) != find(b):
            union(a,b)
            temp.append(c)
    if len(temp) == n-1: ans.append(sum(temp))
    else: 
        flag = True
        ans.append(0)
    edges.popleft()
    print(edges)
print(*ans, sep=' ')


