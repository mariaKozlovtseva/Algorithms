class IndexedPriorityQueue:
    def __init__(self, inverse_ids):
        """
        This queue works with the pair of key-value where keys are of type string.
        If your keys are already integers, then modify this class and its methods.
        Dictionary inverse_ids will provide good interpretability for queue.
        Provide map, which can be obtained from inv_transform(keys) func in this module
        :param inverse_ids: given int id return its key. Id should be started from 1.
        """
        self.vals = [0]
        self.size = 0
        self.im = {} # inverse map: which key is represented at node of index i
        self.pm = {} # position map: given key id return its position
        self.inverse_ids = inverse_ids

    def insert(self, ki, val): # ki - transformed key to index
        """
        Provide ki of type integer. You can use transform_data(keys) func from this module.
        If you want to add new key, firstly add it to key-id map and then use this func.
        See examples for more details.
        :param ki: int, which starts from 1
        :param val: int
        Example:
        keys = ['cat', 'dog']
        ids = transform_data(keys)
        inverse_ids = inv_transform(keys)
        ipq = IndexedPriorityQueue()
        ipq.insert(ids['cat'], 2)
        ipq.insert(ids['dog'], 3)
        ids['bird'] = len(ids)+1
        ipq.insert(ids['bird'], 5)
        """
        self.vals.append(val)
        self.size += 1
        self.pm[ki] = self.size
        self.im[self.size] = ki
        self.check_priority_up()

    def swap(self, i, j):
        self.pm[self.im[i]], self.pm[self.im[j]] = self.pm[self.im[j]], self.pm[self.im[i]]
        self.im[i], self.im[j] = self.im[j], self.im[i]

    def check_priority_up(self, i=0):
        if not i: i = self.size
        while i//2:
            if self.vals[self.im[i]] < self.vals[self.im[i//2]]:
                self.swap(i, i//2)
            i //= 2

    def __str__(self):
        return str([(self.inverse_ids[ki], pos) for ki, pos in self.pm.items()])

    def get_min_val(self):
        return self.im[1], self.vals[self.im[1]]

    def extract_min(self):
        idx, val = self.get_min_val()
        self.swap(1, self.size)
        self.size -= 1
        self.check_priority_down()
        self.vals[idx] = None
        self.pm[idx] = -1
        self.im[self.size+1] = -1
        return idx, val

    def check_priority_down(self, i=1):
        while i*2 <= self.size:
            min_child = self.get_min_child(i)
            if self.vals[self.im[i]] > self.vals[self.im[min_child]]:
                self.swap(i, min_child)
            i = min_child

    def get_min_child(self, i):
        if i*2 + 1 > self.size:
            return i*2
        else:
            if self.vals[self.im[i*2]] < self.vals[self.im[i*2 + 1]]:
                return i*2
            else: return i*2 + 1

    def __contains__(self, ki):
        return ki in self.pm

    def decrease_key(self, ki, new_val):
        if new_val < self.vals[ki]:
            self.vals[ki] = new_val
            self.check_priority_up(self.pm[ki])

    def build_heap(self, dictionary):
        self.vals = [0] + list(dictionary.values())
        self.pm = dict(zip(dictionary.keys(), dictionary.keys()))
        self.im = dict(zip(dictionary.keys(), dictionary.keys()))
        self.size = len(dictionary)
        i = self.size // 2
        while i:
            self.check_priority_down(i)
            i -= 1


def transform_data(keys):
    return dict(zip(keys, range(1, len(keys) + 1)))

def inv_transform(keys):
    return dict(zip(range(1, len(keys)+1), keys))



if __name__ == '__main__':
    keys = ['cat', 'dog', 'bird', 'bee', 'duck']
    ids = transform_data(keys)
    inverse_ids = inv_transform(keys)
    ipq = IndexedPriorityQueue(inverse_ids)
    ipq.insert(ids['cat'], 2)
    ipq.insert(ids['dog'], 3)
    ipq.insert(ids['bird'], 5)
    ipq.insert(ids['bee'], 8)
    ipq.insert(ids['duck'], 1)
    print(ipq)
    print(ipq.extract_min())
    print(ipq.get_min_val())
    ipq.decrease_key(ids['bee'], 1.5)
    print(ipq)
    costs = {'cat': 2,
             'dog': 3,
             'bird': 5,
             'bee': 1.5}
    keys = list(costs.keys())
    ids = transform_data(keys)
    inverse_ids = inv_transform(keys)
    cost_ipq = IndexedPriorityQueue(inverse_ids)
    cost_ipq.build_heap(dict(zip(ids.values(), costs.values())))
    print(cost_ipq) # both equal
