# 그래프 - Course Schedule
# 문제 링크: https://leetcode.com/problems/course-schedule/?envType=study-plan-v2&envId=top-interview-150
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        arr = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for a, b in prerequisites:
            degree[a] += 1
            arr[b].append(a)
        q = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)
        visited = [False for _ in range(numCourses)]
        while q:
            f = q.popleft()
            visited[f] = True
            for i in arr[f]:
                degree[i] -= 1
                if degree[i] == 0:
                    q.append(i)
        for i in visited:
            if not i:
                return False
        return True
            
            