import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,r,q = map(int, input().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

'''
    dfs로 돌면서 예를 들어 5로 시작시 5->4->3->1->2이렇게 갈테니 4로 시작한다 쳐도 4->3->1->2일 것이다
    그러니 dfs로 돌면서 이 과정들을 저장하면 될 것같다.
'''
dp = [-1 for _ in range(n+1)]
check = [False for _ in range(n+1)]
def dfs(node):
    if dp[node] != -1: return dp[node] # dp값이 존재하면
    check[node] = True
    dp[node] = 1 # 하난 있는거니(자기자신)
    for i in tree[node]:
        if check[i]: continue
        dp[node] += dfs(i)
    return dp[node]

dfs(r)

# 여기서 바로 처리
for _ in range(q):
    print(dp[int(input())])
