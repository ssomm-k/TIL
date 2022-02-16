import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    last_num = N * N
    arr = [[0]*N for _ in range(N)]

    # x -> 좌우,di y -> 상하,dj
    # arr[y][x]로 이동
    # 이동 순서는 오른쪽 -> 아래 -> 왼쪽 -> 위 시계방향
    # 이동방법
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    y = x = 0
    now = 0

    for i in range(1,last_num+1):
        arr[y][x] = i

        y += di[now]
        x += dj[now]

        if y >= N or x >= N or arr[y][x]:
            y -= di[now]
            x -= dj[now]
            now += 1
            if now == 4:
                now = 0
            y += di[now]
            x += dj[now]

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()