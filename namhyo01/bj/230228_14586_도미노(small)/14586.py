import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
# ㅁㅊ 고려대 문제구나 ㅇㅅㅇ..
n = int(input())
dominos = []
dp = [[-1 for _ in range(n+1)] for _ in range(n+1)] # 0 : 왼쪽, 1 : 오른쪽
for _ in range(n):
    dominos.append(list(map(int, input().split())))
dominos.sort() # 순서대로 오게 정렬
x_list = [i[0] for i in dominos]
h_list = [i[1] for i in dominos]

leftdp = [-1 for _ in range(n+1)]
rightdp = [-1 for _ in range(n+1)]
inf = 2000000001


# for i in range(n):
#     start_point, height = dominos[i]
#     left_end_point = start_point - height
#     right_end_point = start_point + height
#     for j in range(i, -1, -1):
#         if left_end_point <= dominos[j][0]:
#             left_end_point = min(left_end_point, dominos[j][0] - dominos[j][1])
#             leftdp[i] = min(leftdp[i], j)
#     for j in range(i + 1, n):
#         if right_end_point >= dominos[j][0]:
#             right_end_point = max(right_end_point, dominos[j][0] + dominos[j][1])
#             rightdp[i] = max(rightdp[i], j)


def left(cur):

    if leftdp[cur] != -1:
        return leftdp[cur]
    x,h = dominos[cur][0], dominos[cur][1]
    move = x-h
    temp = bisect_left(x_list,move)
    leftdp[cur] = temp
    for i in range(temp,cur): # 자신이 밀쳐내는 것 들 중에서 더 멀리 밀쳐내면 그 값으로 갱신한다
        leftdp[cur] = min(leftdp[cur], left(i))

    return leftdp[cur]

def right(cur):
    if rightdp[cur] != -1:
        return rightdp[cur]
    x,h = dominos[cur][0], dominos[cur][1]
    move = x+h
    temp = bisect_right(x_list,move)

    rightdp[cur] = temp-1
    for i in range(cur,temp): # 자신이 밀쳐내는 것 들 중에서 더 멀리 밀쳐내면 그 값으로 갱신한다
        rightdp[cur] = max(rightdp[cur], right(i))
    return rightdp[cur]

for i in range(n):
    left(i)
    right(i)

def solve(start,end):
    if dp[start][end] != -1:
        return dp[start][end]
    # 기저조건이 뭐가 있을까 생각이 안난다
    if start>end:
        dp[start][end] = 0
        return 0

    if rightdp[start]>=end or leftdp[end]<=start:
        dp[start][end] = 1
        return dp[start][end]
    
    dp[start][end] = float('inf')
    for i in range(start,end+1):
        dp[start][end] = min(dp[start][end], solve(start,leftdp[i]-1)+solve(leftdp[i],rightdp[i])+solve(rightdp[i]+1,end))
    return dp[start][end]


def solve2(n):
    dp2 = [ float('inf') for _ in range(n+1) ]
    dp2[0] = 1
    for i in range(1,n):
        if leftdp[i] <= 0:
            dp2[i] = min(dp2[i],1)
        else:
            dp2[i] = min(dp2[i],dp2[leftdp[i]-1]+1)
        for j in range(i):
            if rightdp[j] >= i:
                if j==0:
                    dp2[i] = min(dp2[i],1)
                else:
                    dp2[i] = min(dp2[i],dp2[j-1]+1)
    print(dp2[n-1])


def solve3(n):
        # dp[i] -> 0 ~ i까지 넘어뜨리는 데 필요한 최소 횟수
    dp = [float('inf') for i in range(n)]
    # 0~0번째 도미노를 넘어뜨리는 데 필요한 최소 개수는 1개 
    dp[0] = 1

    for i in range(n):
        if left[i] - 1 < 0:
            dp[i] = min(dp[i], 1)
        else:
            # i번째 도미노를 왼쪽으로 무너뜨렸을 때 left[i]번째까지 한방에 무너지므로, 
            # 0 ~ i번째 도미노까지 무너뜨리는 데 필요한 최소 횟수는 0 ~ left[i] - 1까지 넘어뜨리는 데 필요한 최소 횟수 + 1
            dp[i] = min(dp[i], dp[left[i] - 1] + 1)

        # 왼쪽으로 넘어뜨렸을 때의 최솟값을 전부 고려했다면 이번에는 오른쪽으로 넘어뜨렸을 때의 상황을 고려해야함
        # 만약 i보다 왼쪽에 있는 j번째 도미노를 오른쪽으로 넘어뜨렸을 때, i번째 도미노가 같이 넘어진다면, dp[i] = min(dp[i], dp[j - 1] + 1)로 볼 수 있음 
        # 이는 앞서 i보다 왼쪽에 있는 dp들이 모두 제대로 업데이트 됐기 때문에 가능한 검증임
        for j in range(i):
            if right[j] >= i:
                if j == 0:
                    dp[i] = min(dp[i], 1)
                else:
                    dp[i] = min(dp[i], dp[j - 1] + 1) 
                    
    print(dp[n - 1])

# print(solve(0,n-1))
solve2(n)
    
    