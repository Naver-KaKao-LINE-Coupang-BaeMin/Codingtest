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
    # ######## INPUT AREA BEGIN ##########

    def dfs(me):
        visit[me] = 1
        for friend in friends[me]:
            if not visit[friend]:
                dfs(friend)
                cases[me][0] += cases[friend][1] # 내가 어답터가 아니려면 내 친구 모두 어답터여야 하므로, 내 친구가 어답터일 때의 어답터 수를 모두 더해줘야 함
                cases[me][1] += min(cases[friend][0], cases[friend][1]) # 내가 어답터라면, 내 친구가 어답터일 경우와 아닐 경우 중 어답터 수가 더 적은 경우를 더해주면 됨

    N = int(input().strip())
    sys.setrecursionlimit(N+3)
    friends = [[] for _ in range(N+1)]
    cases = [[0, 1] for _ in range(N+1)] # [내가 어답터가 아닐 때, 내가 어답터일 때]
    visit = [0] * (N+1)
    for _ in range(N-1):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)
    
    dfs(1)

    return min(cases[1])
    
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