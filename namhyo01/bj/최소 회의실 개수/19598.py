import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
ref = []
for _ in range(n):
    a,b = map(int, input().split())
    ref.append((a,b))
ref.sort()
start, end = ref[0][0], ref[0][1]
cnt = 1
# nq = ref
hq = [end]
for i in range(1,n):
    start,end = ref[i][0], ref[i][1]
    if hq and hq[0] <= start:
        heappop(hq)
    heappush(hq, end)
print(len(hq))

# while True:
#     cq = []
#     for i in range(1, len(nq)):
#         if nq[i][0] >= end:
#             end = nq[i][1]
#         else:
#             cq.append((nq[i][0], nq[i][1]))
#     if not cq: break
#     nq = cq
#     start,end = nq[0][0], nq[0][1]
#     cnt+=1