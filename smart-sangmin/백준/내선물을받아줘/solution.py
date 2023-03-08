"""
3 4
SWWW
SEWN
EEEN

3 4 
SWWW
SNWN
EEEN

1 6
EEWWEW
"""

movement = {
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1)
}


def dfs(y, x, cnt):
    if check[y][x] != 0:
        return check[y][x]
    check[y][x] = cnt
    dy, dx = movement[maps[y][x]]
    ny, nx = y + dy, x + dx
    check[y][x] = dfs(ny, nx, cnt)
    return check[y][x]


# 초기 세팅
N, M = map(int, input().split())
maps = []
check = [[0] * M for _ in range(N)]
num = 1
for _ in range(N):
    maps.append(input())

for y in range(N):
    for x in range(M):
        if check[y][x] == 0:
            dfs(y, x, num)
            # for i in range(N):
            #     for j in range(M):
            #         print(check[i][j], end=" ")
            #     print()
            # print("----------------------")
            num += 1

answer = set()
for i in range(N):
    for j in range(M):
        answer.add(check[i][j])
print(len(answer))
