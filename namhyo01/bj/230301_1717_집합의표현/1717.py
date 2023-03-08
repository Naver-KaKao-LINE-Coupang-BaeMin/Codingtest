import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int, input().split())
parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])  # 경로 압축
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    ''' 
        작은 값으로 부모 설정
    '''
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    method, a,b = map(int, input().split())
    if method == 0: 
        union_parent(a,b)
    else: 
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')


