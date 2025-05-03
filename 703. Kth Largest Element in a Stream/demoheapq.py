class DemoHeapq:
    def __init__(self, array: list):
        self.array = array[:]
        self._heapfy()

    def push(self, val):
        self.array.append(val)
        self._siftdown(0, len(self.array) - 1)

    def pop(self):
        last_val = self.array.pop()
        if self.array:
            return_val = self.array[0]
            self.array[0] = last_val
            self._siftup(0)
            return return_val
        return last_val

    def _heapfy(self):
        n = len(self.array)
        for pos in range(n // 2)[::-1]:
            self._siftup(pos)

    def _siftup(self, pos):
        val = self.array[pos]
        start_pos = pos
        end_pos = len(self.array)

        child_pos = 2 * pos + 1
        while child_pos < end_pos:
            right_child_pos = child_pos + 1
            if (
                right_child_pos < end_pos
                and not self.array[child_pos] < self.array[right_child_pos]
            ):
                child_pos = right_child_pos
            self.array[pos] = self.array[child_pos]
            pos = child_pos
            child_pos = 2 * pos + 1
        self.array[pos] = val
        self._siftdown(start_pos, pos)

    def _siftdown(self, start_pos, pos):
        val = self.array[pos]
        while pos > start_pos:
            parent_pos = (pos - 1) // 2
            if self.array[parent_pos] <= val:
                break
            self.array[pos] = self.array[parent_pos]
            pos = parent_pos
        self.array[pos] = val


if __name__ == "__main__":
    import heapq
    import random

    def assert_eq(l1, l2):
        assert len(l1) == len(l2)
        assert all((i == j for i, j in zip(l1, l2)))

    for _ in range(100):
        num_list = [random.randint(0, 1000) for _ in range(1000)]
        demo_heap = DemoHeapq(num_list)

        # check heapify
        heapq.heapify(num_list)
        assert_eq(num_list, demo_heap.array)

        for num in [random.randint(0, 1000) for _ in range(1000)]:
            demo_heap.push(num)

            # check push
            heapq.heappush(num_list, num)
            assert_eq(num_list, demo_heap.array)

            # chech pop
            pop_from_heapq = heapq.heappop(num_list)
            pop_from_demo_heapq = demo_heap.pop()
            assert pop_from_heapq == pop_from_demo_heapq
            assert_eq(num_list, demo_heap.array)
