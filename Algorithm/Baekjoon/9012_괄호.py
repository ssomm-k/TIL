T = int(input())

Vps_list = []
i = 1
while i <= T:
    Vps_list.append(str(input()))
    i += 1

b = ['(',')']
for j in Vps_list:
    if j.count(b[0]) == j.count(b[1]):
        print('YES')
    else : print('NO')