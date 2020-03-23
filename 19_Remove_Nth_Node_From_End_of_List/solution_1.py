# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not n:
            return head
        preNode = None
        currentNode = head
        for i in range(n):
            currentNode = currentNode.next

        removeNode = head
        while currentNode:
            currentNode = currentNode.next
            preNode = removeNode
            removeNode = removeNode.next

        if preNode:
            preNode.next = removeNode.next
            return head
        else:
            return head.next


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
        ("12345", 2),
        ("12345", 1),
        ("12345", 5),
        ("1", 1),
        ("1", 0),
    ]

    solution = Solution()
    for string, n in test_cases:
        print(reconstruct(solution.removeNthFromEnd(constructList(string), n)))