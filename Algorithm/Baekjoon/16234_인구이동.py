# bfs
'''
bfs를 통해서 동맹국들을 찾음, 동맹을 한 나라의 수 cnt, 총 인구수를 더한 값 sum_v를 반환
answer:며칠 지났는지 
isTrans:오늘 인구이동이 있었는지 판단, 만약 한 나라라도 cnt의 개수가 2 이상이라면 인구이동이 일어났다고 판단
num: 동맹국들을 그룹핑하기 위한 카운팅 숫자 ex) 첫번째 동맹국들은 temp에 모두 0으로 표시 두번쨰 동맹국들은 temp에 1로 표시 ...
'''

from collections import deque


def bfs(num, i, j):
    q = deque()
    q.append((i, j))

    cnt = 1
    sum_v = board[i][j]

    while q:
        y, x = q.popleft()

        for dy, dx in d:
            newy = y+dy
            newx = x+dx
            if newy >= n or newy < 0 or newx >= n or newx < 0 or temp[newy][newx] != -1:
                continue

            if l <= abs(board[newy][newx]-board[y][x]) <= r:
                temp[newy][newx] = num
                sum_v += board[newy][newx]
                cnt += 1
                q.append((newy, newx))

    return cnt, sum_v


n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]


answer = 0

isTrans = True

while isTrans:
    isTrans = False
    lis = []
    num = 0
    temp = [[-1]*n for _ in range(n)]

    # board를 순회돌면서 아직 동맹을 맺지 않은 나라면 bfs를 통해서 동맹국들을 찾아줌
    for i in range(n):
        for j in range(n):
            if temp[i][j] != -1:
                continue

            temp[i][j] = num
            cnt, sum_v = bfs(num, i, j)
            lis.append(sum_v//cnt)

            num += 1

            if cnt != 1:
                isTrans = True

    # 다시 board를 순회돌면서 인구수를 갱신
    for i in range(n):
        for j in range(n):
            board[i][j] = lis[temp[i][j]]

    # 날짜 카운팅
    answer += 1

print(answer-1)