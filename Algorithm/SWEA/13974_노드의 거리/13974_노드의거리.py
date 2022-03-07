# 입력순서 : T(테스트케이스 수) -> V(노드 수) , E(간선 수) -> S(출발 노드) , G(도착 노드)

T = int(input())

# dfs 함수
def dfs(node):
    global result
    if node == G:
        result = sum(visited)
        return

    for i in range(1,V+1):
        if node_arr[node][i] and not visited[i]:
            visited[node] = 1
            dfs(i)
            visited[node] = 0

for tc in range(1,T+1):
    V,E = map(int,input().split())

    # 간선들을 담을 리스트
    node_arr = [[0]*(V+1) for _ in range(V+1) ]

    # 간선 업로드
    for i in range(E):
        n_1 , n_2 = map(int,input().split())
        node_arr[n_1][n_2] = 1
        node_arr[n_2][n_1] = 1

    # 방문기록 리스트
    visited = [0] * (V+1)

    S , G = map(int,input().split())

    result = 0

    dfs(S)

    print(f'#{tc} {result}')