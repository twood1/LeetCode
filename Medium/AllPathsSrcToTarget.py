class Solution:
    def allPathsSourceTarget(self, graph):
        paths = self.doDFS(graph, 0, len(graph), [], [])
        return paths

    def doDFS(self, graph, currNode, N, currPath, paths):
        currPath.append(currNode)
        # If we found the target node, append the path and pop the node and return. Don't need to check anymore
        # since it's acyclic.
        if currNode == N-1:
            paths.append(currPath.copy())
            currPath.pop()
            return
        for neighbor in graph[currNode]:
            self.doDFS(graph, neighbor, N, currPath, paths)
        # Python annoyingly keeps parameter values stored in some heap out of stack space, so need to pop the currPath
        # once we are done with this node on that path.
        currPath.pop()
        return paths