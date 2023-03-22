# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import combinations
#import collections
from collections import deque
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

    def save_next(curr_page):
        if curr_page == -1:
            return
        if next_pages and next_pages[0][0] == curr_page:
            next_pages[0][1] += 1
        else:
            next_pages.appendleft([curr_page, 1])

    def save_prev(curr_page):
        if curr_page == -1:
            return
        if prev_pages and prev_pages[-1][0] == curr_page:
            prev_pages[-1][1] += 1
        else:
            prev_pages.append([curr_page, 1])
    
    def delete_next():
        next_pages[0][1] -= 1
        if next_pages[0][1] == 0:
            next_pages.popleft()
    
    def delete_prev():
        prev_pages[-1][1] -= 1
        if prev_pages[-1][1] == 0:
            prev_pages.pop()

    N, Q, C = map(int, input().split())
    page_sizes = list(map(int, input().split()))
    curr_memory = 0
    curr_page = -1
    prev_pages, next_pages = deque(), deque()

    for _ in range(Q):

        query, *number = input().split()

        if query == "B" and prev_pages:
            save_next(curr_page)
            curr_page = prev_pages[-1][0]
            delete_prev()
            continue
        
        if query == "F" and next_pages:
            save_prev(curr_page)
            curr_page = next_pages[-1][0]
            delete_next()
            continue
        
        if query == "A":
            page_index = int(number[0]) - 1
            
            while next_pages:
                page, count = next_pages.pop()
                curr_memory -= page_sizes[page] * count
            
            save_prev(curr_page)
            curr_page = page_index
            curr_memory += page_sizes[page_index]

            while curr_memory > C:
                curr_memory -= page_sizes[prev_pages[0][0]]
                prev_pages[0][1] -= 1
                if prev_pages[0][1] == 0:
                    prev_pages.popleft()
            continue
        
        if query == "C":
            for index in range(len(prev_pages)):
                page, count = prev_pages[index]
                if count > 1:
                    curr_memory -= page_sizes[page] * (count - 1)
                    prev_pages[index][1] = 1
    
    answer = []
    answer.append(str(curr_page + 1))

    if len(prev_pages) == 0:
        prev_pages.append([-2, 1])
    if len(next_pages) == 0:
        next_pages.append([-2, 1])

    prevs = []
    while prev_pages:
        page, number = prev_pages.pop()
        prevs.extend([str(page+1)] * number)
    nexts = []
    while next_pages:
        page, number = next_pages.popleft()
        nexts.extend([str(page+1)] * number)
        
    answer.append(' '.join(map(str, prevs)))
    answer.append(' '.join(map(str, nexts)))

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