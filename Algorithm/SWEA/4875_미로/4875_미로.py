# miro에서 0 : 통로, 1 : 벽, 2 : 출발, 3 : 도착
T = int(input())

# 델타이동하기
def dfs(starti,startj):
        global result
        # 오른쪽 -> 아래 -> 왼쪽 -> 위 순서로 델타이동
        # di : 행,y / dj : 열,x -> miro[y][x]
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]

        # 함수탈출조건 result의 값이 1이면 탈출
        if result:
            return

        # 미로 완전 탐색
        for i in range(4):
            for j in range(4):
                # 탐색할 위치 인덱스
                dy = starti+di[i]
                dx = startj+dj[j]
                # 미로를 벗어나는 경우에는 순회를 건너뛴다!!
                if dy<0 or dy>=N or dx<0 or dx>=N or miro[dy][dx] == 1:
                    continue

                # 도착하면 결과값을 변경하고 함수탈출
                if miro[dy][dx] == 2:
                    result = 1
                    return

                # 지나간 곳을 1로 방문기록함
                miro[starti][startj] = 1
                # 함수를 이동한 위치에서 다시 부른다.
                dfs(dy,dx)


for tc in range(1,T+1):
    N = int(input())
    miro = [list(map(int,input())) for _ in range(N)]

    # 출발,도착의 인덱스 찾기
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                # 도착 인덱스
                end_i,end_j = i,j
            elif miro[i][j] == 3:
                # 출발 인덱스
                start_i,start_j = i,j

    # 미로탈출결과 (미로탈출하면 호출한 함수에서 결과값이 1로 변경됨)
    result = 0
    # 함수호출
    dfs(start_i,start_j)

    print(f'#{tc} {result}')
