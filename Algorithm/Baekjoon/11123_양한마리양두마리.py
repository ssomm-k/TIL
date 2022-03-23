from collections import deque

def bfs(y,x):
    di,dj = [0,1,0,-1],[1,0,-1,0]

    q = deque()
    q.append([y,x])

    while q:
        Y,X = q.popleft()

        for i in range(4):
            dy = Y + di[i]
            dx = X + dj[i]

            if 0>dy or H<=dy or 0>dx or W<=dx or sheep[dy][dx] == '.':
                continue
            sheep[dy][dx] = '.'
            q.append([dy,dx])

# ------------------------------------------------------------------

T = int(input())

for tc in range(T):
    H,W = map(int,input().split())
    sheep = [list(map(str,input())) for _ in range(H)]

    cnt = 0
    for i in range(H):
        for j in range(W):
            if sheep[i][j] == '#':
                cnt += 1
                bfs(i,j)

    print(cnt)
'''
아래 코드에 반례

###
#.#
..#

def bfs():
    # #의 위치 모음
    q = deque()

    # #의 위치 찾기
    for i in range(H):
        for j in range(W):
            if sheep[i][j] == '#':
                q.append([i,j])
    # 델타
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    # q에 있는 좌표가 없을 때까지 반복
    while q:
        y,x = q.popleft()
        # 사방으로 확인
        for i in range(4):
            dy = y + di[i]
            dx = x + dj[i]
            # 사방으로 확인중에 양이 있으면 찾기를 멈춘다.
            if 0<=dy<H and 0<=dx<W and sheep[dy][dx] == '#':
                sheep[y][x] = '.'
                break
            
    # 양의 무리
    cnt = 0
    for i in sheep:
        cnt+=i.count('#')
    return cnt
'''