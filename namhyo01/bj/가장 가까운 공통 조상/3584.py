import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    # graph = [[] for _ in range(n+1)]
    parent = [i for i in range(n+1)]
    check = [False for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int, input().split())
        parent[b] = a # b노드의 부모는 a이다
        # graph[a].append(b)
    a,b = map(int, input().split())
    check[a] = True # a에서 시작해 bottom - top으로 이동
    while True:
        if parent[a] == a: break
        a = parent[a] # 부모로 거슬러 올라가보자
        check[a] = True
    '''
        여기까지하면 부모들이 a로 변경 되어 있을 것이다.
    '''
    # 반대로 5도 시작해서 check가 True이면...? 그게 최대 깊이일거시앋
    while True:
        if check[b]: 
            print(b)
            break
        b = parent[b]
