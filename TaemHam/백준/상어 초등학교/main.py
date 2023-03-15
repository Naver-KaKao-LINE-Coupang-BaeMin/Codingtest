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

    # 교실 테이블: 전체적으로 학생이 어디 앉아있는지 저장하는 테이블
    # 학생 테이블: 특정 학생의 자리를 저장해 놓는 테이블

    # 공간 테이블: 주위 빈 자리가 몇 개 있는지 알려주는 테이블. 학생이 앉으면 그 상하좌우를 -1 해준다.
    # 친구 테이블: 학생의 친구들을 셋으로 저장하는 테이블. 점수 계산시 필요.

    # 선호자리 테이블: 좋아하는 학생이 앉아 있다면, 그 상하좌우로 +1 해준다.

    N = int(input().strip())
    L = N+1
    classroom = [0] * (N * L) + [-1] * N # 교실 테이블. 빈 자리는 0, 못 앉는 곳은 -1
    seats = [-1] * (N**2 + 1) # 학생 테이블. 앉았으면 앉은 곳의 인덱스를, 아직 안앉았으면 -1
    likes = [0] * (N**2 + 1) # 친구 테이블. 학생 명수 만큼 세팅
    empties = [4] * (L * L) # 공간 테이블.
    remaining_seats = set(xy for y in range(0, L * N, L) for xy in range(y, y + N))

    for index in range(N):
        # 교실 테이블 가장 자리 못앉는 곳으로 세팅
        classroom[index * L + N] -= 1
        # 공간 테이블 가장자리들 -1 해줌
        empties[index] -= 1
        empties[index * L] -= 1
        empties[index * L + N - 1] -= 1
        empties[index + L * (N-1)] -= 1


    directions = [1, -1, L, -L] # 상하좌우 탐색시 사용할 방향.

    for _ in range(N**2):
        student, *friends = map(int, input().split())

        likes[student] = set(friends)

        prefers = [0] * L * N # 선호자리 테이블 초기화
        max_prefer_point = 0
        candidates = [] # 선호자리 가능한 자리
        for friend in friends:
            # 친구가 앉아있다면,
            if seats[friend] != -1:
                # 상하좌우를 탐색해서,
                for direction in directions:
                    current_location = seats[friend] + direction
                    # 그 자리가 빈자리라면, 선호 점수 +1점
                    if not classroom[current_location]:
                        prefers[current_location] += 1
                        # 최대 선호 점수 갱신 및 선호자리 가능한 자리로 추가
                        if max_prefer_point < prefers[current_location]:
                            max_prefer_point = prefers[current_location]
                            candidates = [current_location]
                        elif max_prefer_point == prefers[current_location]:
                            candidates.append(current_location)
        
        # 학생 자리 앉히기
        # 가능한 자리 중에서 찾고, 없다면 빈 자리에서 찾는다.
        # 빈자리가 가장 많은 자리 중 좌석 번호가 가장 작은 자리에 앉힌다.
        seat_location = max(candidates if candidates else remaining_seats, key = lambda x: (empties[x], -x))

        # 앉히고 나서 후처리
        remaining_seats.discard(seat_location)
        classroom[seat_location] = student
        seats[student] = seat_location
        for direction in directions:
            empties[seat_location + direction] -= 1

    scores = (0, 1, 10, 100, 1000)
    answer = 0
    # 점수 더하기
    for student in range(1, len(seats)):
        # 학생이 앉은 네 방향의 학생들과 친구들을 교집합 해 친구들 몇 명 있는지 구함.
        nearby_friends = set(classroom[seats[student] + direction] for direction in directions) & likes[student]
        answer += scores[len(nearby_friends)]

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