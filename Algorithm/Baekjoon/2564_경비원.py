#가로,세로 입력
garo , sero = map(int,input().split())
#가게 수
N = int(input())

#최소거리 구하는 함수
#x1 : 가게방향 y1 : 위치 x2 : 동근이방향 y2 : 동근이 위치
def min_distance(x1,y1,x2,y2):
    if x1 == 1: #가게 방향 북쪽
        if x2 == 1: #동근이 방향 북쪽
            return abs(y1-y2) #같은 위치에 있으므로 절대값 거리반환
        elif x2 == 2: #동빙남
            return min((y2+sero+y1),(garo-y2+sero+garo-y1)) #시계방향,반시계방향은 최소값 반환
        elif x2 == 3 : #동방서
            return min((y2+y1),(sero-y2+garo+sero+garo-y1))
        elif x2 == 4 : #동방동
            return min((sero-y2+garo+sero+y1),(y2+garo-y1))
    elif x1 == 2: #가방남
        if x2 == 1: 
            return min((garo-y2+sero+garo-y1),(y2+sero+y1)) #시계방향,반시계방향은 최소값 반환
        elif x2 == 2: 
            return abs(y1-y2) #같은 방향에 있으므로 절대값 거리반환
        elif x2 == 3 : 
            return min((y2+garo+sero+garo-y1),(sero-y2+y1))
        elif x2 == 4 : 
            return min((sero-y2+garo-y1),(y2+garo+sero+y1))
    elif x1 == 3: #가방서
        if x2 == 1: 
            return min((garo-y2+sero+garo+sero-y1),(y2+y1))
        elif x2 == 2: 
            return min((y2+sero-y1),(garo-y2+sero+garo+y1)) #시계방향,반시계방향은 최소값 반환
        elif x2 == 3 : 
            return abs(y1-y2) #같은 방향에 있으므로 절대값 거리반환
        elif x2 == 4 : 
            return min((sero-y2+garo+sero-y1),(y2+garo+y1))
    elif x1 == 4: #가위동
        if x2 == 1: 
            return min((garo-y2+y1),(y2+sero+garo+sero-y1))
        elif x2 == 2: 
            return min((y2+sero+garo+y1),(garo-y2+sero-y1)) #시계방향,반시계방향은 최소값 반환
        elif x2 == 3 : 
            return min((y2+garo+y1),(sero-y2+garo+sero-y1))
        elif x2 == 4 : 
            return abs(y1-y2) #같은 방향에 있으므로 절대값 거리반환

store_arr = []
#가게방향/위치
for i in range(N):
    x1 , y1 = map(int,input().split())
    store_arr.append([x1,y1])

#동근이방향/위치
x2 , y2 = map(int,input().split())

#최단거리 합
result = 0
for i in store_arr:
    result += min_distance(i[0],i[1],x2,y2)

print(result)