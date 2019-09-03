import sys; sys.stdin = open('data/(5189)input.txt', 'r')
from itertools import permutations

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    Min = 99999
    for lst in permutations(range(1, N)):
        sub = arr[0][lst[0]]
        for i in range(len(lst) - 1):
            sub += arr[lst[i]][lst[i + 1]]
        sub += arr[lst[i + 1]][0]
        if Min > sub:
            Min = sub
    print('#{} {}'.format(tc + 1, Min))