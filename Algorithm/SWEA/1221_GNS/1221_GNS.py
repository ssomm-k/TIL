import sys
sys.stdin = open("GNS_test_input.txt")

T = int(input())

for tc in range(1,T+1):
    case_N = list(input().split())
    case_N[1] = int(case_N[1])
    arr = list(map(str,input().split()))

    sort_list = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4,
                 "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}

    count_arr = [0]*10
    sort_arr = [0]*case_N[1]
    for i in range(case_N[1]):
        count_arr[sort_list[arr[i]]] += 1
    for i in range(1,10):
        count_arr[i] += count_arr[i-1]
    for i in range(case_N[1]-1,-1,-1):
        count_arr[sort_list[arr[i]]] -= 1
        sort_arr[count_arr[sort_list[arr[i]]]] = arr[i]

    print(f'#{tc}')
    for i in sort_arr:
        print(i,end=' ')
    print()