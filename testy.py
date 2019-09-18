import sys; sys.stdin = open('data/(5248)input.txt', 'r')

T = int(input())
N, M = map(int, input().split())
arr = list(map(int, input().split()))

N, M = map(int, input().split())
arr = list(map(int, input().split()))

N, M = map(int, input().split())
arr = list(map(int, input().split()))

check = [[] for _ in range(N + 1)]

for i in range(0, len(arr) - 1, 2):
    check[arr[i]].append(arr[i + 1])

print(check[1:])

for i in range(len(check)):
