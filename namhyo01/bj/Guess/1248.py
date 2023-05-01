import sys
input = sys.stdin.readline

n = int(input())
string = list(input())

maps = [[0 for _ in range(n)] for _ in range(n)]
a = [] # 정답 배열 => 담을 배열들
idx = 0

for i in range(n):
    for j in range(i, n):
        if string[idx] == '+':
            maps[i][j] = 1
        elif string[idx] == '-':
            maps[i][j] = -1
        idx += 1

# print(maps)
def check(idx):
    sum = 0
    for i in range(idx,-1,-1):
        sum += a[i] # a[i]를 더해가자
        if sum == 0 and maps[i][idx] != 0:
            return False
        if sum < 0 and maps[i][idx] >= 0:
            return False
        if sum > 0 and maps[i][idx] <= 0:
            return False
    return True

'''
    최악의 케이스여도 21 ** 10 정도 될듯하다
    10000000000
    S[1][1] = - a[1] = -
'''
def solve(idx): # 원소 하나씩 넣어보면서 체크해보자
    if idx == n: # 기저조건
        print(*a)
        exit(0)
    for i in range(1,11): # 범위가 -10 ~ 10이니 
        a.append(i * maps[idx][idx]) # i 추가
        if check(idx):
            solve(idx+1)
        a.pop() # 제거
        
solve(0)