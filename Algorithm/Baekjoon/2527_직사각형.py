# 입력 순서 : 사각형 왼쪽 아래(x,y) , 사각형 오른쪽 위(p,q)

T = 4

for i in range(T):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int,input().split())

    # 결과
    result = 'a'

    # 만나지 않는다. 
    if q1 < y2 or q2 < y1 or x1 > p2 or p1 < x2:
        result = 'd'
    else:
        # 점 & 선 (왼쪽 -> 오른쪽)
        if p1 == x2:
            # 점
            if q1 == y2 or y1 == q2:
                result = 'c'
            else:
                result = 'b'
        if x1 == p2:
            if y1 == q2 or q1 == y2:
                result = 'c'
            else:
                result = 'b'
        if q1 == y2:
            if p1 == x2 or p2 == x1:
                result = 'c'
            else:
                result = 'b'
        if q2 == y1:
            if p1 == x2 or p2 == x1:
                result = 'c'
            else:
                result = 'b'

    # 위 조건에서 다 통과하지 못하면 다 직사각형
    
    print(result)