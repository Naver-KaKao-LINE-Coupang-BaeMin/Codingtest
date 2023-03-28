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
    sys.setrecursionlimit(100000)
    # ######## INPUT AREA BEGIN ##########

    # 처음엔 while 문 돌려서 왼쪽 오른쪽 포인터가 가리키는 문자가 다르면,
    # 먼저 왼쪽 인덱스 바꾸고 확인하고, 아니면 오른쪽 인덱스 바꾸고 확인하고 하는 형식으로 했는데,
    # abbab 에서 왼쪽 인덱스를 올리면 bbab 가 남아서 2를 도출해 오답이 났었다.
    # 따라서 재귀 형식으로 바꿔주어 풀었다.

    def check(pattern, left, right, result):

        if left >= right:
            return result
        
        if pattern[left] == pattern[right]:
            return check(pattern, left + 1, right - 1, result)
        
        if result == 1:
            return 2
        
        return min(check(pattern, left + 1, right, 1), check(pattern, left, right - 1, 1))


    TC = int(input().strip())
    answer = []
    for _ in range(TC):
        pattern = input().strip()
        answer.append(str(check(pattern, 0, len(pattern) - 1, 0)))

    return '\n'.join(answer)

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