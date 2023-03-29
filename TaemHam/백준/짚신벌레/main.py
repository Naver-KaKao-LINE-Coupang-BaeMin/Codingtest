# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import combinations
#import collections
from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
# from bisect import bisect_left as bl
DEBUG = False

def main(f=None):
    init(f)
    # sys.setrecursionlimit(300000)
    # ######## INPUT AREA BEGIN ##########

    # 인덱스를 나이로 두고, 개체 수를 저장하는 배열 age_counts는 하루가 지나면 오른쪽으로 쉬프트 해주어야 한다.
    # -> deque의 rotate 메서드 이용

    # 태어날 개체의 수 borns는 A살 이상, B살 미만 사이의 개체수의 합.
    # -> borns를 누적합으로 놓고, A살이 되는 개체 수를 더하고 B살이 되는 개체 수를 뺀다.

    A, B, D, N = map(int, input().split())
    total = 1
    borns = 0
    age_counts = deque([0] * D)
    age_counts[0] = 1

    for day in range(N):

        age_counts.rotate(1)
        deaths = age_counts[0]
        borns = (borns + age_counts[A] - age_counts[B]) % 1000
        age_counts[0] = borns
        total = (total + borns - deaths) % 1000
    
    return total

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