class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        min_index = None
        counter = 0
        while True:
            if counter == len(lists):
                break
            elif not lists[counter]:
                lists.pop(counter)
                continue
            elif min_index is None or lists[counter].val < lists[min_index].val:
                min_index = counter
            counter += 1

        if not lists:
            return None
        p = head = lists[min_index]
        if not p.next:
            lists.pop(min_index)
        else:
            lists[min_index] = p.next

        while True:
            if not lists:
                return head
            elif len(lists) == 1:
                p.next = lists[0]
                return head
            min_index = None
            for counter, l in enumerate(lists):
                if min_index is None or l.val < lists[min_index].val:
                    min_index = counter
            p.next = lists[min_index]
            p = p.next
            if not p.next:
                lists.pop(min_index)
            else:
                lists[min_index] = p.next


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
        ["124", "134"],
        ["135679", "2"],
        ["1", "234567"],
        ['14689', '2666899999'],
        ['12345'],
        [],
        ['12345'],
    ]

    solution = Solution()
    for strings in test_cases:
        for i, string in enumerate(strings):
            strings[i] = constructList(string)
        head = solution.mergeKLists(strings)
        print(reconstruct(head))
    print(reconstruct(solution.mergeKLists([None, None, constructList("1234")])))
