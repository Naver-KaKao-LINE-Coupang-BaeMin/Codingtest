# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import combinations
#import collections
#from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
# from bisect import bisect_left as bl
DEBUG = False

def main(f=None):
    init(f)
    # sys.setrecursionlimit(100000)
    # ######## INPUT AREA BEGIN ##########

    N, M = map(int, input().split())
    INF = sys.maxsize
    time = [INF] * 100002 # 도착 위치가 100000일 때, 두 번째 포문이 100001 까지 비교함

    # 원래 위치보다 낮은 곳들은 무조건 +1씩 해서 가야됨
    for distance in range(N+1):
        time[N - distance] = distance
    
    for distance in range(M - N + 2):

        location = N + distance

        # 현 위치가 짝수면, 순간이동 해서 올 경우와 비교
        if location % 2 == 0:
            time[location] = min(time[location], time[location // 2])
        # -1 에서 걸어올 경우와 비교
        time[location] = min(time[location], time[location - 1] + 1)
        # +1 에서 걸어올 경우와 비교해야 하지만, +1은 갱신이 안되어 있으므로, 갱신이 됐을 때 -1에서 비교
        time[location - 1] = min(time[location - 1], time[location] + 1)

    return time[M]

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