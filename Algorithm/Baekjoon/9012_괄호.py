T = int(input())

Vps_list = []
i = 1
while i <= T:
    Vps_list.append(str(input()))
    i += 1


for Vps in Vps_list:
    stack_list = []
    cnt = 0 
    for j in Vps:
        if j == '(':
            stack_list.append(j)
        else :
            if not stack_list :
                break
            else :
                stack_list.pop()
        cnt += 1

    if not stack_list and cnt == len(Vps):
        print('YES')
    else:
        print('NO')


# 연습코드2 --> 실패
# for Vps in Vps_list:
#     if len(Vps) % 2 :
#         print('NO')
#     else:
#         stack_list = []
#         for j in Vps:
#             if j == '(':
#                 stack_list.append(j)
#             elif j == ')':
#                 if len(stack_list) > 0 :
#                     stack_list.pop()
#                 else : 
#                     print('NO')
#         if len(stack_list) != 0 :
#             print('NO')
#         else : print('YES')



# 연습코드1 --> 실패
# Vps_list = []
# i = 1
# while i <= T:
#     Vps_list.append(str(input()))
#     i += 1

# b = ['(',')']
# for j in Vps_list:
#     if j.count(b[0]) == j.count(b[1]):
#         print('YES')
#     else : print('NO')