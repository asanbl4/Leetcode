from LinkedListGenerator.LinkedListGenerator import generateLinkedListFromArray
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        head = curr3 = ListNode()
        while curr1 or curr2:
            if curr1:
                if curr2: # general
                    if curr1.val < curr2.val:
                        # print("first", curr1.val)
                        curr3.next = curr1
                        curr1 = curr1.next
                    else:
                        # print("second", curr2.val)
                        curr3.next = curr2
                        curr2 = curr2.next
                else: # if curr2 is none
                    curr3.next = curr1
                    # print(curr3.val)
                    curr1 = curr1.next
            else: # if curr 1 is none
                curr3.next = curr2
                # print(curr3.val)
                curr2 = curr2.next
            curr3 = curr3.next
        return head.next

solution = Solution()
# print(solution.mergeTwoLists(generateLinkedListFromArray([]), generateLinkedListFromArray([])))
