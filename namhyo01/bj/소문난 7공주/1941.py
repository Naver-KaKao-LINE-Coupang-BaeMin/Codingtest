import sys
input = sys.stdin.readline

maps = [list(input().strip()) for _ in range(5)]

ans = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

arr = []

def bfs(arr):
    check = [[True for _ in range(5)]for _ in range(5)]
    for y,x in arr:
        check[y][x] = False
    cq = [arr[0]]
    check[arr[0][0]][arr[0][1]] = True
    check_visit = 1
    while True:
        nq = []
        for y,x in cq:
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]
                if 0<=ny<5 and 0<=nx<5 and not check[ny][nx]:
                    check[ny][nx] = True
                    check_visit += 1
                    nq.append((ny,nx))
        if not nq: break
        cq = nq
    if check_visit == 7:
        return True
    else: return False
                    

def dfs(x,depth,cnt):
    global ans
    if cnt >= 4: return
    if depth == 7 and bfs(arr):
        ans+=1
        return
    for i in range(x, 25):
        r = i//5
        c = i%5
        arr.append((r,c))
        dfs(i+1, depth+1, cnt+1 if maps[r][c] == 'Y' else cnt)
        arr.pop()


dfs(0,0,0)
print(ans)