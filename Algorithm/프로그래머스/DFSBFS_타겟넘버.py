# dfs
'''
sum에 현재 값을 더하는 경우와 빼는 경우로 dfs를 돌아주고, 만약 현재 깊이가 len(numbers)와 같을 경우 sum과 target이 같다면 카운팅
'''
answer = 0
def dfs(sum, d, numbers, target):
    global answer
    if d == len(numbers):
        if sum == target:
            answer += 1
        return

    dfs(sum+numbers[d], d+1, numbers, target)
    dfs(sum-numbers[d], d+1, numbers, target)


def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return answer