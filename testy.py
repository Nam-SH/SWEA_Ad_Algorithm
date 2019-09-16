import sys; sys.stdin = open('data/(5209)input.txt', 'r')

def backtrack(idx):
    global res, Min

    if res >= Min:
        return

    if idx == N:
        Min = min(Min, res)
        return

    for i in range(N):
        if check[i]: continue
        check[i] = True
        res += arr[idx][i]
        backtrack(idx + 1)
        res -= arr[idx][i]
        check[i] = False

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    res, Min = 0, 9999
    backtrack(0)
    print('#{} {}'.format(tc + 1, Min))