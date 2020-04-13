class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_list = None
        current = result_list
        digit_1 = l1
        digit_2 = l2
        c = 0
        while digit_1 is not None and digit_2 is not None:
            sum = digit_1.val + digit_2.val + c
            digit_val = sum % 10
            c = int(sum/10)
            digit = ListNode(digit_val)
            if result_list is None:
                result_list = digit
            else:
                current.next = digit
            current = digit
            digit_1 = digit_1.next
            digit_2 = digit_2.next

        remain_digit = digit_1
        if digit_2 is not None:
            remain_digit = digit_2
        while c == 1 and remain_digit is not None:
            sum = remain_digit.val + c
            digit_val = sum % 10
            c = int(sum / 10)
            digit = ListNode(digit_val)
            current.next = digit
            current = digit
            remain_digit = remain_digit.next

        if c == 1:
            current.next = ListNode(1)
        else:
            current.next = remain_digit

        return result_list


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
    return string[::-1]


if __name__ == '__main__':
    test_cases = [
        ('342', '456'),
        ('0', '0'),
        ('9999999', '1'),
        ('9999999', '0'),
    ]

    solution = Solution()
    for (a, b) in test_cases:
        l1 = constructList(a[::-1])
        l2 = constructList(b[::-1])
        result = solution.addTwoNumbers(l1=l1, l2=l2)
        output = reconstruct(result)
        print(output)
