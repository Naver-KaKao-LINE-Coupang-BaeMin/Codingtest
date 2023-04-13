import sys
input = sys.stdin.readline


maps = []
attacks = [] # 가장 최근 공격 시간
n,m,k = map(int, input().split())
for _ in range(n):
    maps.append(list(map(int, input().split())))
    attacks.append([0 for _ in range(m)])
'''

    4가지 액션을 k번 반복
    만약 부서지지 않은 포탑이 1개가 되면 즉시 중지
    n,m이 10이하이면 그냥 싹다 돌려도될거같다
'''

def chooseWeakness():
    min_attack = float('inf')
    min_r = min_c = -1
    for i in range(n):
        for j in range(m):
            if maps[i][j] <= 0: continue
            if maps[i][j] < min_attack:
                min_attack = maps[i][j]
                min_r,min_c = i,j
            elif maps[i][j]==min_attack: # 같으면
                if attacks[i][j] > attacks[min_r][min_c]:
                    min_r,min_c = i,j
                elif attacks[i][j] == attacks[min_r][min_c]:
                    if min_r+min_c < i+j:
                        min_r, min_c = i,j
                    elif min_r + min_c == i+j and min_c < j:
                        min_r = i
                        min_c = j
    return min_r, min_c

def attack(y,x): # y,x는 제외
    max_attack = 0
    min_r = min_c = -1
    for i in range(n):
        for j in range(m):
            if maps[i][j] <= 0: continue
            if i == y and j == x: continue
            if maps[i][j] > max_attack:
                max_attack = maps[i][j]
                min_r,min_c = i,j
            elif maps[i][j] == max_attack: # 같으면
                if attacks[i][j] < attacks[min_r][min_c]:
                    min_r,min_c = i,j
                elif attacks[i][j] == attacks[min_r][min_c]:
                    if min_r+min_c > i+j:
                        min_r, min_c = i,j
                    elif min_r + min_c == i+j and min_c > j:
                        min_r = i
                        min_c = j
    return min_r, min_c

def laiser(y,x,y1,x1):
    cq = [[y,x,[[y,x]]]]
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    check = [[False for _ in range(m)] for _ in range(n)]
    check[y][x] = True
    while True:
        nq = []
        for i,j, path in cq:
            if i==y1 and j==x1:
                return path
            for l in range(4):
                ni = i+dy[l]
                nj = j+dx[l]
                if ni < 0:
                    ni = n-1
                if ni >= n:
                    ni = 0 
                if nj < 0:
                    nj = m-1
                if nj >= m:
                    nj = 0
                if not check[ni][nj] and maps[ni][nj] != 0:
                    check[ni][nj] = True
                    nq.append([ni,nj,path+[[ni,nj]]])
        if not nq:
            break
        cq = nq
    return []

def attackLaiser(path,damage,y1,x1):
    global maps
    for i in range(1, len(path)-1):
        y,x = path[i][0], path[i][1] 
        maps[y][x] = maps[y][x] - (damage//2) if (maps[y][x] - (damage//2)) >= 0 else 0
    maps[y1][x1] = maps[y1][x1] - damage if (maps[y1][x1] - damage) >= 0 else 0

def potan(sty,stx,y,x):
    global maps
    path = [[sty,stx],[y,x]]
    dy = [1,-1,0,0,1,1,-1,-1]
    dx = [0,0,1,-1,1,-1,1,-1]
    damage = maps[sty][stx]
    for i in range(8):
        ny = dy[i] + y
        nx = dx[i] + x
        if ny < 0: ny = n-1
        if ny >= n: ny = 0
        if nx < 0 : nx = m-1
        if nx >= m: nx = 0
        if ny == sty and nx == stx: continue
        if maps[ny][nx] >= 0:
            maps[ny][nx] = maps[ny][nx] - (damage//2) if (maps[ny][nx] - (damage//2)) >= 0 else 0
            path.append([ny,nx])
    maps[y][x] = maps[y][x] - (damage) if (maps[y][x] - (damage)) >= 0 else 0
    return path

def repair(path):
    global maps
    for i in range(n):
        for j in range(m):
            if maps[i][j] > 0:
                flag = False
                for i1, j1 in path:
                    if i == i1 and j == j1:
                        flag = True
                        break
                if not flag:
                    maps[i][j] += 1

def countPotap():
    cnt = 0
    for i in maps:
        for j in i:
            if j > 0:
                cnt += 1
            if cnt >= 2:
                return True
    return False

for t in range(1, k+1):
    if not countPotap():
        break
    y,x = chooseWeakness()
    # print(y,x)
    attacks[y][x] = t
    maps[y][x] += (n+m)
    y1,x1 = attack(y,x)
    # 이제 레이저 or 포탄 공격
    path = laiser(y,x,y1,x1)
    if path:
        attackLaiser(path, maps[y][x], y1,x1)
    else:
        #포탄
        path = potan(y,x,y1,x1)
    # 정비
    repair(path)
ans = 0
for i in maps:
    for j in i:
        if ans < j:
            ans = j
# print(maps)
print(ans)
