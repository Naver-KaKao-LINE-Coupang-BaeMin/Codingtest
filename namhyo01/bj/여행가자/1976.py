import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[max(x,y)] = min(x,y)

for i in range(1,n+1):
    data = [0]+list(map(int,input().split()))
    for j in range(1, n+1):
        if data[j] == 1:
            union(i,j)
plan = list(map(int,input().split()))
s = plan[0]
for p in plan:
    if find(s) != find(p):
        print('NO')
        exit(0)
print('YES')
