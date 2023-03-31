import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
def find(x):
    if x!=parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x!=y:
        parent[max(x,y)] = min(x,y)

for _ in range(m):
    op,a,b = map(int,input().split())
    if op==0:
        union(a,b)
    else:
        print('YES' if find(a)==find(b) else 'NO')