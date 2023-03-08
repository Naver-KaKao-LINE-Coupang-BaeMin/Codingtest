import sys
input = sys.stdin.readline
n,m = map(int, input().split())
maps = [list(input().strip()) for _ in range(n)]
checked = [[0 for _ in range(m)] for _ in range(n)]
move = {
    'S':(0,1),
    'E':(1,0),
    'N':(0,-1),
    'W':(-1,0)
}
''''
3 4
SWWW
SEWN
EEEN

EWW 

'''
ans = 0
def solve1():
    def dfs(y,x,cnt):
        if checked[y][x]:
            return checked[y][x]
        if not checked[y][x]:
            checked[y][x] = cnt
            dx,dy = move[maps[y][x]][0],move[maps[y][x]][1]
            ny = y+dy
            nx = x+dx
            checked[y][x] = dfs(ny,nx,cnt) # 값 갱신 => 사이클을 찾은거니
            return checked[y][x]
    ans = 0
    for i in range(n):
        for j in range(m):
            if not checked[i][j]:
                ans = max(dfs(i,j,ans+1),ans)

    print(ans)
solve1()