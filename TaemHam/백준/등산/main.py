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
from heapq import heappush, heappop
#import bisect
# from bisect import bisect_left as bl
DEBUG = False

def main(f=None):
    init(f)
    # sys.setrecursionlimit(100000)
    # ######## INPUT AREA BEGIN ##########

    # 호텔에서 특정 위치까지 가는 데 걸리는 시간, 오는 데 걸리는 시간을 각각 다익스트라로 구해준 후
    # 모든 위치를 for문으로 돌리며 (가는 데 걸린 시간 + 오는 데 걸린 시간) <= D 라면, 해당 위치의 최대값을 갱신시켜 정답을 구해주었다.

    # 알파벳을 높이 숫자로 바꿔주는 함수
    def get_height_number(alphabet):
        ascii_number = ord(alphabet)
        if ascii_number >= lower_margin:
            return ascii_number - lower_margin + 26
        return ascii_number - upper_margin

    N, M, T, D = map(int, input().split())
    L = M+1
    directions = (1, -1, L, -L)
    upper_margin, lower_margin = ord("A"), ord("a")

    heights = [-1] * L * (N + 1)
    for y in range(0, N*L, L):
        for xy, alphabet in enumerate(input().strip(), y):
            heights[xy] = get_height_number(alphabet)
            # print(alphabet, heights[xy])
        # print(heights[y:y+M])
    
    INF = sys.maxsize
    up_time = [INF] * len(heights)
    down_time = [INF] * len(heights)
    up_time[0] = down_time[0] = 0

    # 호텔에서 각 위치까지 "가는 데" 걸리는 시간 계산
    heapq = [(0, 0)] # (걸린 시간, 현재 위치)
    while heapq:
        total_time, curr_loc = heappop(heapq)

        if total_time > up_time[curr_loc]:
            continue
        
        for direction in directions:
            next_loc = curr_loc + direction
            # 가는 곳이 마진인 경우 거르고
            if heights[next_loc] == -1:
                continue
            height_diff = heights[next_loc] - heights[curr_loc]
            # 높이 차이가 T보다 큰 경우 거르고
            if height_diff > T:
                continue
            time_taken = height_diff ** 2 if height_diff > 0 else 1
            # 이 루트로 가는 시간이 다른 루트 보다 오래 걸리는 경우 거르고
            if total_time + time_taken >= up_time[next_loc]:
                continue
            up_time[next_loc] = total_time + time_taken
            heappush(heapq, (total_time + time_taken, next_loc))

    for y in range(0, N*L, L):
        print(up_time[y:y+M])

    # 각 위치에서 호텔로 "오는 데" 걸리는 시간 계산
    heapq = [(0, 0)]
    while heapq:
        total_time, curr_loc = heappop(heapq)

        if total_time > down_time[curr_loc]:
            continue
        
        for direction in directions:
            next_loc = curr_loc + direction
            if heights[next_loc] == -1:
                continue
            height_diff = heights[next_loc] - heights[curr_loc]
            if height_diff > T:
                continue
            # 위와 다른 곳은 여기 하나임. 내려가거나 같은 높이는 에너지 1, 나머지는 차이의 제곱
            time_taken = 1 if height_diff >= 0 else height_diff ** 2
            if total_time + time_taken >= down_time[next_loc]:
                continue
            down_time[next_loc] = total_time + time_taken
            heappush(heapq, (total_time + time_taken, next_loc))

    print()

    for y in range(0, N*L, L):
        print(down_time[y:y+M])

    # 모든 위치에 대해, (가는 데 걸리는 시간 + 오는 데 걸리는 시간) <= D 라면 최고 높이를 갱신시켜준다.
    max_travelable = heights[0]

    for y in range(0, N*L, L):
        for xy in range(y, y+M):
            if up_time[xy] + down_time[xy] <= D:
                max_travelable = max(max_travelable, heights[xy])

    return max_travelable

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