import sys
sys.stdin = open("sample_input(1) (1).txt")

T = int(input())

for tc in range(1,T+1):
    N , K = map(int,input().split())

    arr = list(range(1,13))

    cnt_sum = 0
    for i in range(1<<12) :
        tmp_set = []
        for j in range(12):
            if i &(1<<j):
                tmp_set.append(arr[j])
        if len(tmp_set) == N and sum(tmp_set) == K :
            cnt_sum += 1
    print(f'#{tc} {cnt_sum}')