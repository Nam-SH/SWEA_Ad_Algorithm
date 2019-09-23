import sys; sys.stdin = open('data/(5207)input.txt', 'r')


def binary_search_recursion(target, start, end, data):
    global cnt

    if start > end: return

    mid = (start + end) // 2
    if data[mid] == target:
        cnt += 1
        return

    elif data[mid] > target:
        end = mid - 1

    else: start = mid + 1

    binary_search_recursion(target, start, end, data)
    return

for tc in range(int(input())):
    N, M = map(int, input().split())
    arr1 = sorted(list(map(int, input().split())))
    arr2 = list(map(int, input().split()))
    cnt = 0
    for target in arr2:
        binary_search_recursion(target, 0, len(arr1) - 1, arr1)

    print('#{} {}'.format(tc + 1, cnt))