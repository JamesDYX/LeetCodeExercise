class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        temp_head = ListNode('$')
        temp_head.next = head
        p = temp_head
        from_node = to_node = p.next

        while True:
            counter = 0
            while counter < k and to_node:
                to_node = to_node.next
                counter += 1
            if counter < k:
                return temp_head.next

            q = from_node
            pre_q = p
            counter = 0
            while counter < k:
                post_q = q.next
                q.next = pre_q
                pre_q = q
                q = post_q
                counter += 1

            from_node.next = q
            p.next = pre_q
            p = from_node

            if not p.next:
                return temp_head.next
            from_node = to_node = p.next


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
        ("12345", 3),
        ("12345", 1),
        ("12345678", 3),
    ]

    solution = Solution()
    for linkedlist, k in test_cases:
        head = constructList(linkedlist)
        head = solution.reverseKGroup(head, k)
        result = reconstruct(head)
        print(result)


