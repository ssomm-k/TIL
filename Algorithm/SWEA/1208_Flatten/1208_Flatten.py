import sys
sys.stdin = open("input (1).txt")

T = 10

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    for i in range(N):
        minV , min_idx = arr[0] , 0
        maxV , max_idx = arr[0] , 0
        for j in range(100):
            if minV > arr[j]:
                minV = arr[j]
                min_idx = j
            elif maxV < arr[j]:
                maxV = arr[j]
                max_idx = j
        arr[min_idx] += 1
        arr[max_idx] -= 1
    minV2 , maxV2 = arr[0] , arr[0]
    for k in range(100):
        if minV2 > arr[k]:
            minV2 = arr[k]
        elif maxV2 < arr[k]:
            maxV2 = arr[k]
    print(f'#{tc} {maxV2 - minV2}')
