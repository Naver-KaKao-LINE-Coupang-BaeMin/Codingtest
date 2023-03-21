# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
from itertools import combinations
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

    # 바이러스를 놓을 수 있는 모든 위치 중 M개를 뽑아 각각 바이러스를 퍼뜨려보면서, 그 중 최소 시간을 출력한다.
    # 

    #### 초기 설정 ####
    # 지도를 확인하면서 각각의 값 (0, 1, 2) 마다 각각 다른 함수를 호출 해준다.
    #   1. 지도 값이 0이면, is_empty의 해당 위치에 1을 넣어 빈칸임을 표시한다. 빈칸 개수도 셀 수 있도록 empty 배열에 더해준다.
    #   2. 지도 값이 1이면, walls의 해당 위치에 INF 값을 넣어 벽임을 표시한다.
    #   3. 지도 값이 2이면, starters 에 해당 위치를 넣어 combinations로 뽑을 수 있도록 한다.

    def set_empty(xy):
        is_empty[xy] = 1
        empty.append(xy)
    
    def set_walls(xy):
        walls[xy] = INF

    N, M = map(int, input().split())
    L = N+1
    INF = 2500
    directions = (1, -1, L, -L)
    starters = [] # 바이러스 놓을 수 있는 위치들.
    walls = [0] * N * L + [INF] * L # 특정 위치가 벽인지 확인. 나중에 방문 체크하는 배열로도 사용 예정.
    empty = [] # 빈칸 개수를 세기 위한 배열
    is_empty = [0] * N * L # 특정 위치가 빈칸인지 확인. 1이면 빈칸.

    functions = (set_empty, set_walls, starters.append)

    for y in range(0, N*L, L):
        walls[y+N] = INF
        for xy, block in enumerate(map(int, input().split()), y):
            functions[block](xy)
    
    # 빈 공간이 없으면 바이러스 확산에 소요 시간 0
    if len(empty) == 0:
        return 0
    
    #### 바이러스 확산 확인 ####
    # 벽 배열을 방문 배열로 사용한다.
    # 각 조합을 돌리면서 빈 공간의 개수가 0이 되는 때 answer와 비교해 최솟값을 찾는다.

    id = 0
    answer = INF
    visited = walls
    for queue in combinations(starters, M):
        empty_count = len(empty)
        cque = list(queue)
        id += 1

        for xy in cque:
            visited[xy] = id
    
        for time in range(1, INF):
            nque = []

            for xy in cque:
                for d in directions:
                    if visited[xy + d] < id:
                        visited[xy + d] = id
                        nque.append(xy + d)
                
                        if is_empty[xy + d] == 1:
                            empty_count -= 1
                            if empty_count == 0:
                                answer = min(answer, time)
                                nque = []
                                cque.clear()
                                break
            
            if not nque:
                break
            cque = nque
    
    return answer if answer != INF else -1

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