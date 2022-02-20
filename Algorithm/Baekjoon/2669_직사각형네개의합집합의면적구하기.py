# 직사각형의 수
box_n = 4
arr = [[0]*101 for _ in range(101)]

box_cnt = 0

for box in range(box_n):
    # 입력순서가 사각형의 왼쪽 아래 x,y 오른쪽위 x,y
    x1,y1,x2,y2 = map(int,input().split())
    # x의 범위를 x1부터 x2+1까지 하지 않고 x2까지 한다.
    # 사각형의 넓이를 구할때 (x2-x1)(y2-y1)으로 넓이를 구하는 것과 유사하다.
    for x in range(x1,x2):
        for y in range(y1,y2):
            if not arr[x][y] :
                arr[x][y] = 1
                box_cnt += 1

print(box_cnt)

# 생각을 잘못한듯
# # 겹치는 부분을 알아서 제거하여 모으기 위해 set을 사용함
# box_area = set()
# ggup_area = []

# for box in range(box_cnt):
#     # 입력순서가 사각형의 왼쪽 아래 x,y 오른쪽위 x,y
#     x1,y1,x2,y2 = map(int,input().split())
#     for x in range(x1,x2+1):
#         for y in range(y1,y2+1):
#             if (x,y) not in box_area:
#                 box_area.add((x,y))
#             else:
#                 ggup_area.append((x,y))
#     print(box_area,ggup_area)

# print(len(box_area),ggup_area)