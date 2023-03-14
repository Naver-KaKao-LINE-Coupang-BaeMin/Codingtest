import sys
import heapq
input = sys.stdin.readline
N = int(input())
queue = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if not queue:
            print(0)
            continue
        a, real = heapq.heappop(queue)
        print(real)
    else:
        heapq.heappush(queue, (abs(x), x))
