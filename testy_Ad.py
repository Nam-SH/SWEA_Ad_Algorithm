import sys; sys.stdin = open('data/(5250)input.txt', 'r')

from collections import deque

def BFS(y, x, calc):
    global Min

    q = deque()
    q.append((y, x, calc))

    while q:
        i, j, res = q.popleft()

        if res >= Min: return

        if (i, j) == (N - 1, N - 1):
            Min = min(Min, res)
            return

        for dy, dx in (1, 0), (0, 1):
            ty = i + dy; tx = j + dx
            if not (0 <= ty < N and 0 <= tx < N): continue
            if arr[ty][tx] > arr[i][j]: q.append((ty, tx, res + 1 + arr[ty][tx] - arr[i][j]))
            else: q.append((ty, tx, res + 1))

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [[0] * N for _ in range(N)]
    Min = 99999
    BFS(0, 0, 0)
    print('#{} {}'.format(tc + 1, Min))