# CP template Version 1.006
# import io
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
# from bisect import bisect_left as bl
DEBUG = False

def main(f=None):
    init(f)
    # ######## INPUT AREA BEGIN ##########

    # 지도를 벗어나지 않음 -> 어딜 가든 루프로 들어가게 된다 -> 루프의 갯수를 찾으면 된다.
    # 서 있는 장소를 가야할 장소의 집합에 넣어준다. -> 루프는 모두 같은 집합으로 세팅
    # 집합의 개수를 세주면 된다.

    N, M = map(int, input().split())
    moving_dict = {
        "E": 1,
        "W": -1,
        "N": -M,
        "S": M,
    }
    map_size = N*M
    moving_map = [0] * map_size

    # moving_map 의 인덱스는 현재 서 있는 위치, 값은 다음 이동할 위치로 만들어줌
    # SW  ->  20  
    # EN  ->  31  -> [2, 0, 3, 1] 로 바꾼다.
    for y in range(N):
        pattern = input().strip()
        line = y * M
        for x in range(M):
            moving_map[line + x] = line + x + moving_dict[pattern[x]]
    
    # 유니온 파인드 세팅
    groups = [i for i in range(map_size)]

    def find(x):
        if groups[x] != x:
            groups[x] = find(groups[x])
        return groups[x]
    
    # 현재 위치와 이동할 위치를 같은 집합으로 만듬
    for cur_pos, nxt_pos in enumerate(moving_map):
        group_a = find(cur_pos)
        group_b = find(nxt_pos)

        if group_a > group_b:
            group_a, group_b = group_b, group_a
        
        groups[group_b] = group_a 
    
    # 집합의 개수를 세어줌
    answer = 0
    for index in range(map_size):
        if index == find(index):
            answer += 1
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
    input = sys.stdin.readline # io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
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
