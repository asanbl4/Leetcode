from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, s1 = l1, ''
        curr2, s2 = l2, ''
        while curr1:
            s1 += str(curr1.val)
            curr1 = curr1.next
        while curr2:
            s2 += str(curr2.val)
            curr2 = curr2.next
        res = str(int(s1[::-1]) + int(s2[::-1]))[::-1]
        a = [ListNode(int(i)) for i in res]
        for i in range(1, len(a)):
            a[i - 1].next = a[i]
        return a[0]

if __name__ == '__main__':
    l11 = ListNode(2)
    l12 = ListNode(4)
    l13 = ListNode(3)
    l21 = ListNode(5)
    l22 = ListNode(6)
    l23 = ListNode(4)
    l11.next = l12
    l12.next = l13
    l21.next = l22
    l22.next = l23
    print(Solution().addTwoNumbers(l11, l21).next.next.val)