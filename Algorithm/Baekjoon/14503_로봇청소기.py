# 0:북 1:동 2:남 3:서 -> 위오아왼
N,M = map(int,input().split())
r,c,d = map(int,input().split())
cleaning = [list(map(int,input().split())) for _ in range(N)]

# 델타
delta = [[-1,0],[0,1],[1,0],[0,-1]]
