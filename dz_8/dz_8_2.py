import heapq
from collections import Counter, namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def haffman_encode(str):
    # Создание дерева при помощи очереди с приоритетами
    h = []
    for ch, freq in Counter(str).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    # Корень дерева
    code = dict()
    # Создание словаря с кодами
    if h:
        [(_freq, _count, root)] = h
        root.walk(code=code, acc="")
    # Вывод элемента и его кода
    for key, val in code.items():
        print(f'{key}: {val}')

    return ''.join(code[ch] for ch in str)


if __name__ == '__main__':
    encoded = haffman_encode(input('Введите строку: '))
    print(encoded)
