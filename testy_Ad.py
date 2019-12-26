import sys;sys.stdin = open('data/(5250)input.txt', 'r')

from collections import deque

def find():
    q = deque()
    q.append((0, 0))
    check[0][0] = 0

    while q:
        y, x = q.popleft()
        for ny, nx in (-1, 0), (0, 1), (1, 0), (0, -1):
            ty = y + ny; tx = x + nx
            if not (0 <= ty < N > tx >= 0): continue

            if arr[ty][tx] > arr[y][x]: w = arr[ty][tx] - arr[y][x] + 1
            else: w = 1

            if check[ty][tx] > check[y][x] + w:
                check[ty][tx] = check[y][x] + w
                q.append((ty, tx))

    return check[N - 1][N - 1]


for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [[0xffffff] * N for _ in range(N)]
    ans = find()

    print(f'#{tc + 1} {ans}')