# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import combinations
#import collections
# from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
# from bisect import bisect_left as bl
DEBUG = False

def main(f=None):
    init(f)
    # sys.setrecursionlimit(300000)
    # ######## INPUT AREA BEGIN ##########

    # 부분합이 K가 되려면, 임의의 누적합 원소 A[i] 와 A[j]의 차이가 K가 되면 된다.
    # 숫자를 돌아 누적합을 쌓아주면서, (현재까지의 누적합 - K) 였던 누적합이 등장했던 횟수를 정답에 더해주면 된다.

    # 예제 2번 설명
    #  숫자 |    1  2  3  4  5  0  
    #  누적 | 0  1  3  6 10 15 15
    #
    # 1. 누적합 1 - 5 = -4 는 없으니 +0
    # 2. 누적합 3 - 5 = -2 는 없으니 +0
    # 3. 누적합 6 - 5 = 1 은 1번 나왔으니 +1
    # 4. 누적합 10 - 5 = 5 는 없으니 +0
    # 5. 누적합 15 - 5 = 10 은 1번 나왔으니 +1
    # 6. 누적합 15 - 5 = 10 은 1번 나왔으니 +1

    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    summation = 0
    sum_dict = {0:1}
    answer = 0

    for number in numbers:
        summation += number
        
        # 누적합 - K가 등장했다면, 등장한 횟수 정답에 더해주기
        if summation - K in sum_dict:
            answer += sum_dict[summation - K]

        # 누적합 등장 횟수에 +1 해주기
        if summation in sum_dict:
            sum_dict[summation] += 1
        else:
            sum_dict[summation] = 1
    
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