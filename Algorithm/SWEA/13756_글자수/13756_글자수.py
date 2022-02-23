import sys
sys.stdin = open("sample_input(2) (2).txt")

T = int(input())

for tc in range(1,T+1):
    str1 = list(input())
    str2 = list(input())

    count_str = {}
    for i in range(len(str1)):
        if str1[i] not in count_str.keys():
            count_str[str1[i]] = 0

    cnt = 0
    for i in range(len(str2)):
        for j in count_str.keys():
            if str2[i] == j:
                count_str[j] = count_str[j] + 1
                break
        else:
            cnt += 1

    maxV = 0
    for i in count_str.values():
        if maxV<i:
            maxV = i
    print(f'#{tc} {maxV}')