import sys; sys.stdin = open('data/(5247)input.txt', 'r')


from collections import deque

def BFS():
    global start_num, end_num, result, tc

    q = deque()
    q.append((start_num, 0))

    while q:
        num, cnt = q.popleft()
        if num == end_num:
            result = cnt
            return

        for i in range(4):
            if not (0 < eval(N + operation[i]) <= 1000000): continue
            # if num_lst[num2] != tc:
            q.append((eval(N + operation[i]), cnt+1))

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    num_lst = [0] * 1000001
    num_lst[N] = tc
    result = 0
    BFS()
    print('#%d %d'%(tc, result))



def find(N):
    global Min, cnt
    print(N)
    if cnt >= Min: return

    if int(N) == int(M):
        Min = min(Min, cnt)
        return

    for i in range(4):
        if not (0 < eval(N + operation[i]) <= 1000000): continue
        if check[i]: continue
        check[i] = 1
        cnt += 1
        find(str(eval(N + operation[i])))
        cnt -= 1
        check[i] = 0


int(input())
for tc in range(2):
    N, M = input().split()
    Min = 9999
    check = [0]*4
    operation = ['+1', '-1', '*2', '-10']
    cnt = 0
    find(N)
    print('#{} {}'.format(tc + 1, Min))