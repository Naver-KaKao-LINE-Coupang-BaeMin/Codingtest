import sys
input = sys.stdin.readline

'''
    세트 승 => 6게임 이상 이기고 적어도 상대보다 2게임 이상 이겨야함
    만약 1 or 2세트 결과가 6대6이면 승자를 가리는 게임한판
    2세트를 먼저 이긴 사람이 테니스 경기의 승자다
    승자를 가리면 더이상 x
    federer는 세트에서 안패함 => 얘가 지면 x

'''
right = 'da'
wrong = 'ne'
a,b = input().strip().split()
n = int(input())
for _ in range(n):
    sets = list(input().strip().split())
    '''
        일단 승패 체크가 맞는지부터 체크잇
    '''
    a_win = b_win = 0
    iswrong = False
    for idx,set in enumerate(sets):
        if a_win==2 or b_win==2: # 하나라도 2승하면 더 이상 진행 x
            iswrong = True
            break
        a_score, b_score = map(int, set.split(':'))
        if abs(a_score-b_score) < 2: # 2미만이면
            if idx == 0 or idx == 1:
                if (a_score == 6 and b_score == 7):
                    b_win += 1
                    continue
                if (b_score == 6 and a_score == 7):
                    a_win += 1
                    continue
            iswrong = True
            break
        if a_score < 6 and b_score < 6:
            iswrong = True
            break
        if idx == 0 or idx == 1:
            if a_score >= 8 or b_score >= 8:
                iswrong = True
                break
        if a_score > b_score:
            a_win += 1
        else:
            b_win += 1
    if a == 'federer' and b_win > 0:
        print('ne')
        continue
    if b == 'federer' and a_win > 0:
        print('ne')
        continue
    if iswrong:
        print('ne')
    else:
        if a_win==2 or b_win == 2:
            print('da')
        else:
            print('ne')
