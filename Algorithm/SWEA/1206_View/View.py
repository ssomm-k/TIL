import sys
sys.stdin = open("input.txt")
T = 10

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    #조망권 구하기
    for i in range(2,N-2):
        maxV = 0
        for j in range(i-2,i+3):
            if j != i and maxV < arr[j]:
                maxV = arr[j]
        result = arr[i] - maxV
        if result > 0 :
            cnt += result
    print(f'#{tc} {cnt}')