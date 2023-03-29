import sys
input = sys.stdin.readline

t =  int(input())

def solve(l,r,k,w):
    '''
        3번 부터 해보자
    '''
    di = {}
    for idx,value in enumerate(w):
        if value in di:
            di[value].append(idx)
        else:
            di[value] = [idx]
    smallest = float('inf')
    largest = -1
    for v in di.values():
        if len(v) >= k: # v가 k보다 이상이면 (자르면 되니)
            for i in range(len(v)-k+1): # 돌자 5-8 8-13
                length = v[i+k-1] - v[i] + 1
                smallest = min(smallest,length)
                largest = max(largest,length)
    if smallest == float('inf') and largest==-1:
        print(-1)
    else:
        print(smallest,largest)


for _ in range(t):
    w = input().strip()
    k = int(input())
    '''
        index가 필요하다 ㅎㅎ
    '''
    solve(0,len(w)-1,k,w)    