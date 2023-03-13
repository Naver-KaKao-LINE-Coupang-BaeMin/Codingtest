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

    # 시작 지점부터 각각의 지점까지 사각형에 포함된 값들을 미리 구해놓고, 포함 영역에서 미포함 영역을 빼주면 된다.

    # a b b
    # c d d
    # c d d 
    # 이런 영역이 있을 때, d 영역의 숫자의 합을 구하려면 a b c d 모든 구역의 합에서 a b c 를 빼주면 된다.
    # -> (a + b + c + d) - (a + b) - (a + c) + (빼기에서 중복 a)

    N, M = map(int, input().split())
    territory = [list(map(int, input().split())) for _ in range(N)]
    # 마진을 넣기 위해 +1 한 크기로 만들어준다
    square_sum = [[0] * (M+1) for _ in range(N+1)]
    for row in range(N):
        line_sum = 0
        for col in range(M):
            line_sum += territory[row][col]
            square_sum[row+1][col+1] = square_sum[row][col+1] + line_sum

    # x1, y1 을 포함하는 영역의 값을 구해야 한다.
    # 0 0 0 0
    # 0 a b b
    # 0 c d d
    # 0 c d d
    # 이렇게 위와 왼쪽에 마진을 넣어서 x1, y1에서는 -1 해서 넓이를 구해준다.
    
    K = int(input().strip())
    answer = []
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        x1 -= 1
        y1 -= 1
        answer.append(str(square_sum[x1][y1] + square_sum[x2][y2] - square_sum[x1][y2] - square_sum[x2][y1]))
    
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