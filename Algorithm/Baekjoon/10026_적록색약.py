from collections import deque

# 적록색약이 아닌 사람이 본 경우
def bfs_no():
    # 오->아->왼->위
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    while start_color:

        y,x = start_color.popleft()

        for i in range(4):

# 적록색약인 사람이 본 경우
def bfs_yes():
    # 오->아->왼->위
    di = [0,1,0,-1]
    dj = [1,0,-1,0]


N = int(input())
color = [list(map(str,input())) for _ in range(N)]

start_color = deque([])
