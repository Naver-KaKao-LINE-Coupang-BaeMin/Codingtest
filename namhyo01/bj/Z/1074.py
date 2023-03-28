import sys
input = sys.stdin.readline
n,r,c = map(int, input().split())
answer = 0
def solve(y,x,size):
    global answer
    '''
        4분할로 나누자
        + 기준으로
        ㅁㅁㅁㅁ
        ㅁㅁxㅁ
        ㅁㅁㅁㅁ
        ㅁㅁㅁㅁ
    '''
    if y == r and x == c:
        print(answer)
        return
    if r < y+size and c < x+size and r >= y and c >= x: # 이러면 r과 c가 현재 자른 것 안에 있다는 얘기
        solve(y, x, size//2)
        solve(y, x+size//2, size//2)
        solve(y+size//2, x, size//2)
        solve(y+size//2, x+size//2, size//2)
    else:
        answer += size**2
    '''
        횟수를 세야한다
        어떻게?
        r행 c열보다 전에 있는 애들은 횟수를 세야한다
        횟수는?
        그 자른 애들의 사이즈 만큼이 된다
    '''
solve(0,0,2**n)
