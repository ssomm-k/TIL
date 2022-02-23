import sys
sys.stdin = open("input (11).txt")

T = 10

for tc in range(1,T+1):
    case_len = int(input())
    susic = input()
    yunsan = ['+','*']
    # 연산기호 저장
    stack = []
    # 후위표기식 저장
    result = []

    # 입력 받은 문자열을 후위표기식으로 만들기 위한 준비 1
    for i in susic:
        # 연산기호가 아니면 result에 append해준다.
        if i not in yunsan:
            result.append(i)
        else:
            # 연산기호가 + 일땐 *의 우선 순위가 높으므로 확인이 필요하다.
            if i == '+':
                # 빈stack이 아니고 이전 기호가 * 이면 *를 pop해주고 append한다.
                if len(stack) and stack[-1] == '*':
                    pop_yunsan = stack.pop()
                    result.append(pop_yunsan)
                    stack.append(i)
                # 빈stack 이거나 이전 기호가 + 인 경우는 그냥 append한다.
                else:
                    stack.append(i)
            # 연산기호가 * 일때
            else:
                # 빈stack이 아니고 이전 기호가 * 인 경우는 pop해주고 append한다.
                if len(stack) and stack[-1] == '*':
                    pop_yunsan = stack.pop()
                    result.append(pop_yunsan)
                    stack.append(i)
                # 빈stack 이거나 이전 기호가 + 인 경우는 그냥 append한다.
                else:
                    stack.append(i)

    # stack에 남아있는 기호를 모두 후위표기식으로 넘겨준다.
    for i in range(len(stack)):
        pop_yunsan = stack.pop()
        result.append(pop_yunsan)

    # 작성된 후위표기식과 비어있는 stack리스트를 이용해 계산한다.
    for i in result:
        # i가 숫자일때는 stack에 쌓고
        if i not in yunsan:
            stack.append(i)
        # i가 연산기호 일때는 계산한다.
        # i : 연산기호('*'or'+') / i1 : 2번째 pop 숫자 / i2 : 1번째 pop 숫자
        # new_i = i1  * or + i2
        else:
            if i == '*':
                i2 = int(stack.pop())
                i1 = int(stack.pop())
                new_i = i1 * i2
                stack.append(new_i)
            elif i == '+':
                i2 = int(stack.pop())
                i1 = int(stack.pop())
                new_i = i1 + i2
                stack.append(new_i)

    print(f'#{tc} {stack.pop()}')