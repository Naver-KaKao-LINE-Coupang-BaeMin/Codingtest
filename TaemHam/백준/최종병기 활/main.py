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

    # 이분 탐색으로 찾을 값 = 잘랐을 때 나와야하는 최소 고무줄 길이
    # mid 값으로 잘랐을 때 횟수가 K번이 안나오면 길이를 줄여야 함
    # 잘라졌다면, 잘라진 길이들 중 최솟값을 정답과 비교해 가장 긴 걸 뽑으면 됨

    def get_length(from_index, to_index):
        if from_index == to_index:
            return N
        return (marks[to_index] - marks[from_index]) % N

    N, M, K = map(int, input().split())
    marks = [int(input().strip()) for _ in range(M)]
    cut_index = list(range(M))
    answer = 0

    for start_mark in range(M):
        left, right = 0, N+1

        while left + 1 < right:
            mid = (left + right) // 2
            previous_mark = start_mark
            count = 0

            for current_mark in cut_index[start_mark + 1:] + cut_index[:start_mark + 1]:
                length = get_length(previous_mark, current_mark)
                if length < mid:
                    continue
                previous_mark = current_mark
                count += 1
            
            if count >= K:
                left = mid
            else:
                right = mid
        
        answer = max(answer, left)
        
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