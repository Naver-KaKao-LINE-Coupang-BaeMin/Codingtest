import sys
from itertools import permutations
input = sys.stdin.readline

k,m = map(int,input().split())
'''
0~9까지 k가지의 숫자를 한번씩만 이용
1. 서로다른 두개의 소수의 합으로 나타낼 수 있느 ㄴ경우
M으로 나누어 떨어지지 않을때까지 나눈 수가 두개의 소수의 곱인 경우
'''

check = [False for _ in range(10)]
possible = []
def dfs(num,cnt):
    if cnt == k:
        possible.append(int(num))
        return
    for i in range(10):
        if num == '' and i ==0: continue
        if not check[i]:
            check[i] = True
            dfs(num+str(i),cnt+1)
            check[i] = False
# dfs('',0)
MAX = 98765 // 10**(5-k)
# 일단 최대 범위까지 소수 리스트 만들어 놓음
check = [0] * (MAX + 1)
yesPrime = set()   # 있는지 체크하기에는 set 자료형이 최고
for i in range(2, MAX+1):
    if check[i] == 0:
        check[i] = 1
        yesPrime.add(i)  # 1부터 N까지 소수 리스트
        for j in range(i+i,MAX+1,i):
            check[j] = 1
        

ans = 0
# for num in possible:
for num in permutations(range(10),k):
    if num[0] == 0: continue
    num = int(''.join(list(map(str,num))))
    temp = num
    while temp % m == 0:    # m으로 나누어떨어지지 않을 때까지 나눠줌
        temp //= m
    for i in range(2, int(temp**0.5)+1):  
        if temp % i == 0:   # 한 번이라도 소수와 소수가 아닌 수가 있어도 반례이므로 break 해줌
            if i in yesPrime and temp//i in yesPrime: # 2조건
                for j in range(2,num//2):
                    if j in yesPrime and num-j in yesPrime:
                        ans += 1
                        break
            # break  
                    
print(ans)