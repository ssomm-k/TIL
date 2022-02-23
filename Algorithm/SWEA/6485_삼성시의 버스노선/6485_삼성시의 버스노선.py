import sys
sys.stdin = open("s_input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    P = int(input())
    c_arr = [int(input()) for _ in range(P)]

    bus_N = {}

    # bus_N 딕셔너리에 각 버스정류장에 버스 노선이 몇개인지 넣어준다.
    for i in range(len(arr)):
        # arr에 들어있는 순서들중 항상 0번째는 Ai 1번째는 Bi 값이다.
        for j in range(arr[i][0],arr[i][1]+1):
            if j not in bus_N.keys():
                bus_N[j] = 1
            else:
                bus_N[j] = bus_N[j] + 1

    print(f'#{tc}',end=" ")
    for i in c_arr:
        print(bus_N.get(i,0) , end=" ")
