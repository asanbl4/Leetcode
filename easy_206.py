from LinkedListGenerator.LinkedListGenerator import generateLinkedListFromArray
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            prevTemp = prev
            headTemp = head
            nextTemp = head.next
            # print("before:", prevTemp.val if prevTemp else 0, headTemp.val if headTemp else 0, nextTemp.val if nextTemp else 0)
            head.next = prevTemp
            prev = headTemp
            head = nextTemp
        return prev




solution = Solution()
print(solution.reverseList(generateLinkedListFromArray([1,2])))

