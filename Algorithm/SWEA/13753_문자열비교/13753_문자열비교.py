import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())

for tc in range(1,T+1):
    str1_p = list(input())
    str2_t = list(input())

    cnt = 0
    for i in range(len(str2_t)):
        if str2_t[i:i+len(str1_p)] == str1_p[::]:
            cnt = 1

    # for i in range(len(str2_t)):
    #     for j in range(len(str1_p)):
    #         if str2_t[i+j] != str1_p[j]:
    #             break
    #     else:
    #         cnt = 1

    print(f'#{tc} {cnt}')