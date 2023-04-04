import sys
input = sys.stdin.readline

v,e = map(int, input().split())
road = []
for _ in range(e):
    a,b,c = map(int, input().split())
    road.append((a,b,c))
road.sort(key=lambda x:x[2])
parent = [i for i  in range(v+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    x = find(x)
    y = find(y)
    if x!=y:
        parent[max(x,y)] = min(x,y)
ans = 0
for a,b,c in road:
    if find(parent[a]) != find(parent[b]):
        union(a,b)
        ans += c
print(ans)