
'''
3 2
cho
gahui alpa
mysql
namahage 754 cho alpa
dochida 644 cho cho
3
cho namahage X
gahui namahage W
mysql namahage X

2 2
OPPA IS,HATE,HOSPITAL
IHATE JYUSAGI
DONGMUL 755 OPPA JYUSAGI
maruchise 754 OPPA JYUSAGI
2
OPPA DONGMUL X
IHATE maruchise X
'''
import sys
input = sys.stdin.readline

users = {}
U, F = map(int, input().split())
for _ in range(U):
    line = input().split()
    if len(line) == 1:
        name = line[0]
        users[name] = [name]
    else:
        name, groups = line
        groups = groups.split(",")
        users[name] = groups + [name]
files = {}
for _ in range(F):
    filename, perm, owner, owner_group = input().split()
    files[filename] = {
        "perm": perm,
        "owner": owner,
        "owner_groups": owner_group
    }
operations = {
    "R": [4, 5, 6, 7],
    "W": [2, 3, 6, 7],
    "X": [1, 3, 5, 7]
}

N = int(input())
for _ in range(N):
    user, filename, op = input().split()
    groups = users[user]

    file_info = files[filename]

    perm = file_info["perm"]
    user_perm = int(perm[0])
    group_perm = int(perm[1])
    other_perm = int(perm[2])

    owner = file_info["owner"]
    owner_group = file_info["owner_groups"]

    if user == owner:
        if user_perm in operations[op]:
            print(1)
        else:
            print(0)
    elif owner_group in groups:
        if group_perm in operations[op]:
            print(1)
        else:
            print(0)
    else:
        if other_perm in operations[op]:
            print(1)
        else:
            print(0)
