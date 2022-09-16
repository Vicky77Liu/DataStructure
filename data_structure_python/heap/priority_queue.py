from heap.max_heap import MaxHeap


class PriorityQueue:
    def __init__(self):
        self.max_heap = MaxHeap()

    def __str__(self):
        return str(self.max_heap)

    def __len__(self):
        return len(self.max_heap)

    def is_empty(self):
        return self.max_heap.is_empty()

    def enqueue(self, val):
        self.max_heap.add(val)

    def dequeue(self):
        return self.max_heap.extract_max()

    def get_head(self):
        return self.max_heap.find_max()


if __name__ == '__main__':
    q = PriorityQueue()
    q.enqueue(20)
    q.enqueue(45)
    q.enqueue(33)
    q.enqueue(10)
    print(q)
    print(q.get_head())
    print(q.dequeue())
    print(q)
