# 위상정렬 - 임계경로 (백준 플래5)
# 문제 링크: https://www.acmicpc.net/problem/1948
N = int(input())
M = int(input())
# graph = {} # TODO: pre_graph, post_graph로 나눠서 post는 degree 연산, pre는 시간 연산으로 사용할 것
pre_graph = [[] for _ in range(N + 1)] # M
post_graph = [[] for _ in range(N + 1)] # M
degree = [0] * (N + 1) # N
for i in range(M):
    u, v, w = map(int, input().split())
    post_graph[u].append((v, w))
    pre_graph[v].append((u, w))
    degree[v] += 1

START_POINT, END_POINT = map(int, input().split())


from collections import deque
q = deque([(START_POINT, 0)])
time_cost = [0] * (N + 1)

while q:
    point, bridge_cnt = q.popleft()
    time = 0
    for prev_node, prev_weight in pre_graph[point]:
        if time < time_cost[prev_node] + prev_weight:
            time = time_cost[prev_node] + prev_weight
            
    time_cost[point] = time
    for next_node, next_weight in post_graph[point]:
        degree[next_node] -= 1
        if degree[next_node] == 0:
            q.append((next_node, bridge_cnt + 1))



'''
set 연산이 큼. 따라서 visited 사용해야함. 또한 중복 경로가 너무 많이 들어갈 수 있음.
visited로 방문했던 노드 재방문 방지.(경로가 여러 개면 여러 번 들어갈테니)
'''
q = deque([END_POINT])
visited = [False] * (N + 1)
visited[END_POINT] = True
cnt = 0
while q:
    front = q.popleft()
    for i, w in pre_graph[front]:
        if time_cost[i] + w == time_cost[front]:
            cnt += 1
            if not visited[i]:
                visited[i] = True
                q.append(i)

print(time_cost[END_POINT])
print(cnt)