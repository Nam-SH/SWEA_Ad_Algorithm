import sys; sys.stdin = open('data/(5250)input.txt', 'r')

def DFS(i, j, res):
    global Min

    if res >= Min: return

    if (i, j) == (N - 1, N - 1):
        if Min > res:
            Min = res
        return

    for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
        ty = i + dy; tx = j + dx
        if not (0 <= ty < N and 0 <= tx < N): continue
        if check[ty][tx]: continue
        check[ty][tx] = 1

        if arr[ty][tx] > arr[i][j]:
            DFS(ty, tx, res + 1 + arr[ty][tx] - arr[i][j])
        else:
            DFS(ty, tx, res + 1)

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [[0] * N for _ in range(N)]
    Min = 99999
    DFS(0, 0, 0)
    print('#{} {}'.format(tc + 1, Min))