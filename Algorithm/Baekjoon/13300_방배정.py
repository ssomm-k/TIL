N , K = map(int,input().split())

i = 1
students = []
while i <= N:
    S , Y = map(int,input().split())
    students.append((S,Y))
    i += 1

student_type = set(students)
type_count = []

for a in student_type:
    type_count.append([a,students.count(a)])

d = 0
for j in type_count :
    if j[1]%K == 0 :
        d += j[1]//K
    else : d += (1+j[1]//K)

print(d)