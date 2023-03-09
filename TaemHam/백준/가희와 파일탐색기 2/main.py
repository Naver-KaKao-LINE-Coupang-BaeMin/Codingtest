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
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    # 주의사항: 수정 권한이 있다면, 읽기 권한도 있다.

    # 권한 확인은 비트 연산으로 해결 가능.
    # 실행 권한은 2진수 001 과 & 연산해서 0이 아니면 된다.
    # 수정 권한은 2진수 010 과 & 연산해서 0이 아니면 된다.
    # 읽기 권한은 2진수 110 과 & 연산해서 0이 아니면 된다.

    # 권한 확인하는 함수
    def check(oprt, prms):
        if oprt == 'X':
            res = 1 & prms
        elif oprt == 'W':
            res = 2 & prms
        else: #oprt == 'R':
            res = 6 & prms
        return '1' if res else '0'

    U, F = map(int, input().split())
    group_dict = {}
    file_dict = {}

    # 그룹으로 유저 찾을 수 있도록 딕셔너리 세팅
    for _ in range(U):
        user_name, *user_group = input().split()
        # 본인은 본인 이름인 그룹에 속해야 함
        if user_name in group_dict:
            group_dict[user_name].append(user_name)
        else:
            group_dict[user_name] = [user_name]
        # 속한 그룹이 존재하면 콤마로 나누고 모든 그룹에 이름을 더해줌
        if user_group:
            for group_name in user_group[0].split(','):
                if group_name in group_dict:
                    group_dict[group_name].append(user_name)
                else:
                    group_dict[group_name] = [user_name]
    
    # 파일 이름으로 [권한, 소유자, 소유 그룹] 찾을 수 있도록 딕셔너리 세팅
    for _ in range(F):
        file_name, *file_info = input().split()
        file_info[0] = tuple(map(int, file_info[0]))
        file_dict[file_name] = file_info
    
    ans = []
    for _ in range(int(input().strip())):
        name, file, oprt = input().split()

        # 소유자라면, 첫 번째 숫자가 권한임
        if name == file_dict[file][1]:
            auth_pointer = 0
        # 소유 그룹에 속한다면, 두 번째 숫자가 권한임
        elif name in group_dict[file_dict[file][2]]:
            auth_pointer = 1
        # 어느 것도 아니면, 세 번째 숫자가 권한임
        else:
            auth_pointer = 2
        
        ans.append(check(oprt, file_dict[file][0][auth_pointer]))

    return '\n'.join(ans)

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