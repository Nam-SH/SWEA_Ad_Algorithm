import sys; sys.stdin = open('data/(5249)input.txt', 'r')


def getParent(parent, num):
    if parent[num] == num: return num
    return getParent(parent, parent[num])

def unionParent(parent, num1, num2):
    a = getParent(parent, num1)
    b = getParent(parent, num2)
    if a == b: return
    if a < b: parent[b] = a
    else: parent[a] = b

def findParent(parent, num1, num2):
    a = getParent(parent, num1)
    b = getParent(parent, num2)
    if a == b: return True
    else: return False


for tc in range(int(input())):

    V, E = map(int, input().split())

    parent = [i for i in range(V + 1)]

    arr = [tuple(map(int, input().split())) for _ in range(E)]

    arr.sort(key = lambda x: x[2])

    sum = 0
    for a in arr:
        if findParent(parent, a[0], a[1]): continue
        sum += a[2]
        unionParent(parent, a[0], a[1])

    print('#{} {}'.format(tc + 1, sum))