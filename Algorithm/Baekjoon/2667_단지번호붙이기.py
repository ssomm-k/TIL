from collections import deque
def bfs(y,x):
    q = deque()
    q.append([y,x])

    di,dj = [0,1,0,-1],[1,0,-1,0]
    while q:
        Y,X = q.popleft()
        for i in range(4):
            dy = Y + di[i]
            dx = X + dj[i]
            if 0>dy or N<=dy or 0>dx or N<=dx or not arr[dy][dx]:
                continue

            dangi[dy][dx] = dangi_num
            q.append([dy,dx])
            arr[dy][dx] = 0

    cnt = 0
    for i in dangi:
        cnt += i.count(dangi_num)
    
    dangi_h.append(cnt)

# -----------------------------------------------------------

N =  int(input())

arr = [list(map(int,input())) for _ in range(N)]
dangi = [[0]*N for _ in range(N)]

# 각 단지에 속하는 집의 수 리스트
dangi_h = []

# 총단지수
dangi_num = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] :
            dangi_num += 1
            dangi[i][j] = dangi_num
            bfs(i,j)

# 출력
print(dangi_num)
dangi_h.sort(reverse=False)
for i in dangi_h:
    print(i)