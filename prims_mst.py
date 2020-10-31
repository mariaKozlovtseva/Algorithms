from indexed_priority_queue import IndexedPriorityQueue, transform_data, inv_transform
from graph import Graph

def prims_algo(g, start, inv_ids, ids):
    ipq = IndexedPriorityQueue(inv_ids)
    for vertex in g:
        vertex.setDist(float('inf'))
        vertex.setPred(None)
    start.setDist(0)
    ipq.build_heap(dict([(ids[vertex.getId()], vertex.getDist()) for vertex in g]))
    visited = []
    while ipq.size:
        key, val = ipq.extract_min()
        node = g.getVertex(inv_ids[key])
        for neighbour in node.getConnections():
            if neighbour in visited: continue
            new_val = val + node.getWeight(neighbour)
            if ids[neighbour.getId()] in ipq and new_val < neighbour.getDist():
                neighbour.setPred(node)
                neighbour.setDist(new_val)
                ipq.decrease_key(ids[neighbour.getId()], new_val)
        visited.append(node)

    res = []
    for vertex in g.getVertices():
        vertex = g.getVertex(vertex)
        if not vertex.getPred():
            res.append((vertex.getPred(), vertex.getId(), vertex.getDist()))
        else:
            res.append((vertex.getPred().getId(), vertex.getId(), vertex.getDist()))
    return res



if __name__ == '__main__':
    keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    ids = transform_data(keys)
    inverse_ids = inv_transform(keys)
    d = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
        'C': {'A': 3, 'B': 1, 'F': 5},
        'D': {'B': 1, 'E': 1},
        'E': {'B': 4, 'F': 1, 'D': 1},
        'F': {'C': 5, 'G': 1, 'E': 1},
        'G': {'F': 1}
    }
    g = Graph()
    g.build_graph(d)
    print(prims_algo(g, g.getVertex('A'), inverse_ids, ids))