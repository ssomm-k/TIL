students = int(input())

random_num = list(map(int,input().split()))

student_num = []
for i in range(students):
    if random_num[i] > 0 :
        student_num.insert(i-random_num[i],i+1)
    else :
        student_num.append(i+1)

for pr in student_num:
    print(pr , end=' ')

#--------------------------------------------------
# 아래 두줄은 처음 맞은 pritn 방법
# s_n = list(map(str,student_num))
# print(' '.join(s_n))

#--------------------------------------------------
#연습코드 1
# 아래코드로 돌리면 4번째에서 원하는 결과랑 다르게 나옴
# student_num = list(range(1,students+1))
# for i in student_num:
#     if random_num[i-1] > 0:
#         student_num[i-1] = student_num[i-(random_num[i-1])-1]
#         student_num[i-(random_num[i-1])-1] = i

# print(student_num[0],student_num[1],student_num[2],student_num[3],student_num[4])