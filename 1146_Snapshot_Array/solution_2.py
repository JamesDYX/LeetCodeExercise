class SnapshotArray:
    # hash_map
    def __init__(self, length: int):
        self.memory = [{}]
        self.snap_shot_id = 0

    def set(self, index: int, val: int) -> None:
        self.memory[self.snap_shot_id][index] = val

    def snap(self) -> int:
        self.memory.append(self.memory[-1].copy())
        self.snap_shot_id += 1
        return self.snap_shot_id-1

    def get(self, index: int, snap_id: int) -> int:
        return self.memory[snap_id].get(index, 0)


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
