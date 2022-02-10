K,N,M = 3,10,5
cnt = [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0]
stop_i = 0
counts = 0
for i in range(N):
    if stop_i + K >= N :
        break
    for j in range(stop_i+K,stop_i,-1):
        if cnt[j] :
            stop_i = j
            counts += 1
            break
    else:
        print(0)
        break
