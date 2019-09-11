import sys; sys.stdin = open('data/(5185)input.txt', 'r')

def find(N):
    res = ''
    for i in range(int(N)):
        if len(data[i]) < 4: res += format(int(data[i], 16), 'b').zfill(4)
        else: res += format(int(data[i], 16), 'b')
    return res

for tc in range(int(input())):
    N, data = input().split()
    print('#{} {}'.format(tc + 1, find(N)))