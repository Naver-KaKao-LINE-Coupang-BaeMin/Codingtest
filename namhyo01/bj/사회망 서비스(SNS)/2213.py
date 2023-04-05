import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
populations = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
check = [False for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]
path = [[[],[]] for _ in range(n+1)]
'''
    만약 현재가 우수마을이라면 => 자식은 우수마을이 아니다
    만약 현재가 우수마을이 아니라면 => 자식은 우수마을 일 수도 있고 아닐 수도 있고
'''
def dfs(node):
    check[node] = True
    dp[node][1] += populations[node]
    path[node][1].append(node)
    for i in tree[node]:
        if check[i]: continue
        ret = dfs(i)
        dp[node][1] += dp[i][0]
        dp[node][0] += max(dp[i][1],dp[i][0])
        path[node][1] += ret[0]
        if dp[i][0] > dp[i][1]: # 0이 더크니 0을 추가
            path[node][0] += ret[0]
        else: # 1이 더 크니 1을 추가
            path[node][0] += ret[1] 
    return path[node]
ret = dfs(1)
if dp[1][0] > dp[1][1]:
    print(dp[1][0])
    ret[0].sort()
    print(*ret[0])
else:
    print(dp[1][1])
    ret[1].sort()
    print(*ret[1])
# print(max(dp[1]))
