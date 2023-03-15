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

    # 슬라이딩 윈도우로 K 만큼을 재배치 하는 경우를 모두 계산해 정답을 구해주는 문제다.

    # 어떤 특정 연속 부분 배열을 재배치 해서 가장 긴 연속적인 증가하는 배열이 나오도록 만드는 경우는,
    # 재배치할 연속 부분 배열과 비교해서
    #   1. 부분 배열 바로 왼쪽 숫자보다 큰 게 몇 개 있는지 세어서 왼쪽의 증가하는 배열과 이어주는 경우
    #   ex) 3 {1 5 2} 4 에 중괄호 숫자들을 재배치 하는 경우는, 3 보다 큰 수는 5 하나이므로, 왼쪽의 경우는 2
    #
    #   2. 부분 배열 바로 오른쪽 숫자보다 작은 게 몇 개 있는지 세어서 오른쪽의 증가하는 배열과 이어주는 경우
    #   ex) 3 {1 5 2} 4 에 중괄호 숫자들을 재배치 하는 경우는, 5 보다 작은 수는 1 2 이므로, 오른쪽의 경우는 3
    #
    #   3. 만약 왼쪽 숫자와 모두 이어지고, 오른쪽 숫자와 모두 이어지면 좌우를 이어주는 경우
    #   ex) 1 {3 2} 4 인 경우, 1보다 큰 수 갯수 == 4 보다 작은 수 갯수 == K 이므로, 왼쪽과 오른쪽을 이어줘 4.

    # 왼쪽과 이어줄 땐 순방향으로 잰 길이를 더해주고
    #   ex) 7 1 2 3 6 5 4 의 경우, 순방향 길이 배열은 [1, 1, 2, 3, 1, 1, 1], 
    #       여기서 7 1 2 3 {6 5 4} 로 재배치 하면, 배열 왼쪽 인덱스의 길이인 3을 더해준다.
    # 오른쪽과 이어줄 땐 역방향으로 잰 길이를 더해준다.
    #   ex) 7 3 2 1 4 5 6 의 경우, 역방향 길이 배열은 [1, 1, 1, 1, 3, 2, 1], 
    #       여기서 7 {3 2 1} 4 5 6 으로 재배치 하면, 배열 오른쪽 인덱스의 길이인 3을 더해준다.

    N, K = map(int, input().split())
    numbers = [2001] + list(map(int, input().split())) + [0]

    # 순방향 길이와 역방향 길이 구해줌
    inorder_counts = [0] + [1] * N + [0]
    reverse_counts = inorder_counts[:]
    for index in range(2, N+1):
        if numbers[index] > numbers[index - 1]:
            inorder_counts[index] += inorder_counts[index - 1]
        
        if numbers[-index] > numbers[-index - 1]:
            reverse_counts[-index - 1] += reverse_counts[-index]
    
    # 슬라이딩 윈도우로 재배치 할 연속 부분 배열 모두 연산 해 봄
    answer = K
    for index in range(1, len(numbers) - K):
        higher_than_prev = lower_than_next = 0
        for number in numbers[index:index+K]:
            higher_than_prev += 1 if number > numbers[index-1] else 0
            lower_than_next += 1 if number < numbers[index+K] else 0
        
        answer = max(answer, 
            # 1번 케이스
            inorder_counts[index-1] + higher_than_prev, 
            # 2번 케이스
            reverse_counts[index+K] + lower_than_next,
            # 3번 케이스
            inorder_counts[index-1] + K + reverse_counts[index+K] if higher_than_prev == lower_than_next == K else 0
        )
    
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