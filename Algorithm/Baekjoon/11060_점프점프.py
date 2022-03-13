# bfs
'''
현재 내 좌표에서 갈 수 있는 곳들을 방문하면서 dist배열을 채워줍니다 
만약 현재 좌표가 미로의 도착지점이라면 도착을 한거니까 거기서 while문을 빠져나옵니다
'''
from collections import deque
n = int(input())
miro = list(map(int, input().split()))

q = deque()
q.append(0)
dist = [0]*n
dist[0] = 1

while q:
    now_idx = q.popleft()
    if now_idx == n-1:
        break

    for next_idx in range(now_idx+1, now_idx+miro[now_idx]+1):
        if next_idx >= n or dist[next_idx]:
            continue
        dist[next_idx] = dist[now_idx]+1
        q.append(next_idx)

if dist[n-1] == 1e9:
    print(-1)
else:
    print(dist[n-1]-1)