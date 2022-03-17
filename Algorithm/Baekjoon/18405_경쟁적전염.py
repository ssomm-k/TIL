from collections import deque
# N : 배열의 크기 K : 바이러스의 수 S : 초 (X,Y) : 확인위치

# 바이러스 전파함수 : 진행되는 초를 받음
def virus_junpa(second):
    virus_q = deque(virus_idx)

    # 델타
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    # 값이 작은 바이러스부터 퍼질 수 있는 곳을 찾음
    while virus_q:
        # 바이러스번호,행번호,열번호,흘러간초
        virus_num,y,x,s = virus_q.popleft()

        # 흘러간 시간이 초기에 진행해야하는 시간과 같으면 멈춤
        if s == second:
            return

        # 바이러스가 퍼질 수 있는 곳을 찾음
        for i in range(4):
            dy = y + di[i]
            dx = x + dj[i]
            if 0<=dy<N and 0<=dx<N:
                # 바이러스가 없는 곳이라면
                if not virus[dy][dx]:
                    # 위치를 저장하고 시간을 1초 늘린다
                    virus_q.append([virus_num,dy,dx,s+1])
                    virus[dy][dx] = virus_num

# 입력
N,K = map(int,input().split())
virus = [list(map(int,input().split())) for _ in range(N)]
S,X,Y = map(int,input().split())

# 초기 바이러스 위치 모음집
virus_idx = []
# 바이러스 위치 찾기
for i in range(N):
    for j in range(N):
        # 값이 0 이 아니면 바이러스
        if virus[i][j] != 0:
            # 바이러스번호, 위치_행, 위치_열, 초
            virus_idx.append([virus[i][j],i,j,0])

# 바이러스의 숫자가 작은 것부터 퍼저야하므로 정렬해줌
virus_idx.sort()

# 바이러스가 퍼지는 함수 호출
virus_junpa(S)

# 결과 출력
print(virus[X-1][Y-1])