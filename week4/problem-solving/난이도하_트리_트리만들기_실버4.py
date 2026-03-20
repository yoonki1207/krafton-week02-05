# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

N, M = map(int, input().split())

print(0, 1)
prev_node = 1
next_node = 2
while N - 2:
    N -= 1

    print(prev_node, next_node)
    if M > 2: # 0과 N-1을 제외한 나머지 모든 리프노드들을 1에서 시작하게 만든다
        M -= 1
        next_node += 1
    else: # 꼬리물기 (리프 노드 생성 안 됨)
        prev_node = next_node
        next_node = prev_node + 1
