import sys; sys.stdin = open('data/(A1)input.txt', 'r')

def find(lst):
    global res, cnt, visit

    if cnt > 5: return

    if len(lst) == N:
        if lst == sorted(lst) or lst == sorted(lst, reverse=True):
            res = cnt
            return

    for x in range(len(visit)):
        if not visit[x]:
            visit[x] = 1
            find(shuffle(x, lst[:N//2], lst[N//2:]))


def shuffle(x, l, r):
    global lst, cnt
    if x >= 3:
        x = 5 - x
        l, r = r, l
    while l and r:
        for _ in range(3 - x):
            if l: lst.append(l.pop(0))
        for _ in range(3 - x):
            if r: lst.append(r.pop(0))
    cnt += 1
    return lst


t = int(input())
for tc in range(5):
    N = int(input())
    arr = list(map(int, input().split()))
    lst = []
    cnt = 0
    res = -1
    visit = [0]*6
    for x in range(6):
        visit[x] = 1
        find(shuffle(x, arr[:N//2], arr[N//2:]))
        visit[x] = 0
        if 0 <= cnt <=5:
            print(cnt)
            break
    else:
        print(-1)

