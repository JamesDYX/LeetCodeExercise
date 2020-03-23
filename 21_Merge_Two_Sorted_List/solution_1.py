# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        p1 = l1
        p2 = l2
        if p1.val > p2.val:
            head = p2
            p2 = p2.next
        else:
            head = p1
            p1 = p1.next
        current = head
        while p1 and p2:
            if p1.val > p2.val:
                current.next = p2
                p2 = p2.next
            else:
                current.next = p1
                p1 = p1.next
            current = current.next
        if p1:
            current.next = p1
        else:
            current.next = p2
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
        ("124", "134"),
        ("135679", "2"),
    ]

    solution = Solution()
    for string1, string2 in test_cases:
        l1 = constructList(string1)
        l2 = constructList(string2)
        head = solution.mergeTwoLists(l1, l2)
        print(reconstruct(head))
