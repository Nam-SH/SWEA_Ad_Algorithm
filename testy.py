import sys; sys.stdin = open('data/(A1)input.txt', 'r')

def find(sfdata):
    global res, cnt, lst

    if cnt > 5: return

    if len(lst) == N:
        if lst == sorted(lst) or lst == sorted(lst, reverse=True):
            res = cnt
            return




def shuffle(x, l, r):
    global lst

    if x >= 3:
        x = 5 - x
        l, r = r, l
    while l and r:
        for _ in range(3 - x):
            if l: lst.append(l.pop(0))
        for _ in range(3 - x):
            if r: lst.append(r.pop(0))
    return lst

t = int(input())
for tc in range(2):
    N = int(input())
    arr = list(map(int, input().split()))
    lst = []
    cnt = 0
    res = -1
    for x in range(6:)
        find(shuffle(x, arr[:N//2], arr[N//2:]))
        if 0 <= res <=5:
            print(res)
            break
    else:
        print(-1)