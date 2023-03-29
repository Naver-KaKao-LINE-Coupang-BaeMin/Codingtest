import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m = map(int,input().split())
nemo = [[False for _ in range(26)]for _ in range(26)]
ans = 0
def solve(y,x):
    '''
        문제의 조건
        네모칸을 만들지 못하게 해야한다...
        한칸 한칸 네모에 두고 전진하자 일단
    '''
    global ans
    nx,ny = x,y
    if y > n:
        ans += 1
        return
    if x == m: # x가 행의 끝에 도착했으면 더이상 가지 않는다
        nx = 1
        ny += 1
    else: # 거꾸로
        nx += 1
    # 이렇게 한칸씩 증가시켜가면서 테스트를 하자
    solve(ny,nx)  # 그냥 지나 가기
    if not nemo[y-1][x] or not nemo[y-1][x-1] or not nemo[y][x-1]:
        nemo[y][x] = True # 배치
        solve(ny,nx)
        nemo[y][x] = False # 다시 해제
    
solve(1,1)
print(ans)