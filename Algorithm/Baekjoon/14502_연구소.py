from collections import deque
import copy
import sys

input = sys.stdin.readline

def wall(x):
    if x ==3:
        # bfs함수 실행
        bfs()
        return
    
    # 벽 3개 세우기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(x+1)
                arr[i][j] = 0
        
def bfs():
    global result
    copy_arr = copy.deepcopy(arr)

    for i in range(N):
        for j in range(M):
            if copy_arr[i][j] == 2:
                virus.append([i,j])
    
    # 델타
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    # 바이러스 퍼트리기
    while virus:
        y,x = virus.popleft()
        for i in range(4):
            dy = y + di[i]
            dx = x + dj[i]
            if 0<=dy<N and 0<=dx<M :
                if not copy_arr[dy][dx]:
                    copy_arr[dy][dx] = 2
                    virus.append([dy,dx])
    
    # 안전구역 탐색하기
    cnt = 0
    for i in copy_arr:
        cnt += i.count(0)
    result = max(result,cnt)

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
result = 0
# 바이러스 위치
virus = deque()

wall(0)
print(result)