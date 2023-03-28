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

    # 왼쪽 위 비트를 기준으로, 사각형 내의 모든 비트가 같다면 해당 비트를 반환
    # 만약 다르다면, 괄호로 덮어서 각 사분면에 대해 절반의 길이로 같은 작업을 수행
    
    def compact(start_x, start_y, size):

        if is_one_color(start_x, start_y, size):
            return image[start_x][start_y]
        else:
            half = size // 2
            return '(' + \
                compact(start_x, start_y, half) + \
                compact(start_x, start_y + half, half) + \
                compact(start_x + half, start_y, half) + \
                compact(start_x + half, start_y + half, half) + \
                ')'

    def is_one_color(start_x, start_y, size):
        color = image[start_x][start_y]
        for x in range(start_x, start_x + size):
            for y in range(start_y, start_y + size):
                if image[x][y] != color:
                    return False
        return True

    N = int(input().strip())
    image = [input().strip() for _ in range(N)]
    
    return compact(0, 0, N)

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