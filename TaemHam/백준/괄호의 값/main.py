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

    bracket = input().strip()
    open_bracket = { "(", "[" }
    close_bracket = { ")": "(", "]": "[" }
    bracket_score = { ")" : 2, "]" : 3 }
    stack = []
    stack_score = 0

    for b in bracket:

        # 만약 열린 괄호라면, 일단 스택에 더한다.
        if b in open_bracket:
            stack.append(b)
        
        # 닫힌 괄호라면:
        elif b in close_bracket:

            # "()[]]"
            # 스택이 ["[", 2, 3] 과 같은 형태면, 숫자만 모두 빼 더한다.
            while stack and stack[-1] not in open_bracket:
                stack_score += stack.pop()

            # 닫을 열린 괄호가 없어 에러
            if not stack:
                return 0
            
            # 괄호 내용이 비었으면, 곱해주기 위해 1로 초기화
            if not stack_score:
                stack_score = 1

            # 닫는 괄호와 마지막 여는 괄호가 매칭 됐다면:
            if stack[-1] == close_bracket[b]:
                stack.pop()
                stack_score *= bracket_score[b]
                stack.append(stack_score)
                stack_score = 0

            # 매칭 안됐다면 에러
            else:
                return 0
        
        # 이도 저도 아닌 이상한 문자라면: 
        else:
            return 0
    
    for num in stack:
        if num in open_bracket:
            return 0
        stack_score += num
    return stack_score

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
