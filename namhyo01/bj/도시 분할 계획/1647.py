import sys
input = sys.stdin.readline

n,m = map(int, input().split())
edge = []

for _ in range(m):
    a,b,c = map(int, input().split())
    edge.append((a,b,c))

edge.sort(key=lambda x: x[2])
parent = [i for i  in range(n+1)]

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
minus = 0
for a,b,c in edge:
    if find(a) != find(b):
        union(a,b)
        ans += c
        minus = c
print(ans-minus)