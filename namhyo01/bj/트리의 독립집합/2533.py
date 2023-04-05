import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

'''
    현재 노드가 얼리어답터인 경우 => 자식은 그래도 되고 아니어도 되고
    반대로 아니면 => 자식은 무조건 얼리어답터여야 한다
    그럼 dp기준 최소한으로 맞추는 방법은 => ?
    일단 노드 상태는 얼리어답터인 경우/ 아닌 경우 이 두가지 케이스를 다 봐야 한다.
    0이면 아닌거 1이면 맞는거
'''

dp = [[0,1] for _ in range(n+1)] # 무엇을 dp로 둘것인가 현재 노드 상태가 중요하다 
check = [False for _ in range(n+1)]
def dfs(node):
    check[node] = True
    if tree[node]: # 자식이 있다면
        # dp[node][1] += 1 # 자기 자신 증가
        for i in tree[node]:
            if check[i]: continue # 재귀를 어디서 돌려야할까
            dfs(i) # dp 값 갱신
            dp[node][1] += min(dp[i][0],dp[i][1]) # 1이란 얘긴 지금이 얼리어답터 -> 자식은 얼리어답터이어도되고 아니어도되고
            dp[node][0] += dp[i][1]# 반대로 얘는 무조건이다 자식이 무조건 그거여야 한다
    # else:
    #     dp[node][0] = 0 # 얼리어답터가 아니니 횟수를 세지 말자
    #     dp[node][1] = 1 # 역으로 세야한다 1회
dfs(1)
print(min(dp[1][0],dp[1][1]))
