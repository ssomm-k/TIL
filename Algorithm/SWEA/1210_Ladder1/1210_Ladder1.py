import sys
sys.stdin = open("input (7).txt")

T = 10

for tc in range(1,T+1):
    tc_N = int(input())

    arr = []
    for i in range(100):
        lis = list(map(int,input().split()))
        arr.append(lis)

    y,x = 98,arr[99].index(2)

    for i in range(10000):
        if not y:
            print(f'#{tc} {x}')
            break
        else:
            if x == 99:
                if arr[y][x-1]:
                    arr[y][x] = 0
                    x -= 1
                elif arr[y-1][x]:
                    arr[y][x] = 0
                    y -= 1

            elif not x:
                if arr[y][x+1]:
                    arr[y][x] = 0
                    x += 1
                elif arr[y-1][x]:
                    arr[y][x] = 0
                    y -= 1
            else:
                if arr[y][x-1]:
                    arr[y][x] = 0
                    x -= 1
                elif arr[y][x+1]:
                    arr[y][x] = 0
                    x += 1
                elif arr[y-1][x]:
                    arr[y][x] = 0
                    y -= 1