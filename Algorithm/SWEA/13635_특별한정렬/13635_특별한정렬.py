import sys
sys.stdin = open("sample_input(3).txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    for i in range(0,N-1,2):
        minV = arr[i]
        maxV = arr[i]
        # i부터 끝까지 중에서 max값과 min값을 찾는다.
        for j in arr[i::]:
            if minV > j:
                minV = j
            elif maxV < j:
                maxV = j
        # 찾은 max값을 i자리에 넣어주고
        arr.insert(i,maxV)
        # i번째 이후 즉 i+1번째부터 끝까지 중에 max값이 있는 걸 지워준다.
        arr.pop(arr.index(maxV, i + 1, N + 1))
        # 찾은 min값을 i+1 즉 max값 다음 자리에 넣어주고
        arr.insert(i + 1, minV)
        # max값과 동일하게 넣어준 min값 이후부터 min값을 찾아 지워준다.
        arr.pop(arr.index(minV, i + 2, N + 1))

    # 원하는 결과와 같이 출력해준다.
    print(f'#{tc}',end=' ')
    for i in arr[0:10]:
        print(i,end=' ')
    print()