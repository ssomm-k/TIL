import sys

n = int(sys.stdin.readline().strip())

n_arr = []
pm_arr = []
check = 1
input_n = 1

for i in range(n):
    num = int(sys.stdin.readline().strip())
    while input_n <= num:
        n_arr.append(input_n)
        pm_arr.append('+')
        input_n += 1
    if n_arr[-1] == num:
        n_arr.pop()
        pm_arr.append('-')
    else:
        print("NO")
        check = 0
        break
if check:
    for i in pm_arr:
        print(i)

# for i in range(n):
#     num = int(sys.stdin.readline().strip())
#     for j in range(1,num+1):
#         if cnt < j :
#             n_arr.append(j)
#             pm_arr.append('+')
#             cnt += 1
#     if n_arr[-1] == num:
#         n_arr.pop()
#         pm_arr.append('-')
#     else:
#         print("NO")
#         cnt = 0
#         break
# if cnt:
#     for i in pm_arr:
#         print(i)