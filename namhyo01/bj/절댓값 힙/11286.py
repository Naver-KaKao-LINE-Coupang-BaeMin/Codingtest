import sys
from queue import PriorityQueue
input = sys.stdin.readline
queue = PriorityQueue()
n = int(input())
for _ in range(n):
    x = int(input())
    if x==0:
        if queue.empty():
            print(0)
        else:
            data = queue.get()
            print(data[0]*data[1])
    else:
        queue.put((abs(x),-1 if x<0 else 1))