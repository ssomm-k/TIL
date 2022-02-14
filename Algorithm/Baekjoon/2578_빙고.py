bingo_game = [list(map(int,input().split())) for _ in range(5)]
bingo_X = [list(map(int,input().split())) for _ in range(5)]
call_X = sum(bingo_X , [])

call_cnt = 0

for call in call_X:
    line_cnt = 0
    # 사회자가 부른 call이 있는 위치를 찾아서 0으로 바꾸기
    for i in range(5):
        for j in range(5):
            if bingo_game[i][j] == call:
                bingo_game[i][j] = 0
            else:pass
    #가로줄이 지워졌는지 확인
    for i in range(5):
        row_sum = 0
        for j in range(5):
            row_sum += bingo_game[i][j]
        if row_sum == 0 :
            line_cnt += 1
    #세로줄이 지워졌는지 확인
    for i in range(5):
        col_sum = 0
        for j in range(5):
            col_sum += bingo_game[j][i]
        if col_sum == 0 :
            line_cnt += 1
    #대각선이 지워졌는지 확인
    dae1_sum = 0
    for i in range(5):
        dae1_sum += bingo_game[i][i]
    if dae1_sum == 0 :
        line_cnt += 1
    dae2_sum = 0
    for i in range(5):
        dae2_sum += bingo_game[i][-i-1]
    if dae2_sum == 0 :
        line_cnt += 1
    call_cnt += 1
    if line_cnt >= 3:
        print(call_cnt)
        break
# for i in range(5):
#     for j in range(5):
#         if bingo_game[i][j] == 11 :
#             print(i,j)

# cnt = 0 
# for i in range(5):
#     call_x = 0
#     for j in range(5):
#         call_x = bingo_X[i][j]

# cnt = 0
# for call in call_X : 
#     for i in range(5):
#         for j in range(5):
#             if bingo_game[i][j] == call :
#                 bingo_game[i][j] = 0
# if 13 in bingo_game[1] :
#     idx = bingo_game[1].index(13)
#     bingo_game[1][idx] = 0
# print(bingo_game)