from collections import deque

# bfs 함수 : 익힐 수 있는 토마토를 모조리 익히는 함수
def bfs():
    # 익은 토마토 기준 오른쪽 -> 아래 -> 왼쪽 -> 위로 움직일 델타
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while red_tomato:
        # 익은 토마토 위치
        y,x = red_tomato.popleft()
        # 익을 토마토 찾기
        for i in range(4):
            dy = y + di[i]
            dx = x + dj[i]
            # 상자안에서 안익은토마토인 경우
            if 0<=dy<N and 0<=dx<M and (not tomato_arr[dy][dx]):
                # 처음에는 cnt를 사용하려고 했으나 어디에 사용해야할지 몰라서 아래 방법을 택함.
                # 해당 위치의 토마토를 익혔다는 표시로 이전 토마토의 값에 1을 더해준다.
                tomato_arr[dy][dx] = tomato_arr[y][x] + 1
                red_tomato.append([dy,dx])

# 상자의 가로,세로
M,N = map(int,input().split())

# 토마토상자
tomato_arr = [list(map(int,input().split())) for _ in range(N)]

# 익은 토마토 위치
red_tomato = deque([])

# 익은 토마토 위치 찾기
for i in range(N):
    for j in range(M):
        # 익은 토마토는 1로 입력됨
        if tomato_arr[i][j] == 1:
            red_tomato.append([i,j])

# 함수 호출
bfs()

cnt = 0
# 상자안에 토마토가 다 익었나 확인
for i in tomato_arr:
    # 안익은 토마토가 있으면 0 : 왜냐하면 마지막에서 -1 해줘야함. 이유는 아래에서
    if 0 in i:
        cnt = 0
        break
    # 여기에서 처음부터 다익은토마토인 경우는 cnt가 1이된다.
    else:
        cnt = max(cnt,max(i))

# -1을 하는 이유 : 값을 더할때 첫날 익어있는 토마토부터 1로 더해져서 최대로 오래걸린 기간에서 -1을 해줘야 총기간이 된다.
print(cnt-1)