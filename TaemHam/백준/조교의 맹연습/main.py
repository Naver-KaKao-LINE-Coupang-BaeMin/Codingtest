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

    # "dp[보는 방향][남은 에너지] = 제식 횟수" 일때,
    # dp[현재 보는 방향][현재 남은 에너지] = min(dp[현재 보는 방향][현재 남은 에너지], dp[제식 전의 방향][제식 전의 남은 에너지] + 1)
    # 보는 방향이 0으로 시작해서 0으로 끝나고 남은 에너지가 0일 때의 제식 횟수를 구하면 된다.

    INF = sys.maxsize
    A, B, C, K = map(int, input().split())
    energy = [(A, 1), (B, -1), (C, 2)]
    dp = [[INF] * (K+1) for _ in range(4)]
    dp[0][K] = 0
    for curr_energy in range(K-min(A, B, C), -1, -1):
        for use_energy, spin in energy:
            if curr_energy + use_energy <= K:
                for direction in range(4):
                    dp[direction][curr_energy] = min(dp[direction][curr_energy], dp[(direction + spin) % 4][curr_energy + use_energy] + 1)

    return dp[0][0] if dp[0][0] != INF else -1

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