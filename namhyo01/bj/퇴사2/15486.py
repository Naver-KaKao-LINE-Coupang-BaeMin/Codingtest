import sys
input = sys.stdin.readline

n = int(input())
work = []
for _ in range(n):
    work.append(list(map(int, input().split())))
dp = [0 for _ in range(n+1)]
for i in range(1,n+1):
    dp[i] = max(dp[i], dp[i-1]) # 그 전날까지 잡혀있는 것중에서 최대값으로 선택해주자
    day = i+work[i-1][0] - 1 # 오늘 날도 포함
    if day > n: continue # 오바면 패스
    dp[day] = max(dp[day], dp[i-1] + work[i-1][1])
print(max(dp))
