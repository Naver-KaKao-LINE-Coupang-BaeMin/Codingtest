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
    # sys.setrecursionlimit(1000000)
    # ######## INPUT AREA BEGIN ##########

    # A지점과 B지점 둘 다에 우물을 파는 것보다, 둘 중 하나에 우물을 파고 물을 끌어오는 게 이득이라면, 끌어온다(== 합친다).
    # irri_cost -> 그룹장 인덱스에 모든 그룹원의 물 대는 비용의 누적값을 저장한다.
    # well_cost -> 그룹장 인덱스에 모든 그룹원의 우물 파는 비용 중 최솟값을 저장한다.
    # 마지막에 set을 이용해 그룹장만 하나씩 남기고, 우물 파는 비용의 최솟값 + 물 대는 비용의 누적값을 모두 더해주면 된다.

    def find(x):
        tracker = []
        while groups[x] != x:
            tracker.append(x)
            x = groups[x]
        for i in tracker:
            groups[i] = x
        return x
    
    def union(a, b, c):
        a, b = find(a), find(b)
        if a == b or well_cost[a] + well_cost[b] <= min(well_cost[a], well_cost[b]) + c:
            return
        if a > b:
            a, b = b, a
        groups[b] = a
        well_cost[a] = min(well_cost[a], well_cost[b])
        irri_cost[a] += irri_cost[b] + c

    N = int(input().strip())
    well_cost = list(int(input().strip()) for _ in range(N)) 
    irri_cost = [0] * N
    cost_queue = []
    for here in range(N - 1):
        costs = list(map(int, input().split()))
        for there in range(here + 1, N):
            cost_queue.append((here, there, costs[there]))
    cost_queue.sort(key= lambda x: x[2])
    groups = list(range(N))

    for here, there, cost in cost_queue:
        union(here, there, cost)
    
    # find 해주지 않으면, 그룹 번호가 갱신이 되어있지 않은 것도 존재 할 수 있음
    divided_groups = set(map(lambda x: find(x), groups))

    return sum(map(lambda x: well_cost[x] + irri_cost[x], divided_groups))

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