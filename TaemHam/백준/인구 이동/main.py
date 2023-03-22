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
#from bisect import bisect_left as bl
DEBUG = False

def main(f=None):
    init(f)
    # sys.setrecursionlimit(300000)
    # ######## INPUT AREA BEGIN ##########

    # 전날 인구 이동이 일어난 나라들만 인구 이동이 일어날 가능성이 있음.
    # -> 인구 이동이 안일어났던 나라는 다음 날 큐에서 제외

    # 1. 각각의 날마다 인구 이동 가능성 있는 나라를 저장하는 큐 (cque 와 nque)
    # 2. 하나의 나라와 연합되는 나라들을 저장하는 큐 (que)
    # -> 이중 BFS

    N, L, R = map(int, input().split())
    INF = 2001
    line = N + 1
    directions = (1, -1, line, -line)
    popul = [-1] * line * line
    visit = [INF] * line * line
    # 첫 날엔 모든 나라를 확인해야함
    cque = [xy for y in range(0, N * line, line) for xy in range(y, y + N)]

    for y in range(0, N * line, line):
        visit[y : y + N] = [-1] * N
        popul[y : y + N] = map(int, input().split())
    
    # BFS 시작
    for time in range(INF):
        nque = []
        for xy in cque:

            # 방문 처리
            if visit[xy] == time:
                continue
            visit[xy] = time

            # 연합 국가 인구수 구하기
            total = popul[xy]
            que = [xy]
            for location in que:
                for direction in directions:
                    if visit[location + direction] < time and L <= abs(popul[location] - popul[location + direction]) <= R:
                        visit[location + direction] = time
                        total += popul[location + direction]
                        que.append(location + direction)
            
            # 연합 국가 인구 이동
            if len(que) > 1:
                # 연합 국가 인구수 평균으로 설정
                average = total // len(que)
                for location in que:
                    popul[location] = average
                # 인구 이동이 일어났으니, 다음 날 큐에 추가
                nque.extend(que)
        
        # for y in range(0, N*line, line):
        #     print(popul[y:y+N])
        # print(nque)

        if not nque:
            return time
        
        cque = nque

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