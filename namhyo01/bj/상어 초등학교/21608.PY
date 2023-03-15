import sys
input = sys.stdin.readline
n = int(input())
likes = {}
dy = [0,0,1,-1]
dx = [1,-1,0,0]
maps = [[0 for _ in range(n)] for _ in range(n)]
score = {0:0,1:1,2:10,3:100,4:1000}


def returnClose(i,j):
    ans = []
    for k in range(4):
        x = i+dx[k]
        y = j+dy[k]
        if x<0 or y<0 or x>=n or y>=n:
            continue
        ans.append([x,y])
    return ans

def checkLikesMany(like):
    max_cnt = 0
    ans = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 0: # 비어있다면
                cnt = 0
                closest = returnClose(i,j)
                for y,x in closest:
                    if maps[y][x] in like:
                        cnt += 1
                if max_cnt == cnt:
                    ans.append([i,j])
                elif max_cnt < cnt:
                    ans = [[i,j]]
                    max_cnt = cnt
    return ans

def dopart2(part1):
    max_cnt = 0
    ans = []
    for y,x in part1:
        closest = returnClose(y,x)
        cnt = 0
        for cy, cx in closest:
            if maps[cy][cx] == 0:
                cnt += 1
        if cnt == max_cnt:
            ans.append([y,x])
        elif cnt > max_cnt:
            ans = [[y,x]]
            max_cnt = cnt
    return ans        

def dopart3(part2):
    part2.sort()
    return part2[0]


for _ in range(n**2):
    num,*like = list(map(int, input().split()))
    likes[num] = like
    part1 = checkLikesMany(like)
    if len(part1) == 1:
        maps[part1[0][0]][part1[0][1]] = num
    else:
        part2 = dopart2(part1)
        if len(part2) == 1:
            maps[part2[0][0]][part2[0][1]] = num
        else:
            part3 = dopart3(part2)
            # print(part3)
            maps[part3[0]][part3[1]] = num
        # 이제 part2로
ans = 0
for i in range(n):
    for j in range(n):
        closest = returnClose(i,j)
        cnt = 0
        for y,x in closest:
            if maps[y][x] in likes[maps[i][j]]:
                cnt+=1
        ans += score[cnt]

print(ans)