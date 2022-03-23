from collections import deque
import copy

# 전설의 명검 "그람"을 생각하지않는 경우
def bfs1():
    yongsa1 = copy.deepcopy(miro)
    q = deque([[0,0]])
    di,dj = [0,1,0,-1],[1,0,-1,0]

    while q:
        y,x = q.popleft()
        if y == N-1 and x == M-1:
            return yongsa1[N-1][M-1]

        for i in range(4):
            dy = y + di[i]
            dx = x + dj[i]

            if 0>dy or N<=dy or 0>dx or M<=dx or\
                yongsa1[dy][dx]:
                continue

            q.append([dy,dx])
            yongsa1[dy][dx] = yongsa1[y][x]+1

# 전설의 명검 "그람"을 만나면 벽이 없어지는 경우
def bfs2():
    yongsa2 = copy.deepcopy(miro)
    q = deque([[0,0]])
    di,dj = [0,1,0,-1],[1,0,-1,0]

    while q:
        y,x = q.popleft()
        if y == N-1 and x == M-1:
            return yongsa2[N-1][M-1]

        for i in range(4):
            dy = y + di[i]
            dx = x + dj[i]

            if 0<=dy<N and 0<=dx<M and yongsa2[dy][dx] == -2:
                for j in range(N):
                    for k in range(M):
                        if yongsa2[j][k] == -1:
                            yongsa2[j][k] = 0
                yongsa2[dy][dx] = 0

            if 0>dy or N<=dy or 0>dx or M<=dx or\
                yongsa2[dy][dx]:
                continue

            q.append([dy,dx])
            yongsa2[dy][dx] = yongsa2[y][x]+1
                
# -------------------------------------------------------------------------

N,M,T = map(int,input().split())

miro = [list(map(int,input().split())) for _ in range(N)]

# 벽을 -1 전설의 검은 -2로 바꿔주기
for i in range(N):
    for j in range(M):
        if miro[i][j] == 1:
            miro[i][j] = -1
        elif miro[i][j] == 2:
            miro[i][j] = -2

cnt1,cnt2 = bfs1(),bfs2()

if cnt1 and cnt2:
    if min(cnt1,cnt2) <= T:
        print(min(cnt1,cnt2))
    else:
        print("Fail")
else:
    print("Fail")