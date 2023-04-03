import sys
input = sys.stdin.readline
n = int(input())
w = []
edge = []
for i in range(n):
    edge.append((n,i,int(input())))
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        edge.append((i,j,temp[j]))
edge.sort(key=lambda x: x[2])
parent = [i for i in range(n+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[max(x,y)] = min(x,y)
ans = 0
for i,j,c in edge:
    if find(i) != find(j):
        ans += c
        union(i,j)
print(ans)