import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
weight = sorted(list(map(int, input().split())),reverse=True)
m = int(input())
box = sorted(list(map(int, input().split())),reverse=True)
if weight[0] < box[0]:
    print(-1)
    exit(0)
for i in range(1,m+1): # 시간이 최대 m보다 더 걸릴 수는 없다
    for w in weight:
        for b in box:
            if w>=b:
                box.remove(b)
                break
                # 크다면 => box에서 빼면 된다
    if not box:
        print(i)                
        break
    

        

