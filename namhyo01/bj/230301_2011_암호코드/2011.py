import sys
from string import ascii_lowercase
input = sys.stdin.readline

mod = 1000000
n = list(map(int,input().strip()))
ans = 0
alphabet = {k:idx+1 for idx,k in enumerate(list(ascii_lowercase))}
dp = [0 for _ in range(len(n)+1)]
if n[0] == 0:
    print(ans)
    exit(0)
dp[0] = dp[1] = 1 # 1~9
for i in range(2,len(n)+1):
    '''
        기저조건을 생각해보자
        0부터하면 0 자기 자신만으로는 해결불가
       =>오류

        0이 아니라면 일단 dp[i] = dp[i-1]이 된다
    '''

    if n[i-1] != 0: dp[i] = dp[i-1] # 1~9이니 앞의 결과에서 그대로 이어가면 된다
    num = n[i-2]*10 + n[i-1]
    if 10<=num<=26:
        dp[i] += dp[i-2]
    dp[i] %= mod
print(dp[len(n)] % mod)   

