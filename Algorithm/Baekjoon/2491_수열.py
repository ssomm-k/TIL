N = int(input())
arr = list(map(int,input().split()))
# 최대값 저장
maxV = 1

# 커지는 버전
cnt_p = 1
for i in range(1,N):
    # 현재숫자가 이전 숫자보다 크거나 같으면 카운트를 증가시킨다.
    if arr[i-1] <= arr[i]:
        cnt_p += 1
        # 이때 maxV가 카운트 보다 작으면 값을 변경한다.
        if maxV < cnt_p:
            maxV = cnt_p
    # 현재숫자가 다음숫자보다 작으면 카운트를 초기화한다.
    else:
        cnt_p = 1

# 작아지는 버전
cnt_m = 1
for i in range(1,N):
    # 현재숫자가 이전 숫자보다 작거나 같으면 카운트를 증가시킨다.
    if arr[i-1] >= arr[i]:
        cnt_m += 1
        # 이때 maxV가 카운트 보다 작으면 값을 변경한다.
        if maxV < cnt_m:
            maxV = cnt_m
    # 현재숫자가 다음숫자보다 크면 카운트를 초기화한다.
    else:
        cnt_m = 1

print(maxV)

# # 커지는 버전
# cnt_p = 1
# for i in range(N-1):
#     # 현재숫자가 다음숫자보다 작거나 같으면 카운트를 증가시킨다.
#     if arr[i] <= arr[i+1]:
#         cnt_p += 1
#         # 이때 maxV가 카운트 보다 작으면 값을 변경한다.
#         if maxV < cnt_p:
#             maxV = cnt_p
#     # 현재숫자가 다음숫자보다 크면 카운트를 초기화한다.
#     else:
#         cnt_p = 1

# # 작아지는 버전
# cnt_m = 1
# for i in range(N-1):
#     # 현재숫자가 다음숫자보다 크거나 같으면 카운트를 증가시킨다.
#     if arr[i] >= arr[i+1]:
#         cnt_m += 1
#         # 이때 maxV가 카운트 보다 작으면 값을 변경한다.
#         if maxV < cnt_m:
#             maxV = cnt_m
#     # 현재숫자가 다음숫자보다 작으면 카운트를 초기화한다.
#     else:
#         cnt_m = 1

# print(maxV)

# 완전탐색으로 수열의 최대길이 찾기 - 커지는 버전
# for i in range(N-1):
#     x_arr = []
#     x_arr.append(arr[i])
#     for j in range(N-i-1):
#         if x_arr[-1] <= arr[j+i+1]:
#             x_arr.append(arr[j+i+1])
#         else:
#             if maxV < len(x_arr):
#                 maxV = len(x_arr)
#             break
        
# 완전탐색으로 수열의 최대길이 찾기 - 작아지는 버전
# for i in range(N-1):
#     x_arr = []
#     x_arr.append(arr[i])
#     for j in range(N-i-1):
#         if x_arr[-1] >= arr[j+i+1]:
#             x_arr.append(arr[j+i+1])
#         else:
#             if maxV < len(x_arr):
#                 maxV = len(x_arr)
#             break
