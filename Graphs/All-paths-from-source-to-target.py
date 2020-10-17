class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        end = len(graph)-1
        
        def dfs(node, path, l):
            if node == end:
                l.append(path)
            for neighbour in graph[node]:
                dfs(neighbour, path+[neighbour], l)
        
        l = []
        dfs(0, [0], l)
        return l
        