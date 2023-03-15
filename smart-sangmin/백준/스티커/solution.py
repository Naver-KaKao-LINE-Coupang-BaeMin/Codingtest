"""
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
"""
T = int(input())

for _ in range(T):
    N = int(input())
    sticker = []
    dp = []
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
    for i in range(1, N):
        if i == 1:
            sticker[0][i] = sticker[0][i] + sticker[1][i - 1]
            sticker[1][i] = sticker[1][i] + sticker[0][i - 1]
            continue
        sticker[0][i] = sticker[0][i] + max(sticker[1][i - 1], sticker[1][i - 2])
        sticker[1][i] = sticker[1][i] + max(sticker[0][i - 1], sticker[0][i - 2])

    print(max(sticker[0][-1], sticker[1][-1]))
