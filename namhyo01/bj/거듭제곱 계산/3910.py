import sys
from copy import deepcopy
input = sys.stdin.readline

t = int(input())

min_cnt = float('inf')
# def solve(ret, cnt, num,op):
#     global min_cnt
#     if ret == num:
#         min_cnt = min(min_cnt, cnt)
#         return
#     '''
#         제곱
#         그냥 곱
#         나누기
#     '''
#     # # 한번이라도 탐색한 수는 더 이상 탐색 x
#     if num > 2 * ret:
#         return
#     if check[num] <= cnt:
#         return
#     check[num] = cnt
#     op.append(num)
#     if ret > num:
#         for i in op:
#             solve(ret, cnt+1, num+i,op)
#     if num >=1:
#         solve(ret,cnt+1,num-1, op)

def bfs(ret, cnt, num):
    cq = [[num,cnt,[]]]
    check = [False for _ in range(20000)]
    if ret == num:
        return cnt
    check[1] = True
    while True:
        nq = []
        for n,c,op in cq:
            oo = deepcopy(op)
            oo.append(n)
            if n == ret:
                print(oo)
                return c
            for i in oo:
                if not check[n+i]:
                    check[n+i] = True
                    nq.append([n+i, c+1,oo])
                if n-i > 0 and not check[n-i]:
                    check[n-i] = True
                    nq.append([n-i, c+1,oo])
        if not nq:
            break
        cq = nq


for _ in range(t):
    ret = int(input())
    min_cnt = float('inf')
    # solve(ret,0,1,[])
    print(bfs(ret,0,1))

'''
    dfs => dfs푸셨어요
    => 한쪽으로 쭉 간다 ~~ 모든 케이스를 탐색한다
    스택 => 재귀로 구현

    bfs => 큐로 구현
    python기준 두개의 리스트로도 해결 가능!
    => 최단 시간을 뽑기 가능
'''
