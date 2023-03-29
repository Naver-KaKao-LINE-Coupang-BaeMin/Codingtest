import sys
from collections import defaultdict
input = sys.stdin.readline
n,k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
'''
    부분합이라...
    수가 증가하는 것도 아님
    => 다 찾아야하나?
    200000^2 => 아닌듯
    일단 돌자 => a를 돌자
    => 만약에 k랑 같으면 1을 더하자
    => 일단 값 애들을 그 딕셔너리로 넣자
'''
dp = defaultdict(list)
sum = 0
dp[0] = 1 # 누적은 0부터 시작한다 0 + A
for i in a:#a를 돌면서
    sum+=i # 누적합
    cnt += dp.get(sum-k,0)
    # dp갱신을 뭐로할까
    dp[sum] = dp.get(sum,0)+1
print(cnt)
# for i in range(n-1,-1,-1):
#     t = a[i] # 현재 값
#     if t == k:
#         cnt += 1
#     '''
#         cnt를 증가 시키는 방법이 현재 값과 다른 값이 더 있나를 보면된다
#     '''
#     cnt += dp[t-k]
#     dp[t].append(i) # i번째 인덱스는 t라는 키값에 저장
