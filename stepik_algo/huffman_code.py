from collections import Counter, namedtuple
import heapq

class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'

def encode_huffman(s):
    if not s: return {}
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, count1, char1 = heapq.heappop(h)
        freq2, count2, char2 = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(char1, char2)))
        count += 1
    [[freq, count, root]] = h
    code = {}
    root.walk(code, '')
    return code

def decode_huffman(code_dict, encod_s):
    # code_dict = {a: 0
    #              b: 10
    #              c: 110
    #              d: 111}
    # encod_s   = 01001100100111
    # res       = abacabad
    sequence = ''
    res = ''
    for elem in encod_s:
        sequence += elem
        if sequence in code_dict:
            res += code_dict[sequence]
            sequence = ''
    return res

def main_2():
    k, l = map(int, input().split())
    d = {}
    for i in range(k):
        data = input().split(': ')
        d[data[1]] = data[0]
    encoded_s = input()
    res = decode_huffman(d, encoded_s)
    print(res)

def main():
    s = input()
    encoded_s = encode_huffman(s)
    res = ''.join(encoded_s[ch] for ch in s)
    print(str(len(encoded_s)) + ' ' + str(len(res)))
    for k, v in encoded_s.items():
        print('{}: {}'.format(k, v))
    print(res)


if __name__ == '__main__':
    main()
    main_2()