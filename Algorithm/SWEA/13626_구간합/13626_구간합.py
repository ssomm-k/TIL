import sys
sys.stdin = open("sample_input(1).txt")

T = int(input())

for tc in range(1,T+1):
    N , M = map(int,input().split())
    arr = list(map(int,input().split()))
    # N개의 정수를 M개씩 더하기
    sum_arr = []
    for i in range(N-M+1):
        sumV = 0
        for j in range(i,i+M):
            sumV += arr[j]
        sum_arr.append(sumV)
    #최대값과 최소값의 차이 구하기
    minV = sum_arr[0]
    maxV = sum_arr[0]
    for k in range(len(sum_arr)):
        if minV > sum_arr[k]:
            minV = sum_arr[k]
        elif maxV < sum_arr[k]:
            maxV = sum_arr[k]
    # 출력
    print(f'#{tc} {maxV-minV}')