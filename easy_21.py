from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        head = curr = ListNode()
        while curr1 and curr2:
            if curr1.val < curr2.val:
                # print("first", curr1.val)
                curr.next = curr1
                curr1 = curr1.next
            else:
                # print("second", curr2.val)
                curr.next = curr2
                curr2 = curr2.next
            # print(curr.val)
            curr = curr.next
            # print(curr)
        else:
            if curr1:
                while curr1:
                    # print(curr1.val)
                    curr.next = curr1
                    curr1 = curr1.next
                    curr = curr.next
            else:
                while curr2:
                    # print(curr2.val)
                    curr.next = curr2
                    curr2 = curr2.next
                    curr = curr.next
        return head.next


if __name__ == '__main__':
    a11 = ListNode(1)
    a12 = ListNode(2)
    a13 = ListNode(4)
    a11.next = a12
    a12.next = a13
    a21 = ListNode(1)
    a22 = ListNode(3)
    a23 = ListNode(4)
    a21.next = a22
    a22.next = a23
    print(Solution().mergeTwoLists(a11, a21).next.next.next.val)
