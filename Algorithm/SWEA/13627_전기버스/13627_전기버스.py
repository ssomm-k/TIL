import sys
sys.stdin = open("sample_input(2).txt")

T = int(input())

for tc in range(1,T+1):
    K , N , M = map(int,input().split())
    arr = list(map(int,input().split()))
    cnt_electric = [0] * (N+1)
    for i in range(len(arr)):
        cnt_electric[arr[i]] += 1
    stop_i = 0
    counts = 0
    for a in range(N):
        if stop_i + K >= N:
            break
        for j in range(stop_i + K, stop_i, -1):
            if cnt_electric[j]:
                stop_i = j
                counts += 1
                break
            else:
                pass
        else:
            counts=0
            break
    print(f'#{tc} {counts}')
