import sys; sys.stdin = open('data/(5250)input.txt', 'r')

from heapq import heappush, heappop

def prim(start):

    visit[start] = True

    priority_queue = []

    for i in range(len(arr[start])):
        nextweight, next = arr[start][i]
        heappush(priority_queue, (nextweight, next))

    ans = 0
    while priority_queue:

        hereweight, here = heappop(priority_queue)
        if visit[here]: continue
        visit[here] = True
        ans += hereweight
        for i in range(len(arr[here])):
            thereweight, there = arr[here][i]
            heappush(priority_queue, (thereweight, there))
    print(ans)

V = 7
E = 11

visit = [0] * (V + 1)

arr = [[] for _ in range(V + 1)]

data = [
    (1, 2, 2),
    (2, 3, 5),
    (1, 3, 20),
    (1, 4, 10),
    (4, 5, 1),
    (5, 6, 23),
    (3, 6, 3),
    (3, 5, 6),
    (7, 6, 9),
    (7, 3, 2),
    (2, 7, 7)
]

for num1, num2, weight in data:
    arr[num1].append((weight, num2))
    arr[num2].append((weight, num1))

prim(1)