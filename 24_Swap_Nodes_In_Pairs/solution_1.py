class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        temp_head = ListNode('$')
        temp_head.next = head
        tail = temp_head

        first = tail.next
        while first:
            second = first.next
            if not second:
                return temp_head.next
            post = second.next
            tail.next = second
            second.next = first
            first.next = post
            tail = first
            first = post
        return temp_head.next


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
        "12345",
        "12345",
        "12345",
        "12345678",
        "1"
    ]

    solution = Solution()
    for linkedlist in test_cases:
        head = constructList(linkedlist)
        head = solution.swapPairs(head)
        result = reconstruct(head)
        print(result)
