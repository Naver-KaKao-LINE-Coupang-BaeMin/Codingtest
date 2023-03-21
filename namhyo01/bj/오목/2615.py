import sys
input = sys.stdin.readline
maps = []
for _ in range(19):
    maps.append(list(map(int, input().split())))

dy = [0,1,-1,1]
dx = [1,1,1,0]

for i in range(19):
    for j in range(19):
        if maps[i][j] == 1: # 검
            for l in range(4):
                cnt = 1
                ny = i+dy[l]
                nx = j+dx[l]
                while 0<=ny<19 and 0<=nx<19 and maps[ny][nx] == 1:
                    nx += dx[l]
                    ny += dy[l]
                    cnt+=1
                    if cnt == 5:
                        # 육목검사
                        if 0<=ny<19 and 0<=nx<19 and maps[ny][nx] == 1:
                            break
                        if 0<=j-dx[l]<19 and 0<=i-dy[l]<19 and maps[i-dy[l]][j-dx[l]] == 1: # 그이전
                            break
                        print(1)
                        print(i+1,j+1)
                        exit(0)

        if maps[i][j] == 2: # 흰
            for l in range(4):
                cnt = 1
                ny = i+dy[l]
                nx = j+dx[l]
                while 0<=ny<19 and 0<=nx<19 and maps[ny][nx] == 2:
                    nx += dx[l]
                    ny += dy[l]
                    cnt+=1
                    if cnt == 5:
                        # 육목검사
                        if 0<=ny<19 and 0<=nx<19 and maps[ny][nx] == 2: # 그 이후
                            break
                        if 0<=j-dx[l]<19 and 0<=i-dy[l]<19 and maps[i-dy[l]][j-dx[l]] == 2: # 그이전
                            break
                        print(2)
                        print(i+1,j+1)
                        exit(0)

print(0)
