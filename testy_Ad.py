import sys; sys.stdin = open('data/(5250)input.txt', 'r')

def floydWarshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if arr[i][j] > arr[i][k] + arr[k][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]
    return


for tc in range(int(input())):
    N= int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    floydWarshall()

    print(arr)
    # print('#{} {}'.format(tc + 1, floydWarshall()))