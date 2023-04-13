# import sys
# sys.stdin = open("input.txt", "r")

def distance(mo1, mo2):
    x1, y1 = mo1
    x2, y2 = mo2
    return abs(x1 - x2) + abs(y1 - y2)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
# 이동
def move():
    global point
    for i in range(1, m + 1):
        count = False
        if mo[i] == (-1, -1):
            continue
        min_dis = distance(out[0], mo[i])
        min_x, min_y = mo[i]
        mx, my = mo[i]
        # print("mx : {}, my : {}".format(mx, my))
        for j in range(4):
            nx, ny = mx + dx[j], my + dy[j]
            temp_dis = distance(out[0], (nx, ny))
            if in_range(nx, ny) and min_dis > temp_dis and gido[nx][ny] == 0:
                count = True
                min_dis = temp_dis
                min_x, min_y = nx, ny
        if count :
            point += 1
            mo[i] = (min_x, min_y)
        # 도착하면 좌표 변경
            if mo[i] == out[0] :
                mo[i] = (-1, -1)
# 모두 탈출 했는지 확인 및 탈출한 모험가 좌표 변경
def check() :
    for i in range(1, m + 1) :
        if mo[i] != (-1, -1) :
            return False
    return True

# 사각형 찾는 함수
def find_square(s1) :
    x1, y1 = s1
    x2, y2 = out[0]
    len = 999

    if abs(x1 - x2) > abs(y1 - y2) :
        len = abs(x1 - x2)
    else :
        len = abs(y1 - y2)
    # print("len : ", len)
    for i in range(n) :
        for j in range(n) :
            if not in_range(i + len, j + len) :
                continue
            count = 0
            for l1 in range(len + 1) :
                for l2 in range(len + 1)  :
                    if s1 == (i + l1, j + l2) :
                        count += 1
                    elif out[0] == (i + l1, j + l2) :
                        count += 1
                    if count == 2 :
                        return i, j, len
    return -1, -1, -1
# 회전 하는 함수 회전도 2단계 입니다. 먼저 가장 작은 정사각형을 찾고, 그 후 회전
def change() :
    # 모험가 별로 사각형을 찾자루
    min_len = 999
    lx,ly = -1, -1
    for i in range(m + 1) :
        if mo[i] == (-1, -1) :
            continue
        x, y, temp_len = find_square(mo[i])
        if len == -1 :
            continue

        if min_len > temp_len :
            min_len = temp_len
            lx, ly = x, y
            # print("가장 작은 사각형의 모험가 : ", i)
        elif min_len == temp_len :
            if x < lx :
                min_len = temp_len
                lx, ly = x, y
                # print("가장 작은 사각형의 모험가 : ", i)
            elif x == lx :
                if y < ly :
                    min_len = temp_len
                    lx, ly = x, y
    #             print("가장 작은 사각형의 모험가 : ", i)
    # # 가장 작은 정사각형 왼쪽 위 좌표와 해당 사각형의 길이를 구했다
    # print("가장 작은 사각형의 좌표: {}, {}, {}".format(lx, ly, min_len))
    for i in range(lx, lx + min_len + 1) :
        for j in range(ly, ly + min_len + 1) :
            ti = i - lx
            tj = j - ly
            if gido[i][j] > 0 :
                temp_gido[tj + lx][min_len - ti + ly] = gido[i][j] - 1
            for k in range(1, m + 1) :
                if mo[k] == (-1, -1) :
                    continue
                mo_x, mo_y = mo[k]
                if i == mo_x and j == mo_y :
                    temp_mo[k] = (tj + lx, min_len - ti + ly)

            ox, oy = out[0]
            if i == ox and j == oy :
                temp_out[0] = (tj + lx, min_len - ti + ly)
    # print("gido : ", gido)
    # print("temp gido : ", temp_gido)
    for i in range(lx, lx + min_len + 1) :
        for j in range(ly, ly + min_len + 1) :
            gido[i][j] = temp_gido[i][j]

    for k in range(1, m + 1) :
        if mo[k] == (-1, -1) :
            continue
        mo[k] = temp_mo[k]

    out[0] = temp_out[0]


# T = int(input())
T = 1
for testcase in range(1, T + 1) :
    # n : 미로의 크기, m : 참가자 수, k : 게임 시간
    point = 0
    n, m, k = map(int, input().split())
    # 돌의 위치를 입력 받자 !
    gido = []
    for _ in range(n) :
        gido.append(list(map(int, input().split())))
    temp_gido = [arr[:] for arr in gido]
    mo = [(-1, -1)]
    # 모험가들의 좌표
    for _ in range(m) :
        mx, my = map(int, input().split())
        mo.append((mx - 1, my - 1))
    ox, oy = map(int, input().split())
    out = [(ox - 1, oy - 1)]
    temp_mo = [arr[:] for arr in mo]
    temp_out = [(ox - 1, oy - 1)]
    # print("n : {}, m : {}, k : {}".format(n, m, k))
    # print("격자 gido : ", gido)
    # print("mo (모험가 위치): ", mo)
    # print("out (출구) : ", out)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for time in range(k) :
        # 이동
        move()
        # print("이동 후")
        # print("mo (모험가 위치): ", mo)
        # print("point : ", point)
        if check() :
            break
        # 이동에 필요한 가짜 지도와 가짜 모험가 가짜 출구 좌표가 필요하다
        for i in range(n) :
            for j in range(n) :
                temp_gido[i][j] = 0
        temp_out[0] = out[0]
        for i in range(1, m + 1) :
            temp_mo[i] = mo[i]

        change()
        # print("회전 후")
        # print("격자 gido : ", gido)
        # print("mo (모험가 위치): ", mo)
        # print("out (출구) : ", out)
    print(point)
    out[0] = (out[0][0] + 1, out[0][1] + 1)
    print(*out[0])