import sys
sys.stdin = open("1 (1).txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    minV = arr[0]
    maxV = arr[0]
    for i in range(len(arr)):
        if maxV < arr[i]:
            maxV = arr[i]
        elif minV > arr[i]:
            minV = arr[i]
    print(f'#{tc} {maxV-minV}')