from heapq import heappush, heappop, heapify
from collections import Counter, namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    def check(self, code, acc):
        self.left.check(code, acc + '0')
        self.right.check(code, acc + '1')


class Leaf(namedtuple('Leaf', ['symbol'])):
    def check(self, code, acc):
        code[self.symbol] = acc or '0'


def encode(txt):
    queue = []
    for _symb, freq in Counter(txt).items():
        queue.append((freq, len(queue), Leaf(_symb)))
    heapify(queue)
    count = len(queue)
    while len(queue) > 1:
        freq_1, _trash_1, left = heappop(queue)
        freq_2, _trash_2, right = heappop(queue)
        heappush(queue, (freq_1 + freq_2, count, Node(left, right)))
        print(queue, '\n')
        count += 1
    code = {}
    if queue:
        [(_freq, _count, root)] = queue
        root.check(code, '')
    return code


if __name__ == '__main__':
    text = input()
    simplified = text.upper()
    enc = encode(simplified)
    binary_code = ''.join(enc[symb] for symb in enc)
    print(simplified, '>>>', binary_code)
    print("Symbol\tHuffman Code")
    for p in enc:
         print('{}\t\t{}'.format(p[0], enc[p]))
