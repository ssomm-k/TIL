import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    last_num = N * N
    arr = [[0]*N for _ in range(N)]
    # x -> 상하,di y -> 좌우,dj
    # arr[x][y]로 이동
    # 이동 순서는 오른쪽 -> 아래 -> 왼쪽 -> 위 시계방향
    # 이동방법
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    number = 1

    for i in range(N//2 + 1):
        for col in range(i,N-i):
            arr[i][col] = number
            number += 1
        for row in range(i+1,N-i):
            arr[row][-i-1] = number
            number += 1
        for col in range(N-i-2,i-1,-1):
            arr[-i-1][col] = number
            number += 1
        for row in range(N-i-2,i,-1):
            arr[row][i] = number
            number += 1

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end=' ')
        print()