class Vertex:
    def __init__(self, key):
        self.connections = {}
        self.id = key
        self.pred = None
        # need this atributes for bfs and dfs
        self.color = "white"
        self.dist = 0
        self.discover_t = 0
        self.finish_t = 0

    def discovery_time(self, time): self.discover_t = time

    def finish_time(self, time): self.finish_t = time

    def addNeighbour(self, nbr, weight=0):
        self.connections[nbr] = weight

    def getConnections(self): return self.connections.keys()

    def getId(self): return self.id

    def getWeight(self, nbr): return self.connections[nbr]

    def getPred(self): return self.pred

    def setPred(self, vert): self.pred = vert

    def getDist(self): return self.dist

    def setDist(self, dist): self.dist = dist

    def getColor(self): return self.color

    def setColor(self, color): self.color = color

    def __str__(self):
        return str(self.getId())


class Graph:
    def __init__(self):
        self.vertices = {}
        self.size = 0

    def addEdge(self, fromVertex, toVertex, weight=0):
        if fromVertex not in self.vertices:
            self.addVertex(fromVertex)
        if toVertex not in self.vertices:
            self.addVertex(toVertex)
        self.vertices[fromVertex].addNeighbour(self.vertices[toVertex], weight)

    def __contains__(self, key):
        return key in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def addVertex(self, key):
        self.size += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex

    def getVertex(self, key):
        if key in self.vertices:
            return self.vertices[key]

    def getVertices(self): return self.vertices.keys()

from collections import deque
def bfs(g, start):
    start = g.getVertex(start)
    frontier = deque()
    frontier.append(start)
    while frontier:
        curr_vertex = frontier.popleft()
        for v in curr_vertex.getConnections():
            if v.getColor() == "white":
                v.setColor("grey")
                v.setPred(curr_vertex)
                v.setDist(1 + curr_vertex.getDist())
                frontier.append(v)
        curr_vertex.setColor("black")
    traverse(g)

def traverse(g):
    last_node = g.getVertex(g.size - 1)
    while last_node.getPred():
        print(last_node.getId())
        last_node = last_node.getPred()
    print(last_node.getId())

class DFSgraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for v in self:
            if v.getColor() == 'white':
                self.dfs_helper(v)

    def dfs_helper(self, vertex):
        vertex.setColor('gray')
        self.time += 1
        vertex.discovery_time(self.time)
        for next_vertex in vertex.getConnections():
            if next_vertex.getColor() == 'white':
                next_vertex.setPred(vertex)
                self.dfs_helper(next_vertex)
        self.time += 1
        vertex.setColor('black')
        vertex.finish_time(self.time)
        print('id',vertex.getId(), 'discovery time: ',vertex.discover_t,
              'finish time: ', vertex.finish_t)


if __name__ == '__main__':
    g = Graph()
    for i in range(5):
        g.addVertex(i)
    g.addEdge(0, 1, 1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 2)
    g.addEdge(1, 3, 4)
    g.addEdge(2, 3, 3)
    g.addEdge(2, 4, 5)
    g.addEdge(3, 4, 6)
    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
    bfs(g, 0)
    dfs = DFSgraph()
    for i in range(9):
        dfs.addVertex(i)
    dfs.addEdge(0, 4)
    dfs.addEdge(2, 4)
    dfs.addEdge(3, 4)
    dfs.addEdge(4, 5)
    dfs.addEdge(1, 5)
    dfs.addEdge(4, 6)
    dfs.addEdge(6, 8)
    dfs.addEdge(5, 7)
    dfs.addEdge(7, 8)
    dfs.dfs()
