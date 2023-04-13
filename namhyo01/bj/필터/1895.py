import sys
input = sys.stdin.readline

r,c = map(int, input().split())
pixels = [list(map(int, input().split())) for _ in range(r)]
t = int(input())

cnt = 0

def calcMid(arr):
    arr.sort()
    return arr[4]

for y in range(r-2): # y축
    for x in range(c-2): # x축
        arr = []
        for i in range(3):
            arr.append(pixels[y][x+i])
            arr.append(pixels[y+1][x+i])
            arr.append(pixels[y+2][x+i])
        if t <= calcMid(arr):
            cnt+=1
print(cnt)