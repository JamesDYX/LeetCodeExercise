class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        temp_list = []
        first_list = None
        for l in lists:
            if not l:
                continue
            elif not first_list:
                first_list = l
            else:
                temp_list.append(self.merge2Lists([first_list, l]))
                first_list = None
        if first_list:
            temp_list.append(first_list)
        if not temp_list:
            return None

        lists = temp_list
        while True:
            if len(lists) == 1:
                return lists[0]
            temp_list = []
            first_list = None
            for l in lists:
                if not first_list:
                    first_list = l
                else:
                    temp_list.append(self.merge2Lists([first_list, l]))
                    first_list = None
            lists = temp_list
            if first_list:
                lists.append(first_list)

    def merge2Lists(self, listpair):
        if listpair[0].val < listpair[1].val:
            head = listpair[0]
            onlist = 0
        else:
            head = listpair[1]
            onlist = 1

        p = head
        listpair[onlist] = listpair[onlist].next
        if not listpair[onlist]:
            p.next = listpair[1-onlist]
            return head

        if listpair[0].val < listpair[1].val:
            from_node = listpair[0]
            onlist = 0
        else:
            from_node = listpair[1]
            onlist = 1
        while True:
            to_node = from_node
            while to_node.next and to_node.next.val <= listpair[1-onlist].val:
                to_node = to_node.next
            p.next = from_node
            p = to_node
            if not p.next:
                p.next = listpair[1-onlist]
                return head
            listpair[onlist] = to_node.next
            onlist = 1 - onlist
            from_node = listpair[onlist]


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