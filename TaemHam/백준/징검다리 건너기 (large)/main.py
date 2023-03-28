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

    # 돌의 갯수 최대 5000개, N**2 == 25000000 도 커버 가능 

    # 한 번에 모든 돌을 뛰었을 때 드는 에너지를 최대 값으로 두어 이분 탐색을 진행
    # mid 에너지 이내로 뛸 수 있다면 방문 처리 해서, 처음부터 하나씩 돌아가며 다른 돌로 뛸 수 있는지 체크
    # 마지막 돌이 방문 체크 됐다면 탐색 성공.

    N = int(input().strip())
    stones = list(map(int, input().split()))
    left, right = 0, (N - 1) * (1 + abs(stones[-1] - stones[0]))
    visit = [0] * len(stones)
    id = 0

    while left + 1 < right:
        id += 1
        mid = (left + right) // 2
        visit[0] = id

        for from_index in range(len(stones)):

            if visit[from_index] < id:
                continue

            for to_index in range(from_index + 1, len(stones)):
                energy = (to_index - from_index) * (1 + abs(stones[to_index] - stones[from_index]))
                if energy <= mid:
                    visit[to_index] = id
        
        if visit[-1] == id:
            right = mid
        else:
            left = mid

    return right

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