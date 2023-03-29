import sys
input = sys.stdin.readline

n,k = map(int, input().split())
'''
    bfs같은데 최단 거리라고 하니 음..
'''
cq = [[n,0]]
MAX = 100001
check = [False for _ in range(MAX+1)]
time = 0
check[n] = True
while True:
    nq = []
    for i,t in cq:
        check[i] = True
        if i==k:
            print(t)
            exit(0)
        if i*2 <= MAX and not check[i*2]:
            nq.append([i*2,t])
            check[i*2] = True
        if i-1 >= 0 and not check[i-1]:
            nq.append([i-1,t+1])
            check[i-1] = True
        if i+1 <= MAX and not check[i+1]:
            nq.append([i+1,t+1])
            check[i+1] = True
    if not nq:
        break
    cq = nq
    print(cq)