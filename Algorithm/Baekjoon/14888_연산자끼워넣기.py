# + -> - -> * -> /
# 연산 딕셔너리를 앞에서부터 사용한다.
def dfs(sum,d,numbers):
    if d == N:
        result.append(sum)
        return

    if yunsan['+'] != 0:
        yunsan['+'] -= 1
        dfs(sum+num_arr[d],d+1,numbers)
        yunsan['+'] += 1
    if yunsan['-'] != 0:
        yunsan['-'] -= 1
        dfs(sum-num_arr[d],d+1,numbers)
        yunsan['-'] += 1
    if yunsan['*'] != 0:
        yunsan['*'] -= 1
        dfs(sum*num_arr[d],d+1,numbers)
        yunsan['*'] += 1
    if yunsan['/'] != 0:
        yunsan['/'] -= 1
        if sum < 0:
            dfs(-((-sum)//num_arr[d]),d+1,numbers)
            yunsan['/'] += 1
        else:
            dfs(sum//num_arr[d],d+1,numbers)
            yunsan['/'] += 1

N = int(input())
num_arr = list(map(int,input().split()))
yunsan_num = list(map(int,input().split()))
yunsan = {
    '+' : yunsan_num[0],
    '-' : yunsan_num[1],
    '*' : yunsan_num[2],
    '/' : yunsan_num[3]
    }

result = []

dfs(num_arr[0],1,num_arr)

print(max(result))
print(min(result))
