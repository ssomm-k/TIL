import sys
sys.stdin = open("sample_input (5).txt")

T = int(input())

for tc in range(1,T+1):
    # N이 1->1 / 2->3 / 3->5 / 4->11 / 5->21
    # 규칙은 (N의경우의수) = (N-1경우의수) + (N-2경의우수)*2
    N = int(input())//10
    count_arr = [0]*N
    count_arr[0] = 1
    count_arr[1] = 3

    for i in range(2,N):
        count_arr[i] = count_arr[i-1] + count_arr[i-2]*2

    print(f'#{tc} {count_arr[N-1]}')