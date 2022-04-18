N, M = map(int, input().split())
tree = list(map(int, input().split()))

#이분탐색 검색 범위 설정
start, end = 1, max(tree) 

#적절한 벌목 높이를 찾는 알고리즘
while start <= end: 
    mid = (start+end) // 2
    
    #벌목된 나무 총합
    out_tree = 0 
    for i in tree:
        if i >= mid:
            out_tree += i - mid
    
    #벌목 높이를 이분탐색
    if out_tree >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)