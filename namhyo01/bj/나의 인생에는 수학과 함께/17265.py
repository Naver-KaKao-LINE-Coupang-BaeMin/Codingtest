import sys
input = sys.stdin.readline

n = int(input())
maps = [input().split() for _ in range(n)]
op = ['+','-','*']
min_ans = sys.maxsize
max_ans = -sys.maxsize
dy = [1,0]
dx = [0,1]

def calculate(a,b,ops):
    if ops == '+':
        return a+b
    elif ops=='*':
        return a*b
    else:
        return a-b
def dfs(y,x,calc,ops):
    global min_ans, max_ans
    if y == n-1 and x == n-1:
        min_ans = min(calc, min_ans)
        max_ans = max(calc, max_ans)
        return
    for i in range(2):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<n and 0<=nx<n:
            if maps[ny][nx] in op: # 수식 연산이면
                dfs(ny,nx,calc,maps[ny][nx])
            else:
                dfs(ny,nx,calculate(calc,int(maps[ny][nx]),ops),'')
                
        
dfs(0,0,int(maps[0][0]),'')
print(max_ans, min_ans)