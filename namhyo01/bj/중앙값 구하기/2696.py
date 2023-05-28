import sys
from heapq import heappush, heappop
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m = int(input())
    arr = []

    if m % 10 == 0:
        for _ in range(m//10):
            arr.extend(list(map(int, input().rstrip().split())))
    else:
        for _ in range(m//10+1):
            arr.extend(list(map(int, input().rstrip().split())))            
    
    cnt = 0

    small = []
    high = []
    mid = arr[0]
    res = [arr[0]]

    for i, v in enumerate(arr[1:],2):
        if v > mid: # 입력값이 중앙값보다 크다면? => 입력값을 high에다가 둔다
            heappush(high,v)
        else:
            heappush(small,-v) # 작다면 small에다가 두자
        if i % 2 == 1:
            if len(small) < len(high):
                heappush(small,-mid)
                mid = heappop(high)
            elif len(small) > len(high):
                heappush(high, mid)
                mid = -heappop(small)
            res.append(mid)
        
    print(len(res))
    for i in range(len(res)):
        if i != 0 and (i+1) % 10 == 1:
            print()
        print(res[i], end = ' ')
    print()


