import sys
sys.stdin = open("sample_input (2).txt")

T = int(input())

for tc in range(1,T+1):
    A , B = map(str,input().split())

    cnt = 0
    start_n = 0
    typing = ''
    for i in range(len(A)):
        if typing != A :
            if A[start_n:start_n+len(B)] != B:
                typing += A[start_n]
                start_n += 1
                cnt += 1
            else:
                typing += B
                start_n += len(B)
                cnt += 1
        else:
            break
    print(f'#{tc} {cnt}')
