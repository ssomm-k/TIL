import sys
sys.stdin = open("sample_input(1) (2).txt")

T = int(input())

for tc in range(1,T+1):
    N , M = map(int,input().split())
    str_arr = [list(map(str,input())) for _ in range(N)]

    find_M = []
    for i in range(N):
        if N != M :
            for j in range(N-M+1):
                for k in range(M//2):
                    if str_arr[i][k+j] != str_arr[i][-N + M - 1+j]:
                        del (find_M[::])
                    else:
                        find_M.insert(k,str_arr[i][k+j])
                        find_M.insert(k+1,str_arr[i][k+j])
                else:
                    if not find_M:
                        for j in range(N - M + 1):
                            for k in range(M // 2):
                                if str_arr[k + j][i] != str_arr[-N + M - 1+j][i]:
                                    del (find_M[::])
                                else:
                                    find_M.insert(k, str_arr[i][k + j])
                                    find_M.insert(k + 1, str_arr[i][k + j])
        else:
            for j in range(M//2):
                if str_arr[i][j] != str_arr[i][-j-1]:
                    del(find_M[::])
                else:
                    find_M.insert(j,str_arr[i][j])
                    find_M.insert(j+1, str_arr[i][j])
            else:
                if not find_M:
                    for j in range(M // 2):
                        if str_arr[j][i] != str_arr[-j-1][i]:
                            del (find_M[::])
                        else:
                            find_M.insert(j, str_arr[j][i])
                            find_M.insert(j + 1, str_arr[j][i])
            print(find_M)