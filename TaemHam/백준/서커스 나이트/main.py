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

    def find(x):
        tracker = []
        while groups[x] != x:
            tracker.append(x)
            x = groups[x]
        for i in tracker:
            groups[i] = x
        return x
    
    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return
        if a > b:
            a, b = b, a
        groups[b] = a
        counts[a] += counts[b]


    input()
    dolphins = list(map(int, input().split()))
    answer = 1

    limit = max(dolphins) + 1
    prime_list = list(range(limit))
    for number in range(2, int(limit ** 0.5) + 1):
        if prime_list[number] == number:
            for next_number in range(number * 2, limit, number):
                if prime_list[next_number] == next_number:
                    prime_list[next_number] = number
                    
    groups = list(range(limit))
    counts = [0] * (limit)

    for dolphin in dolphins:

        base_group = prime_list[dolphin]
        while dolphin != 1:
            union(base_group, prime_list[dolphin])
            dolphin //= prime_list[dolphin]
        
        base_group = find(base_group)
        counts[base_group] += 1
        answer = max(answer, counts[base_group])

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