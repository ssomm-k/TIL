# 나눠서 푼 경우 = bfs 2번 사용
from pprint import pprint
from collections import deque

def bfs(y,x,status):
    visited = [[0]*(m+1) for _ in range(n+1)]
    q = deque([(y,x)])
    visited[y][x] = 1

    dy = [0,0,1,-1]
    dx = [1,-1,0,0]

    while q:
        y,x = q.popleft()

        for d in range(4):
            ny = y+dy[d]
            nx = x+dx[d]

            # 공주에게 직접가는 방법
            if 1<=ny<n+1 and 1<=nx<m+1 and grid[ny][nx]!=1 and visited[ny][nx] == 0 and status == 1:
                if grid[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1

                    return visited[ny][nx]-1

                visited[ny][nx] = visited[y][x] + 1
                q.append((ny,nx))

            # 소드를 들고 가는 방법
            if 1<=ny<n+1 and 1<=nx<m+1 and grid[ny][nx]!=1 and visited[ny][nx] == 0 and status == 2:
                if grid[ny][nx] == 2:
                    visited[ny][nx] = visited[y][x] + 1
                    StoP = abs(ny-n)+abs(nx-m)

                    return visited[ny][nx] + StoP -1
                    
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny,nx))

    return 1e9

n,m,limited = map(int,input().split())
grid = [[1]*(m+1)]+[[1]+list(map(int, input().split())) for _ in range(n)]
grid[n][m] = -1

mnt = 1e9
for i in range(1,3):
    t = bfs(1,1,i)
    if mnt > t:
        mnt = t

if mnt > limited:
    print('Fail')
else:
    print(mnt)