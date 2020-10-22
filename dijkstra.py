costs = {'record':5,
         'poster': 0,
         'guitar': float("inf"),
         'drums': float("inf"),
         'piano': float("inf")}

parents = {'record':'book',
         'poster': 'book',
         'guitar': None,
         'drums': None,
         'piano': None}

graph = {'book': {'record':5, 'poster':0},
         'poster': {'guitar':30, 'drums':35},
         'record': {'guitar':15, 'drums':20},
         'guitar': {'piano':20},
         'drums': {'piano':10},
         'piano': {}}

def algo_dijkstra(graph, parents, costs):
    """
    Find the smallest path from book to piano
    :param graph: dict
    :param parents: dict
    :param costs: dict
    :return: smallest value of path and path itself from the piano to the book
    """
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

if __name__ == '__main__':
    print(algo_dijkstra(graph, parents, costs))

