# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
#from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl
DEBUG = False

def main(f=None):
    init(f)
    # sys.setrecursionlimit(300000)
    # ######## INPUT AREA BEGIN ##########

    # 기존의 2차원 BFS에서 한 차원만 더해진 방식이다.
    # goal 변수에 안익은 토마토 개수를 넣고 토마토가 익을 때마다 하나씩 빼줌으로, 모든 토마토가 익었는지 판단하게 했다.

    # cque 와 nque, 두 개의 리스트를 사용해 deque 를 사용하지 않고 BFS를 돌릴 수 있다.
    # 1. cque 에 첫 단계를 돌릴 좌표를 넣어주고, 포문을 앞에서부터 돌린다.
    # 2. 포문을 돌리면서 다음 단계에 돌릴 좌표는 nque 에 넣어준다.
    # 3. 다음 단계를 위해 cque 에 nque를 넣어준다.
    # 4. nque가 비었다면 목표를 달성하기

    M, N, H = map(int, input().split())
    boxes = [[list(map(int, input().split())) for _ in range (N)] for _ in range(H)]
    cque = []
    goal = 0
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if boxes[z][y][x] == 1:
                    cque.append((z, y, x))
                elif boxes[z][y][x] == 0:
                    goal += 1

    directions = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))
    days = 0
    while goal:
        days += 1
        nque = []

        for z, y, x in cque:
            for dz, dy, dx in directions:
                nz = z + dz
                ny = y + dy
                nx = x + dx
                if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and not boxes[nz][ny][nx]:
                    goal -= 1
                    boxes[nz][ny][nx] = 1
                    nque.append((nz, ny, nx))
        
        if not nque:
            days = -1
            break
        cque = nque
    
    return days

    # M, N, H = map(int, input().split())
    # L = M + 1
    # K = L * (N + 1)
    # cque = []
    # goal = 0
    # for z in range(0, H * K, K):
    #     for zy in range(z, z * L, L):
    #         line = list(map(int, input().split()))
    #         for zyx, tomato in enumerate(line, zy):
    #             if tomato == 1:
    #                 cque.append(zyx)
    #             elif tomato == 0:
    #                 goal += 1

                # if boxes[z][y][x] == 1:
                #     cque.append((z, y, x))
                # elif boxes[z][y][x] == 0:
                #     goal += 1

    # directions = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))
    # days = 0
    # while goal:
    #     days += 1
    #     nque = []

    #     for z, y, x in cque:
    #         for dz, dy, dx in directions:
    #             nz = z + dz
    #             ny = y + dy
    #             nx = x + dx
    #             if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and not boxes[nz][ny][nx]:
    #                 goal -= 1
    #                 boxes[nz][ny][nx] = 1
    #                 nque.append((nz, ny, nx))
        
    #     if not nque:
    #         days = -1
    #         break
    #     cque = nque
    
    # return days

    # ######## INPUT AREA END ############


# TEMPLATE ###############################


enu = enumerate


def For(*args):
    return itertools.product(*map(range, args))


def Mat(h, w, default=None):
    return [[default for _ in range(w)] for _ in range(h)]


def nDim(*args, default=None):
    if len(args) == 1:
        return [default for _ in range(args[0])]
    else:
        return [nDim(*args[1:], default=default) for _ in range(args[0])]


def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input = sys.stdin.readline


def init(f=None):
    global input
    input = sys.stdin.readline  # io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    if os.path.exists("o"):
        sys.stdout = open("o", "w")
    if f is not None:
        setStdin(f)
    else:
        if len(sys.argv) == 1:
            if os.path.isfile("in/i"):
                setStdin("in/i")
            elif os.path.isfile("i"):
                setStdin("i")
        elif len(sys.argv) == 2:
            setStdin(sys.argv[1])
        else:
            assert False, "Too many sys.argv: %d" % len(sys.argv)


def pr(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end="\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    print(main())