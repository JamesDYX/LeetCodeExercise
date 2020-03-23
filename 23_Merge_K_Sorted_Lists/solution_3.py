class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: list):
        l = []
        for node in lists:
            while node:
                l.append(node.val)
                node = node.next
        return self.tolinkedlist(sorted(l))

    def tolinkedlist(self, ints):
        p = head = None
        for number in ints:
            Node = ListNode(number)
            if not head:
                p = head = Node
            else:
                p.next = Node
                p = Node
        return head


def constructList(string):
    head = None
    p = head
    for c in string:
        c = int(c)
        node = ListNode(c)
        if head is None:
            head = node
        else:
            p.next = node
        p = node
    return head


def reconstruct(l):
    string = ''
    p = l
    while p is not None:
        string += str(p.val)
        p = p.next
    return string


if __name__ == '__main__':
    test_cases = [
        ["124789", "2", "3", "4", "13456", "6779"],
    ]

    solution = Solution()
    for strings in test_cases:
        for i, string in enumerate(strings):
            strings[i] = constructList(string)
        head = solution.mergeKLists(strings)
        print(reconstruct(head))