N = int(input())
tornado = [list(map(int,input().split())) for _ in range(N)]
y = x = N//2

# 왼 -> 아 -> 오 -> 위
di = [0,1,0,-1]
dj = [-1,0,1,0]

d_len = 1
d = -1
cnt = 1
out = 0
while 0<=y<N and 0<=x<N:
    d += 1
    d_len = d // 2 + 1
    if x == -1:
        break
    for _ in range(d_len):
        dy = y + di[d%4]
        dx = x + dj[d%4]
        if dx == -1:
            x = dx
            break

        now = tornado[dy][dx]
        
        for k in [1,-1]:
            d2y = dy + di[(d+k)%4]
            d2x = dx + dj[(d+k)%4]

            if 0<=d2y<N and 0<=d2x<N:
                tornado[d2y][d2x] += int(now * 0.07)
            else:
                out += int(now*0.07)
        y = dy
        x = dx

from pprint import pprint
pprint(tornado)