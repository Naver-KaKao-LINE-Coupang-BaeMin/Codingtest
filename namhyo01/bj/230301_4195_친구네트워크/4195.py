import sys
input = sys.stdin.readline
t = int(input())
friends = []
parent = {}



def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y: # 부모가 달라지면
        parent[y] = x
        friends[x] += friends[y]

for _ in range(t):
    f = int(input())
    parent = {}
    friends = {}
    for _ in range(f):
        x,y = input().split()
        if x not in parent:
            parent[x] = x
            friends[x] = 1
        if y not in parent:
            parent[y] = y
            friends[y] = 1
        union(x,y)
        print(friends[find(x)])