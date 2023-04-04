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
# from heapq import heappush, heappop
#import bisect
# from bisect import bisect_left as bl
DEBUG = False

def main(f=None):
    init(f)
    # sys.setrecursionlimit(100000)
    # ######## INPUT AREA BEGIN ##########

    TC = int(input().strip())
    answer = []

    for _ in range(TC):
        N, K = map(int, input().split())
        time_needed = [0] + list(map(int, input().split()))
        requisites = [[] for _ in range(N+1)]
        results = [0] * (N+1)
        counts = [0] * (N+1)

        for _ in range(K):
            before, after = map(int, input().split())
            requisites[before].append(after)
            counts[after] += 1

        queue = []
        
        for building in range(1, N+1):
            if counts[building] == 0:
                results[building] = time_needed[building]
                queue.append(building)

        goal = int(input().strip())
        
        for curr_building in queue:
            for next_building in requisites[curr_building]:
                results[next_building] = max(results[next_building], results[curr_building] + time_needed[next_building])
                counts[next_building] -= 1
                if counts[next_building] == 0:
                    queue.append(next_building)
        
        answer.append(str(results[goal]))
    
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