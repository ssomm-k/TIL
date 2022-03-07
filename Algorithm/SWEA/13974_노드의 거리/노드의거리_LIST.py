# 입력순서 : T(테스트케이스 수) -> V(노드 수) , E(간선 수) -> S(출발 노드) , G(도착 노드)

T = int(input())

# dfs 함수
def dfs(node,d):
    global result
    # 백트레킹
    if d >= result:
        return
    # 함수 탈출
    if node == G:
        result = min(result,d)
        return
    # 재귀함수
    for n in node_arr[node]:
        if not visited[n]:
            visited[n] = 1
            dfs(n,d+1)
            visited[n] = 0

for tc in range(1,T+1):
    V,E = map(int,input().split())

    # 간선들을 담을 리스트
    node_arr = [[] for _ in range(V+1) ]

    # 간선 업로드
    for i in range(E):
        n_1 , n_2 = map(int,input().split())
        node_arr[n_1].append(n_2)
        node_arr[n_2].append(n_1)

    # 방문기록 리스트
    visited = [0] * (V+1)

    S , G = map(int,input().split())

    visited[S] = 1

    result = 1e9

    dfs(S,0)

    print(f'#{tc} {result}')