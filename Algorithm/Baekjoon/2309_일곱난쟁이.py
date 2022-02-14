nanjangee = []
for i in range(9):
    nan = int(input())
    nanjangee.append(nan)

n = len(nanjangee)

find_nan = []
for i in range(1<<n):
    tmp_set = []
    find_nan_sum = 0
    for j in range(n):
        if i & (1<<j):
            tmp_set.append(nanjangee[j])
            find_nan_sum += nanjangee[j]
    if len(tmp_set) == 7 and sum(tmp_set) == 100 :
        find_nan.append(tmp_set)
find_nan[0].sort()
for nanjang in find_nan[0]:
    print(nanjang)

# 연습코드1 --> 실패
# if sum(nanjangee[0:7]) != 100:
#     for j in range(7):
#         a = nanjangee.pop(1)
#         nanjangee.insert(8,a)
#         if sum(nanjangee[0:7]) == 100 :
#             sort_nan = sorted(nanjangee[0:7])
#             for k in sort_nan:
#                 print(k)
#             break
# else :
#     sort_nan = sorted(nanjangee[0:7])
#     for h in sort_nan:
#         print(h)