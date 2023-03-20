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

    # 바둑판을 마진까지 포함해서 20 * 20 의 1차원 배열로 만듦
    # 오른쪽 = 1, 오른쪽 위 = -19, 오른쪽 아래 = 21, 아래 = 20

    # 바둑판에 돌이 놓여져 있다면, 네 방향으로 진행하며 갯수가 5가 되는지 확인
    # 갯수가 5인데, 첫 돌의 위치 반대 방향에 같은 색 돌이 있다면 육목이므로 정답 X

    # 혹시 8%에서 틀린다면, 출력 조건을 잘 읽어봐야 함

    board = []
    for y in range(0, 19*20, 20):
        line = list(map(int, input().split())) + [0]
        board.extend(line)
    board += [0] * 20
    
    directions = (1, -19, 20, 21)

    for y in range(0, 19 * 20, 20):
        for xy in range(y, y + 19):
            if board[xy] != 0:
                for d in directions:
                    nxy = xy + d
                    count = 1
                    while board[nxy] == board[xy]:
                        nxy += d
                        count += 1
                    # 갯수 5, 반대 방향에 자기 돌 없어야 정답
                    if count == 5 and board[xy - d] != board[xy]:
                        return str(board[xy]) + '\n' + str(xy // 20 + 1) + ' ' + str(xy % 20 + 1)
    
    return 0

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