from graph import Graph
from indexed_priority_queue import IndexedPriorityQueue

def algo_dijkstra(graph, parents, costs):
    global processed
    processed = []
    node = find_lowest_node(costs)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = neighbours[n] + cost
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_node(costs)
    last_node = list(costs.keys())[-1]
    result = []
    while last_node != 'book':
        result.append(last_node)
        last_node = parents[last_node]
    result.append('book')
    return list(costs.values())[-1], result

def find_lowest_node(costs):
    lowest_weight = float("inf")
    lowest_node = None
    for node in costs:
        if costs[node] < lowest_weight and node not in processed:
            lowest_weight = costs[node]
            lowest_node = node
    return lowest_node


def algo_dijkstra2(g, start, parents, dist, keys):
    """
    This implementation uses Indexed Priority Queue and Graph,
    which makes complexity of O((E+V)logV))
    :param g: graph object
    :param start: start vertex, type str
    :param parents: map of vertex:parent, both key and value are string. Start vertex shouldn't be included in this map.
    :param dist: array of distances. Length of array == num of vertices
    :param keys: array of vertices of type str
    :return:
    """
    inverse_ids = dict(zip(range(1, len(dist) + 2), keys))
    ipq = IndexedPriorityQueue(inverse_ids)
    ipq.insert(1, dist[0])
    # while not empty
    while ipq.size:
        idx, val = ipq.extract_min()
        node = g.getVertex(idx)

        for neighbour in node.getConnections():
            new_cost = val + node.getWeight(neighbour)
            if new_cost < dist[neighbour.getId()-1]:
                dist[neighbour.getId()-1] = new_cost
                parents[inverse_ids[neighbour.getId()]] = inverse_ids[idx]
                if neighbour.getId() in ipq:
                    ipq.decrease_key(neighbour.getId(), new_cost)
                else:
                    ipq.insert(neighbour.getId(), new_cost)
            else:
                ipq.insert(neighbour.getId(), dist[neighbour.getId()-1])

    current = inverse_ids[idx]
    path = [current]
    while True:
        parent = parents[current]
        path.append(parent)
        current = parent
        if current == start:
            break
    return val, path

if __name__ == '__main__':
    costs = {'record': 5,
             'poster': 0,
             'guitar': float("inf"),
             'drums': float("inf"),
             'piano': float("inf")}

    parents = {'record': 'book',
               'poster': 'book',
               'guitar': None,
               'drums': None,
               'piano': None}

    graph = {'book': {'record': 5, 'poster': 0},
             'poster': {'guitar': 30, 'drums': 35},
             'record': {'guitar': 15, 'drums': 20},
             'guitar': {'piano': 20},
             'drums': {'piano': 10},
             'piano': {}}

    print(algo_dijkstra(graph, parents, costs))

    # method 2: using Indexed Priority Queue and Graph
    # now getting min value is O(logn)
    dijkstra = Graph()
    dist = {'record': 5,
             'poster': 0,
             'guitar': float("inf"),
             'drums': float("inf"),
             'piano': float("inf")}

    parents2 = {'record': 'book',
               'poster': 'book',
               'guitar': None,
               'drums': None,
               'piano': None}

    keys = ['book', 'record', 'poster', 'guitar', 'drums', 'piano']
    ids = dict(zip(keys, range(1, len(dist)+2)))

    dijkstra.addEdge(ids['book'], ids['record'], 5)
    dijkstra.addEdge(ids['book'], ids['poster'], 0)
    dijkstra.addEdge(ids['poster'], ids['guitar'], 30)
    dijkstra.addEdge(ids['poster'], ids['drums'], 35)
    dijkstra.addEdge(ids['record'], ids['guitar'], 15)
    dijkstra.addEdge(ids['record'], ids['drums'], 20)
    dijkstra.addEdge(ids['guitar'], ids['piano'], 20)
    dijkstra.addEdge(ids['drums'], ids['piano'], 10)

    dist = [0] + list(dist.values())
    print(algo_dijkstra2(dijkstra, 'book', parents2, dist, keys))
    # both methods give the same answer

