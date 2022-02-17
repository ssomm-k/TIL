# n = int(input())

# arr = [0]*n
# i = 1
# while i <= n:
#     arr[i-1] = int(input())
#     i+=1

# arr =[4, 3, 6, 8, 7, 5, 2, 1]
arr = [1,2,5,3,4]
n = len(arr)

n_arr = []
pm_arr = []
# pop_arr = []
cnt = 0

for i in arr:
    for j in range(1,i+1):
        if cnt < j and j not in n_arr:
            n_arr.append(j)
            pm_arr.append('+')
            cnt += 1
        # if j not in pop_arr and j not in n_arr:
        #     n_arr.append(j)
        #     pm_arr.append('+')
    else:
        if len(n_arr) != 0 and n_arr[-1] == i:
            pop_num = n_arr.pop()
            # pop_arr.append(pop_num)
            pm_arr.append('-')
        else:
            print("NO")
            break
else:
    for i in pm_arr:
        print(i)