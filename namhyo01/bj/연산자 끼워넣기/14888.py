import sys
from copy import deepcopy
input = sys.stdin.readline
inf = 10000000000

n = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
max_ans = -inf
min_ans = inf

def div(a,b):
    if a<0:
        a *= -1
        return -(a//b)
    return a//b

def solve(num,ops,idx):
    operator = deepcopy(ops)
    global max_ans
    global min_ans
    if idx == n:
        max_ans = max(max_ans, num)
        min_ans = min(min_ans,num)
        return

    # 더하기
    if ops[0] > 0:
        operator[0]-=1
        solve(num+A[idx],operator,idx+1)
        operator[0]+=1
    # 빼기
    if ops[1] > 0:
        operator[1]-=1
        solve(num-A[idx],operator,idx+1)
        operator[1]+=1
    # 곱하기
    if ops[2] > 0:
        operator[2]-=1
        solve(num*A[idx],operator,idx+1)
        operator[2]+=1
    # 나누기
    if ops[3] > 0:
        operator[3]-=1
        solve(div(num,A[idx]),operator,idx+1)
        operator[3]+=1
solve(A[0],op,1)
print(max_ans)
print(min_ans)