import numpy


class SnapshotArray:
    # compressed array
    def __init__(self, length: int):
        self.memory = numpy.zeros((length, 1, 2), dtype=int).tolist()
        self.current_list = {}
        self.snap_shot_id = -1

    def set(self, index: int, val: int) -> None:
        self.current_list[index] = val

    def snap(self) -> int:
        self.snap_shot_id += 1
        if not self.snap_shot_id:
            for index, value in self.current_list.items():
                self.memory[index][0][1] = value
        else:
            for index, value in self.current_list.items():
                self.memory[index].append([self.snap_shot_id, value])

        self.current_list = {}
        return self.snap_shot_id

    def get(self, index: int, snap_id: int) -> int:
        snap_memory = self.memory[index]
        left, right = 0, len(snap_memory) -1
        while left <= right:
            mid = (left + right) // 2
            if snap_memory[mid][0] == snap_id:
                return snap_memory[mid][1]
            elif snap_memory[mid][0] < snap_id:
                left = mid + 1
            else:
                right = mid - 1
        return snap_memory[right][1]


if __name__ == '__main__':
    a = SnapshotArray(1)
    print(a.snap())
    print(a.snap())
    print(a.set(0, 4))
    print(a.snap())
    print(a.get(0, 1))
    print(a.set(0, 12))
    print(a.get(0, 1))
    print(a.snap())
    print(a.get(0, 3))
