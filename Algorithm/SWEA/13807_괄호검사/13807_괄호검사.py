import sys
sys.stdin = open("sample_input(1) (3).txt")

T = int(input())

for tc in range(1,T+1):
    text = input()
    stack = []
    gualho = ['(',')','{','}']

    for i in text:
        if i in gualho:
            if i == '(' or i =='{':
                stack.append(i)
            elif len(stack):
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i =='}' and stack[-1] == '{':
                    stack.pop()
                else:
                    print(f'#{tc} 0')
                    stack.append(i)
                    break
            else:
                print(f'#{tc} 0')
                stack.append(i)
                break
        else:
            pass
    else :
        if not len(stack):
            print(f'#{tc} 1')
        else:
            print(f'#{tc} 0')