from collections import deque
'''
0을 기준으로 치즈를 찾아야됨
1. 0에서 상하좌우를 살펴 0인 좌표는 deque에 넣고 1인 좌표는 공기와 맡다은 치즈이므로 lose_cheese에 넣는다.
2. 더이상 방분할 곳이 없으면 공기와 맡다은 치즈를 0으로 바꿔주고 방문기록을 초기화한다.
'''
def bfs(i,j):
    # 방문 기록
    visited = [[0]*galo for _ in range(selo)]
    # 0인 좌표 모을 덱큐
    zero_q = deque([])
    # 입력받은 i,j로 탐색 시작좌표 생성
    zero_q.append([i,j])
    # 방문기록 남기기
    visited[i][j] = 1

    # 델타
    di=[0,1,0,-1]
    dj=[1,0,-1,0]

    while zero_q:
        y,x = zero_q.popleft()
        for i in range(4):
            dy = y + di[i]
            dx = x + dj[i]
            if 0<=dy<selo and 0<=dx<galo:
                # 방문기록이 없는 곳 중에
                if not visited[dy][dx]:
                    # 치즈이면
                    if cheese[dy][dx]:
                        # 녹여주고 방문기록을 남긴다.
                        cheese[dy][dx] = 0
                        visited[dy][dx] = 1
                    # 치즈가 아니면
                    else : 
                        # 방문기록을 남기고 0인 좌표를 모으는 곳에 좌표를 넣어준다.
                        visited[dy][dx] = 1
                        zero_q.append([dy,dx])

selo,galo = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(selo)]

# 만들어둔 bfs함수를 치즈가 다 녹을때까지 실행한다.
time = 0
last_cheese = 0
for _ in range(selo*galo):
    # cheese의 수를 계산함.
    cheese_cnt = 0
    for i in cheese:
        cheese_cnt += sum(i)
    
    # cheese가 다 녹으면 멈춘다.
    if not cheese_cnt:
        break

    else:
        bfs(0,0)
        time += 1
        last_cheese = cheese_cnt

print(time)
print(last_cheese)