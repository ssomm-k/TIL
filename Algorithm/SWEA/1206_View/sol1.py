N=6
arr1 = [2,7,2,5,4,6]
arr = [2,7,4,5,4,7]
# Q1. 최대값찾기
# maxV = 0
# for i in range(N):
#     if maxV < arr[i]:
#         maxV = arr[i]
# print(maxV)
#Q2. 최대값의 자리수 찾기
maxIdx = 0
for i in range(N):
    if arr1[maxIdx] > arr1[i]:
        maxIdx = i
print(maxIdx)
#maxIdx = 0
#maxIdx_list = []
#for i in range(N):
#    if arr[maxIdx] <= arr[i]:
#       maxIdx = i
       #maxIdx_list.append(maxIdx)
#print(maxIdx)