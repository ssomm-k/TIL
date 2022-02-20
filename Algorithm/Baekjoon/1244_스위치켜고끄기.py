# 스위치 수
switch_n = int(input())
# 스위치 상태
switch_arr = list(map(int,input().split()))
# 학생수
students_n = int(input())

for i in range(students_n):
    # 학생성별 , 학생이 받은 수
    F_or_M , num = map(int,input().split())
    
    # 성별이 남자일때, 받은 수의 배수를 변경
    if F_or_M == 1 :
        # change : 받은 번호의 배수자리
        for change in range(num,switch_n+1,num):
            # 1이면 0으로
            if switch_arr[change-1]:
                switch_arr[change-1]=0
            # 0이면 1으로
            else:
                switch_arr[change-1]=1
    # 성별이 여자일때, 번호 기준 최대로 긴 좌우대칭을 찾아 모두 변경
    else:
        i = 0
        while num+i-1< switch_n and num-i-1>=0:
            if switch_arr[num+i-1] == switch_arr[num-i-1]:
                if switch_arr[num+i-1] and switch_arr[num-i-1] :
                    switch_arr[num+i-1] = switch_arr[num-i-1] = 0
                else:
                    switch_arr[num+i-1] = switch_arr[num-i-1] = 1
                i += 1
            else:
                break

for i in range(0,switch_n,20):
    print(*switch_arr[i:i+20])