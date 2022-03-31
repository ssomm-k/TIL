triangle = [list(map(int,input())) for _ in range(5)]
sum_tri = []

for i in triangle:
    sum_tri.append([0]*len(i))

for i in range(len(triangle)):
    if i == 0 :
        sum_tri[i][i] = triangle[i][i]
        continue
    for j in range(len(triangle[i])):
        if j == 0 :
            sum_tri[i][j] = sum_tri[i-1][j] + triangle[i][j]
        elif j == len(triangle[i])-1:
            sum_tri[i][j] = sum_tri[i-1][j-1] + triangle[i][j]
        else:
            sum_tri[i][j] = max(sum_tri[i-1][j-1],sum_tri[i-1][j]) + triangle[i][j]
        
print(max(sum_tri[-1]))