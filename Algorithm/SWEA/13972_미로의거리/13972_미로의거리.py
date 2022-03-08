from collections import deque

def bfs():
    # miro delta : 오 -> 아 -> 왼 -> 위
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    while miroque:

        y,x = miroque.popleft()

        for i in range(4):
            dy = y + di[i]
            dx = x + dj[i]
            if end_i == dy and end_j == dx:
                miro[dy][dx] = miro[y][x] - 2
                return miro[dy][dx]
            if 0<=dy<N and 0<=dx<N and (not miro[dy][dx]):
                miro[dy][dx] = miro[y][x] + 1
                miroque.append([dy,dx])

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    miro = [list(map(int,input())) for _ in range(N)]

    miroque = deque([])

    # 출발과 도착 위치 찾기
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                miroque.append([i,j])
            elif miro[i][j] == 3:
                end_i,end_j = i,j

    # 함수 호출
    result = bfs()

    # None인 경우
    if result == None:
        result =0

    # 결과 출력
    print(f'#{tc} {result}')