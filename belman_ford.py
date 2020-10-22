def belman_ford(graph,start, size):
    # returns distance from start to all other vertices
    # if there is no negative cycle
    dist = [float("inf")] * size
    dist[start] = 0
    for i in range(size-1):
        # u - from, v - to, w - weight
        for u,v,w in graph:
            new_dist = dist[u] + w
            if dist[u] != "inf" and new_dist < dist[v]:
                dist[v] = new_dist
    # check for negative cycle
    for u, v, w in graph:
        new_dist = dist[u] + w
        if dist[u] != "inf" and new_dist < dist[v]:
            print('Graph contains negative weight cycle')
            return
    return dist

if __name__ == '__main__':
    graph = [[0, 1, -1],
             [0, 2, 4],
             [1, 2, 3],
             [1, 3, 2],
             [1, 4, 2],
             [3, 2, 5],
             [3, 1, 1],
             [4, 3, -3]]
    size = 5
    print(belman_ford(graph, 0, size))
    # with negative cycle
    graph = [[0, 1, 1],
             [0, 2, 2],
             [1, 3, 4],
             [2, 1, 1],
             [3, 2, -6]]
    size = 4
    print(belman_ford(graph, 0, size))