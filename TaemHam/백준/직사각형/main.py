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

    # 1. 길이 역순으로 정렬 
    #   [10, 6, 6, 6, 5, 4, 4, 4, 3]
    # 2. 길이들을 이전 인덱스의 길이들과 비교, 길이가 같거나 1 차이 나면 변으로 추가
    #   10, 6 차이 너무 큼, 10 버림
    #   6, 6 사용 가능, 6 추가 후 인덱스 하나 뜀
    #   6, 5 사용 가능, 5 추가 후 인덱스 하나 뜀
    #   ...
    # 3. 사용 가능한 변들 역시 가장 긴 변부터 곱해 넓이로 더해줌

    N = int(input().strip())
    # 1. 역순 정렬
    lines = sorted(map(int, input().split()), reverse = True)
    sides = []
    index = 1
    # 2. 변 추가
    while index < len(lines):
        if lines[index] == lines[index - 1] or lines[index] == lines[index - 1] - 1:
            sides.append(lines[index])
            index += 2
            continue
        index += 1
    # 3. 넓이 합
    answer = 0
    for index in range(1, len(sides), 2):
        answer += sides[index] * sides[index - 1]
    
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