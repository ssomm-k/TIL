import sys
sys.stdin = open("input (9).txt")

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    pari = [list(map(int,input().split())) for _ in range(N)]

    max_pari = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_pari = 0
            for m_i in range(i,M+i):
                for m_j in range(j,M+j):
                    sum_pari+=pari[m_i][m_j]
            if max_pari < sum_pari:
                max_pari = sum_pari
    print(f'#{tc} {max_pari}')