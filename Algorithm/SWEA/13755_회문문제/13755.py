import sys
sys.stdin = open("sample_input(1) (2).txt")

T = int(input())

def find_m_row(n,m,list_x):
    for i in range(n):
        for j in range(n-m+1):
            find_M_row = list_x[i][j:j+m]
        if find_M_row[::] == find_M_row[::-1]:
            return find_M_row

def find_m_col(n,m,list_x):
    for i in range(n):
        for k in range(n-m+1):
            find_M_col = []
            for j in range(m):
                find_M_col.append(list_x[j+k][i])
            if find_M_col[::] == find_M_col[::-1]:
                return find_M_col


for tc in range(1,T+1):
    N , M = map(int,input().split())
    str_arr = [list(map(str,input())) for _ in range(N)]

    row_m = find_m_row(N,M,str_arr)
    col_m = find_m_col(N, M, str_arr)

    if row_m:
        print(f'#{tc} ',end='')
        for i in row_m:
            print(i,end='')
        print()
    elif col_m:
        print(f'#{tc} ',end='')
        for i in col_m:
            print(i,end='')
        print()