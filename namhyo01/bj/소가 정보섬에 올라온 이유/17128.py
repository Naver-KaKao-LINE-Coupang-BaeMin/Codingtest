import sys
input = sys.stdin.readline

n,q = map(int, input().split())
A = list(map(int, input().split()))
Q = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
for i in range(n):
    dp[i] = A[i] * A[i-1] * A[i-2] * A[i-3]
'''
    dp[0] => A[1][8][7][6]
    dp[1] => A[2][1][8][7] .... => 그렇다는 것은 
    만약 q=3이라면 2,3,4,5를 포함할 것이다.
'''
prefix_sum = sum(dp)
for q in Q:
    for i in range(4):
        include_idx = (q-1+i) % n # 원형이니
        dp[include_idx] *= -1
        prefix_sum += 2*dp[include_idx]
    print(prefix_sum)
    # print(sum(dp))이렇게하면 시간초과가 뜬다 => 누적합 개념 사용하자