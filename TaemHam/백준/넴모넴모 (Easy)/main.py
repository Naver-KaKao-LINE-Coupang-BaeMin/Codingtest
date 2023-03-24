# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import combinations
#import collections
# from collections import deque
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

    # 한 칸 한 칸 진행하며 놓는 경우와 안놓는 경우 모두 해본다.
    # 만약 왼쪽, 위쪽, 왼쪽위 모두 놓여있는 경우 안놓는 경우만 해본다.
    # 게임판의 끝까지 도달하면 경우의 수에 +1

    def place(xy):
        global count

        # 게임판 마지막칸에 도달하면, 경우의 수에 +1
        if xy == N * L - 1:
            count += 1
            return
        
        # 마진에 도달한 경우, 다음 줄 첫 칸으로 보냄
        if xy % L == M:
            xy += 1
        
        # 안놓고 다음 칸을 보는 경우
        place(xy + 1)

        # 놓고 다음 칸을 보는 경우
        if not(board[xy - 1] and board[xy - L] and board[xy - L - 1]):
            board[xy] = 1
            place(xy + 1)
            board[xy] = 0

    N, M = map(int, input().split())
    L = M + 1
    board = [0] * N * L

    global count
    count = 0
    place(0)
    return count

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