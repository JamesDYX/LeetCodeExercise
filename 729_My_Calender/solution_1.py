class TreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left = None
        self.right = None


class MyCalendar:
    # Binary Search Tree
    def __init__(self):
        self.tree = None

    def book(self, start: int, end: int) -> bool:
        if self.tree is None:
            self.tree = TreeNode(start, end)
            return True
        p = self.tree
        while True:
            if start >= p.end:
                if p.right is not None:
                    p = p.right
                else:
                    new_node = TreeNode(start, end)
                    p.right = new_node
                    return True
            elif end <= p.start:
                if p.left is not None:
                    p = p.left
                else:
                    new_node = TreeNode(start, end)
                    p.left = new_node
                    return True
            else:
                return False


if __name__ == '__main__':
    calender = MyCalendar()
    print(calender.book(10, 20))
    print(calender.book(15, 25))
    print(calender.book(20, 30))
    print(calender.book(5, 10))
    print(calender.book(8, 20))
