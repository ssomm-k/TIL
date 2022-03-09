# DFS 메서드 정의
def dfs(graph,v,visited):
    # 현재 노드를 방문 처리
    visited[v] = 1
    print(v,end=' ')
    # 현재 노드와 연결되 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


# 각 노드가 연결되 정보를 표현한 2차원 리스트
graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

# 각 노드가 방문된 정보를 표현한 1차원 리스트
visited = [0] * 9

# 함수 호출
dfs(graph,1,visited)