import sys
sys.stdin = open("input (8).txt")

T = 10

def find_row(n,list_x):
    r_maxV=0
    # i : 행의 인덱스 / 총 i(행)의 범위는 0-99까지이다.
    for i in range(n):
        # j : 회문의 길이
        for j in range(1,n+1):
            # k : 회문을 찾는 시작 인덱스
            for k in range(n-j+1):
                find_row_m = list_x[i][k:k+j]
                if find_row_m[::] == find_row_m[::-1] and r_maxV < len(find_row_m):
                    r_maxV = len(find_row_m)
    return r_maxV

def find_col(n,list_x):
    # list_x를 전치행렬을한다.
    for i in range(n):
        for j in range(n):
            if i < j :
                list_x[i][j] , list_x[j][i] = list_x[j][i] , list_x[i][j]
    c_maxV = 0
    for i in range(n):
        for j in range(1, n + 1):
            for k in range(n - j+1):
                find_row_m = list_x[i][k:k + j]
                if find_row_m[::] == find_row_m[::-1] and c_maxV < len(find_row_m):
                    c_maxV = len(find_row_m)
    return c_maxV


for tc in range(1,T+1):
    tc_n = int(input())
    arr = [list(map(str,input())) for _ in range(100)]

    row_max = find_row(100,arr)
    col_max = find_col(100,arr)

    if row_max < col_max:
        print(f'#{tc} {col_max}')
    else:
        print(f'#{tc} {row_max}')