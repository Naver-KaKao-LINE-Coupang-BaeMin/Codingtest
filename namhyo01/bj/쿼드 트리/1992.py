import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
maps = []
one_count = 0
zero_count = 0
def check(s,num):
    if s=='1'*num:
        return 1
    if s=='0'*num:
        return 0
    return 2
for _ in range(n):
    s = input().strip()
    maps.append([i for i in s])

'''
    문제는 또 반씩 잘라봐야 한다.
    그러기 위해서는 이걸 찾는 함수를 하나 더 만들자
'''
# print(''.join(maps[0][:6]))
def solve(toy,tox,fromy, fromx):
    now = maps[toy][tox]
    ans = ''
    for y in range(toy, fromy+1):
        for x in range(tox, fromx+1):
            if maps[y][x] != now: # 다르다는 얘기는 무엇이냐 => 나눠야한다 사분할
                ans += '('
                ans += solve(toy, tox,(fromy+toy)//2, (fromx+tox)//2) # 1사분면
                ans += solve(toy, (tox+fromx)//2+1, (fromy+toy)//2, fromx) # 2사분면
                ans += solve((fromy+toy)//2+1, tox, fromy, (fromx+tox)//2) # 3사분면
                ans += solve((fromy+toy)//2+1, (fromx+tox)//2+1, fromy, fromx) # 4사분면
                ans += ')'
                return ans
    return str(now)
print(solve(0,0,n-1,n-1))