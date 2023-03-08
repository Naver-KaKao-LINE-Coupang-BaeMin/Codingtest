import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
'''
    문제에선 양방향 그래프이다.
    왔다갔다 하기 위해서는 도시의 도로가 연결되어 있어야 한다 => 유니온 파인드
'''
parent = [i for i in range(0,n+1)]

def find_parent(x):
    if x!=parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)

    if a>b:
        parent[a] = b
    else:
        parent[b] = a


for i in range(1,n+1):
    temp = list(map(int, input().split()))
    for j in range(1,len(temp)+1):
        if temp[j-1] == 1:
            union(i,j)
plan = list(map(int, input().split()))
start = plan[0]
for i in range(1, len(plan)):
    if find_parent(start) == find_parent(plan[i]):
        continue
    else:
        print('NO')
        exit(0)
print('YES')