from unittest.util import sorted_list_difference


nanjangee = []
for i in range(9):
    nan = int(input())
    nanjangee.append(nan)

if sum(nanjangee[0:7]) != 100:
    for j in range(7):
        a = nanjangee.pop(1)
        nanjangee.insert(8,a)
        if sum(nanjangee[0:7]) == 100 :
            sort_nan = sorted(nanjangee[0:7])
            for k in sort_nan:
                print(k)
            break
else :
    sort_nan = sorted(nanjangee[0:7])
    for h in sort_nan:
        print(h)