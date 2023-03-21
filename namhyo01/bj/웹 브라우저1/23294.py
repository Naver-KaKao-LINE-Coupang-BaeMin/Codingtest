import sys
from collections import deque
input = sys.stdin.readline
'''
    뒤로가기 
        한개 이상 뒤로가기 공간에 있을시 
        현재는 앞으로 가기에저장
        방문한지 가장 최근 페이지 접속 => 그 페이지는 뒤로가기에서 삭제 ==> stack?
    앞으로가기
        앞으로 가기에 한 개 이상
        현재 보고있는 페이지를 뒤로가기에 저장
        앞으로 가기 공간에 방문한지 가장 최근 페이지 접속 => 삭제
    접속
        앞으로가기 공간에 저장된 페이지 **모두삭제** => 캐시에서 사이즈 줄어듬
        현재페이지는 뒤로가기에 추가, 당음에 접속할 페이지가 현재 페이지로 갱신 접속한 페이지 용량만큼 캐시 이용
        단 처음 웹페이지 접속시 현재 페이지를 뒤로가기에 추가 x
        만약 캐시 용량 최대시 뒤로가기에서 가장 오래된 페이지를 삭제 => 그 만큼 용량 제거 => 이과정은 반복 가능

    압축
        뒤로가기에서 같은 번호 페이지 연속 2개이상 등장시 => 가장 최근꺼ㅏ만 제외 모두 삭제
        삭제한만큼 줄어듬
'''
'''
    n : 웹페이지 종류
    q : 작업 개수
    c : 캐시 크기
'''
current = 0
back = deque([])
front = []
n,q,c = map(int, input().split())
sizes = [0]+list(map(int, input().split()))

for _ in range(q):
    work = input().split()
    if work[0] == 'B':
        if not back:
            continue
        front.append(current)
        current = back.pop()
        continue
    if work[0] == 'F':
        if not front:
            continue
        back.append(current)
        current = front.pop()
        continue
    if work[0] == 'C':
        if not back:
            continue
        temp = deque([back[0]])
        for i in range(1,len(back)):
            if back[i] == back[i-1]:
                c += sizes[back[i]]
                continue
            else:
                temp.append(back[i])
        back = temp
        continue
    # Access
    # 앞 삭제
    for size in front:
        c += sizes[size]
    front = []
    if current != 0:
        back.append(current)
    current = int(work[1])
    c -= sizes[current]
    while c<0: # 초과시
        num = back.popleft()
        c += sizes[num]
print(current)
if not back:
    print(-1)
else:
    for i in range(len(back)-1,-1,-1):
        print(back[i],end=' ')
    print()
if not front:
    print(-1)
else:
    for i in range(len(front)-1,-1,-1):
        print(front[i],end=' ')

