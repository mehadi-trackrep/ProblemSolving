import json

class Solution:
    def __init__(self):
        self.visited = []

    def DFS(self, graph, root_node) -> bool:  ### TopSort & Cycle detection logic
        print('==> root_node: ', root_node)
        self.visited[root_node] = 1
        res = True
        for each_node in graph[root_node]:
            if self.visited[each_node] == 0:
                res = res and self.DFS(graph, each_node)
            elif self.visited[each_node] == 1:
                res = res and False
        self.visited[root_node] = 2
        return res

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = {k: [] for k in range(numCourses)}
        self.visited = [0 for i in range(numCourses)]

        for each_list in prerequisites:
            u = each_list[0]
            v = each_list[1]
            graph[u].append(v)
        
        print(json.dumps(graph, indent=4))

        for each_course in range(numCourses):
            if not self.DFS(graph, each_course):
                return False
        return True

if __name__ == '__main__':
    obj = Solution()
    numCourses = 6
    a_list = [
        [0, 1]
        ,[1, 2]
        # ,[2, 3]
        ,[3, 4]
        ,[3, 0]
    ]
    print(obj.canFinish(
        numCourses=numCourses,
        prerequisites=a_list
    ))