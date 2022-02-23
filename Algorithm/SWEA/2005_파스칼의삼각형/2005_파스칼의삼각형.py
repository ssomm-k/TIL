import sys
sys.stdin = open("input (10).txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = []
    for i in range(1,N+1):
        arr.append([0]*i)

    arr[0][0] = 1

    for i in range(1,N):
        for j in range(i+1):
            if 0 < j < i :
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            elif not j:
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = arr[i-1][j-1]

    print(f'#{tc}')
    for i in arr:
        print(*i)