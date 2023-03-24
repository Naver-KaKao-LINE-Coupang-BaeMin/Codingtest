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

    # 사각형을 1/4로 나눴을 때, 나눈 사각형들의 왼쪽 윗칸 기준 어느 칸을 가든 숫자 차이는 똑같음 
    # -> 특정 베이스(= 왼쪽 윗칸) * 사분면 숫자 (0, 1, 2, 3 중 하나) 를 더해가면 된다.

    N, R, C = map(int, input().split())
    N = len(format(max(R, C), 'b'))
    answer = 0
    multipliers = [0, 1, 2, 3]

    for size in range(N-1, -1, -1):

        base = 4 ** size

        if R < 2 ** size:
            multiplier = multipliers[:2]
        else:
            multiplier = multipliers[2:]
        
        if C < 2 ** size:
            multiplier = multiplier[0]
        else:
            multiplier = multiplier[1]
        
        answer += base * multiplier
        R %= 2 ** size
        C %= 2 ** size

    return answer

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
