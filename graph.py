from collections import defaultdict

class Graph(object):

    def __init__(self):

        self.graph = defaultdict(list)

    def addEdge(self,u,v):

        self.graph[u].append(v)

    def BFS(self,s):

        visited = [False]*len(self.graph)

        queue = []

        queue.append(s)

        visited[s] = True



        