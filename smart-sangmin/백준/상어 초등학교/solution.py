from collections import OrderedDict


def get_seat1(favorite):
    cnt = {}
    adjacency = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    answer = [(-1, (N - 1, N - 1))]
    for friend in favorite:
        if friend in sitted_students.keys():
            y, x = sitted_students[friend]
            for dy, dx in adjacency:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < N and classroom[ny][nx] == 0:
                    if not cnt.get((ny, nx), False):
                        cnt[(ny, nx)] = 1
                    else:
                        cnt[(ny, nx)] += 1
                    if answer[0][0] < cnt[(ny, nx)]:
                        answer = [(cnt[(ny, nx)], (ny, nx))]
                    elif answer[0][0] == cnt[(ny, nx)]:
                        answer.append((cnt[(ny, nx)], (ny, nx)))
    return answer


def get_seat2(candidates):
    answer = [(-1, (N - 1, N - 1))]
    for cand in candidates:
        _, (y, x) = cand
        cnt = count_blank(y, x)
        if answer[0][0] == cnt:
            answer.append((cnt, (y, x)))
        elif answer[0][0] < cnt:
            answer = [(cnt, (y, x))]
    return answer


def empty_candidate():
    answer = [(-1, (N - 1, N - 1))]
    for y in range(N):
        for x in range(N):
            if classroom[y][x] == 0:
                cnt = count_blank(y, x)
                if answer[0][0] < cnt:
                    answer = [(cnt, (y, x))]
                if answer[0][0] == cnt:
                    answer.append((cnt, (y, x)))
    return answer


def count_blank(y, x):
    adjacency = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    cnt = 0
    for dy, dx in adjacency:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < N and 0 <= nx < N and classroom[ny][nx] == 0:
            cnt += 1
    return cnt


def count_close_friends(y, x):
    adjacency = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    me = classroom[y][x]  # 0
    friends = students[me]  # 0
    cnt = 0
    for i in range(4):
        dy, dx = adjacency[i]
        ny = y + dy
        nx = x + dx
        if 0 <= ny < N and 0 <= nx < N and classroom[ny][nx] in friends:
            cnt += 1
    return cnt


N = int(input())
classroom = [[0] * (N) for _ in range(N)]

students = {}
sitted_students = {}
for _ in range(N * N):
    line = list(map(int, input().split()))
    me, friends = line[0], line[1:]
    students[me] = friends

my_pos = (-1, -1)
for i, me in enumerate(students):
    friends = students[me]
    if i == 0:
        classroom[1][1] = me
        sitted_students[me] = (1, 1)
        continue
    candidates = get_seat1(friends)
    if candidates[0] == (-1, (N - 1, N - 1)):
        candidates = empty_candidate()
    elif len(candidates) != 1:
        candidates = get_seat2(candidates)
    candidates.sort(key=lambda x: (x[1][0], x[1][1]))
    _, (y, x) = candidates[0]
    classroom[y][x] = me
    sitted_students[me] = (y, x)


score = 0
for i in range(N):
    for j in range(N):
        score += int(pow(10, count_close_friends(i, j) - 1))
        # print(classroom[i][j], end="  ")
    # print()
print(score)
