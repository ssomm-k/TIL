import sys
sys.stdin = open("test_input.txt" , encoding="utf-8")

T = 10

# p : pattern / t : text
def BrBruteForce(p,t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    n = len(t)
    m = len(p)
    success_ls = [] # pattern과 일치하는 경우 시작 인덱스를 append함

    for i in range(n-m+1):
        for j in range(m):
            if t[i+j] != p[j]:
                break
        else:
            success_ls.append(i)
    return len(success_ls)

for tc in range(1,T+1):
    tc_N = int(input())
    p = input()
    t = input()

    print(f'#{tc_N} {BrBruteForce(p,t)}')