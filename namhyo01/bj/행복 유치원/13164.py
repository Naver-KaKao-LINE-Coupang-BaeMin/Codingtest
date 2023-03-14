import sys
from math import ceil
'''

'''
input = sys.stdin.readline
n,k = map(int, input().split())
keys = list(map(int, input().split()))
'''
    키를 최대한 비슷하게?
    k개 조로 나눈다 => 최대한 비스무리하게...?
'''
members = [keys[i+1]-keys[i] for i in range(n-1)]
tk = k
'''
이 방식은 무조건 TO다
2 2 1 4
1 3 5 6 10
2 1
5 2

5 2
2 2 1
2 2 1
3 2
4 1
'''
# for _ in range(k):
#     mem = ceil(n/tk)
#     members.append(mem)
#     n-=mem
#     tk-=1
members.sort(reverse=True)
print(sum(members[k-1:]))