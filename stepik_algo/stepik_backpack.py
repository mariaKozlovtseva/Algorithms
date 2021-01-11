import sys
import heapq

# greedy approach
def backpack(capacity, items):
    unit_costs = [(-v/w, w) for v, w in items]
    heapq.heapify(unit_costs)
    result = 0
    while unit_costs and capacity:
        v_per_w, w = heapq.heappop(unit_costs)
        can_take = min(capacity, w)
        result -= v_per_w * can_take
        capacity -= w
    return result

def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, capacity = next(reader)
    items = list(reader)
    assert len(items) == n
    result = backpack(capacity, items)
    print('{:.3f}'.format(result))
if __name__ == '__main__':
    main()