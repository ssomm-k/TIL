import sys
sys.stdin = open("sample_input(2) (1).txt")

T = int(input())

def binarySearch(N,key):
    start = 1
    end = N
    cnt = 0
    while start <= end :
        middle = (start + end)//2
        if middle == key:
            return cnt
        elif middle < key :
            start = middle
            cnt += 1
        else:
            end = middle
            cnt += 1
    return print('실패')

for tc in range(1,T+1):
    P , A , B = map(int,input().split())

    cnt_A = binarySearch(P,A)
    cnt_B = binarySearch(P,B)

    if cnt_B < cnt_A :
        print(f'#{tc} B')
    elif cnt_A < cnt_B :
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')