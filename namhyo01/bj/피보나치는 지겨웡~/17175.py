import sys
input = sys.stdin.readline

n = int(input())
mod = 1000000007

dp = [0 for _ in range(51)]
dp[1] = 1
dp[0] = 1
# dp[2] = 3
# dp[3] = 5
def fibonacci(n):
    if dp[n] != 0: return dp[n]
    if n < 2:
        return dp[n]
    dp[n] = 1 # 자기 자신 count
    dp[n] = (dp[n]+(fibonacci(n-1) + fibonacci(n-2))) % mod
    return dp[n] % mod
print(fibonacci(n))


