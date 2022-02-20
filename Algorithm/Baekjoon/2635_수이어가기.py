# 시작하는 수를 입력 받는다.
start_n = int(input())

# 최대 개수
maxV = 0
# # 최대 개수일때, 숫자 배열
# max_arr = []

for i in range(start_n,0,-1):
    arr = [start_n,i]
    n1 = start_n
    n2 = i
    n3 = n1 - n2
    while n3 >= 0:
        arr.append(n3)
        n1 = n2
        n2 = n3
        n3 = n1-n2
    cnt = len(arr)
    if maxV < cnt:
        maxV = cnt
        max_arr = arr

print(maxV)
for i in max_arr:
    print(i,end=' ')

# for i in range(start_n-1,-1,-1):
#     arr = [start_n,i]
#     for j in range(i):
#         if arr[-2]-arr[-1] >= 0 :
#             minus_k = arr[-2]-arr[-1]
#             arr.append(minus_k)
#         else:
#             break
#     print(arr)
#     cnt = len(arr)
#     if maxV < cnt:
#         maxV = cnt
#         max_arr = arr

# print(maxV)
# for i in max_arr:
#     print(i,end=' ')