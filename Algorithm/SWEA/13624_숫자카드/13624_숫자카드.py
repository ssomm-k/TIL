import sys
sys.stdin = open('1.txt')

T = int(input())

for tc in range(1,T+1):
    N =  int(input())
    arr =  list(map(int,input()))
    #0-9까지 0으로 채워진 리스트를 생성
    cnt_arr = [0] * 10
    #arr에 입력된 카드를 카운팅함
    for i in range(len(arr)):
        cnt_arr[arr[i]] += 1

    maxIdx = 0
    for j in range(10):
        if cnt_arr[maxIdx] <= cnt_arr[j]:
            maxIdx = j
    print(f'#{tc} {maxIdx} {cnt_arr[maxIdx]}')
