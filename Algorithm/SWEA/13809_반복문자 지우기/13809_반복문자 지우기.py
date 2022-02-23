import sys
sys.stdin = open("sample_input(3) (1).txt")

T = int(input())

for tc in range(1,T+1):
    text = input()

    stack = []

    for i in text:
        if len(stack):
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    print(f'#{tc} {len(stack)}')
