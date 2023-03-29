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
    # sys.setrecursionlimit(100000)
    # ######## INPUT AREA BEGIN ##########


    # 올바르지 않은 세트면 0을, 올바른 세트면 이긴 플레이어 숫자를 반환하는 함수.
    def check_winner(score, match_number):
        p1_point, p2_point = map(int, score.split(":"))
        loser_point, winner_point = sorted([p1_point, p2_point])

        # 승자가 5점 이하인 경우는 없음
        if winner_point < 6:
            return 0

        # 6:0 ~ 4 모두 가능, 6:5 ~ 6 불가능
        elif winner_point == 6:
            if loser_point in {5, 6}:
                return 0
        
        # 7:0 ~ 4, 7은 불가능, 7:5는 모두 가능, 7:6 은 앞 두 세트만 가능
        elif winner_point == 7:
            
            if match_number < 2:
                if loser_point not in {5, 6}:
                    return 0
            else:
                if loser_point != 5:
                    return 0
                
        # 앞 두 세트는 8점 이상이 나올 수 없고, 세 번째 세트는 점수 차가 2여야 함.
        else:
            if match_number < 2 or winner_point - loser_point != 2:
                return 0
        
        # 승자 판별
        if p1_point == winner_point:
            return 1
        return 2

    player1, player2 = input().split()
    matches = int(input().strip())
    answer = []

    for _ in range(matches):

        points = {
            player1: 0,
            player2: 0
        }
        scores = input().split()
        is_invalid_set = False

        for match_number, score in enumerate(scores):

            winner = check_winner(score, match_number)
            
            if winner == 0:
                is_invalid_set = True
                break

            winner_name, loser_name = (player1, player2) if winner == 1 else (player2, player1)

            if loser_name == 'federer':
                is_invalid_set = True
                break

            points[winner_name] += 1
        
        if is_invalid_set or max(points[player1], points[player2]) != 2 or points[player1] == points[player2]:
            answer.append('ne')
            continue

        answer.append('da')

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