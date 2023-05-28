import sys
input = sys.stdin.readline
import heapq

tc = int(input())

#시간 복잡도가 2000만번 이하 정도 되어야 시간안에 풀이가 됨.
#9999개의 수열을 sort로 정렬하게되면, 9999log9999의 시간복잡도 소요
#그리고 testcase 가 1000회 정도 이므로 1000* 9999log9999의 시간복잡도 소요 약 13억정도
# 그래서 sort함수 쓰면 안되고, min heap, max heap을 만들어서 써야함

for _ in range(tc):
    n = int(input())
    
    answer=[]

    arr = []

    min = []
    max = []

    #10개씩 input받기
    for _ in range(n//10+1):
        arr.extend(list(map(int,input().split())))

    mid = arr[0]
    answer.append(mid)

    for i in range(1,len(arr)):
        if mid<arr[i]:
            heapq.heappush(min,arr[i])
        else:
            heapq.heappush(max,-arr[i])
        # mid 갱신을 해야함
        if not i%2:
            if len(max) < len(min):
                heapq.heappush(max,-mid)
                mid = heapq.heappop(min)
            elif len(max) > len(min):
                heapq.heappush(min,mid)
                mid = -heapq.heappop(max)
            answer.append(mid)
    
    num = str(len(answer))

    finans = []

    finans.append(num)
    for i in range(10,len(answer),10):
        finans.append(' '.join(map(str,answer[i-10:i])))
    finans.append(' '.join(map(str,answer[len(answer)//10*10:])))

    print('\n'.join(finans))
