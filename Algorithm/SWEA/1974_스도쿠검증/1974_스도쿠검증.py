import sys
sys.stdin = open("input (12).txt")

T = int(input())

for tc in range(1,T+1):
    # 스도쿠판 가져오기
    arr = [list(map(int,input().split())) for _ in range(9)]

    # 정답
    result = 1

    # 가로로 검사하는 줄의 합이 45면 검증성공
    cnt_row = 0
    # 가로로 검사
    for i in range(9):
        for j in range(9):
            cnt_row += arr[i][j]
        if cnt_row != 45:
            result = 0
            break
        else:
            cnt_row = 0

    # 세로로 검사하는 줄의 합이 45면 검증성공
    cnt_col = 0
    # 세로로 검사
    for i in range(9):
        for j in range(9):
            cnt_col += arr[j][i]
        if cnt_col != 45:
            result = 0
            break
        else:
            cnt_col= 0

    # 3*3 검사 합이 45명 검증성공
    cnt_box = 0
    # 3*3 검사
    for i in range(0,9,3):
        for j in range(0,9,3):
            for k in range(3):
                cnt_box += sum(arr[i+k][j:j+3])
            if cnt_box != 45:
                result =0
                break
            else:
                cnt_box = 0

    # 출력
    print(f'#{tc} {result}')