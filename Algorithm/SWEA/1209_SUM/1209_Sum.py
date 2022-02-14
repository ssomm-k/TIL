import sys
sys.stdin = open("input (6).txt")

T = 10

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    maxV = 0
    dae1_sum = 0
    dae2_sum = 0
    for i in range(100):
        row_sum = 0
        col_sum = 0

        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
            if col_sum < row_sum and maxV < row_sum:
                maxV = row_sum
            elif row_sum < col_sum and maxV < col_sum:
                maxV = col_sum
        dae1_sum += arr[i][i]
        dae2_sum += arr[i][-i-1]

    if dae1_sum < dae2_sum and maxV < dae2_sum:
        maxV = dae2_sum
    elif dae2_sum < dae1_sum and maxV < dae1_sum:
        maxV = dae1_sum

    print(f'#{tc} {maxV}')