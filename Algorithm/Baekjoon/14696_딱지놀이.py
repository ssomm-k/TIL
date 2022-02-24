Round_N = int(input())

for _ in range(Round_N):
    input_arr_A = list(map(int,input().split()))
    pattern_arr_A = input_arr_A[1:]
    input_arr_B = list(map(int,input().split()))
    pattern_arr_B = input_arr_B[1:]

    cnt_4_A = 0
    cnt_3_A = 0
    cnt_2_A = 0
    cnt_1_A = 0
    for i in range(input_arr_A[0]):
        if pattern_arr_A[i] == 4:
            cnt_4_A += 1
        elif pattern_arr_A[i] == 3:
            cnt_3_A += 1
        elif pattern_arr_A[i] == 2:
            cnt_2_A += 1
        elif pattern_arr_A[i] == 1:
            cnt_1_A += 1

    cnt_4_B = 0
    cnt_3_B = 0
    cnt_2_B = 0
    cnt_1_B = 0
    for i in range(input_arr_B[0]):
        if pattern_arr_B[i] == 4:
            cnt_4_B += 1
        elif pattern_arr_B[i] == 3:
            cnt_3_B += 1
        elif pattern_arr_B[i] == 2:
            cnt_2_B += 1
        elif pattern_arr_B[i] == 1:
            cnt_1_B += 1
    
    if cnt_4_A > cnt_4_B:
        print("A")
    elif cnt_4_B > cnt_4_A:
        print("B")
    elif cnt_4_A == cnt_4_B:
        if cnt_3_A > cnt_3_B:
            print("A")
        elif cnt_3_B > cnt_3_A:
            print("B")
        elif cnt_3_A == cnt_3_B:
            if cnt_2_A > cnt_2_B:
                print("A")
            elif cnt_2_B > cnt_2_A:
                print("B")
            elif cnt_2_A == cnt_2_B:
                if cnt_1_A > cnt_1_B:
                    print("A")
                elif cnt_1_B > cnt_1_A:
                    print("B")
                elif cnt_1_A == cnt_1_B:
                    print("D")
