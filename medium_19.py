from typing import Optional
from LinkedListGenerator.LinkedListGenerator import generateLinkedListFromArray

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        i = 0
        curr2 = head2 = head
        while i < size - n - 1:
            i += 1
            curr2 = curr2.next
        else:
            if size == n:
                head2 = head2.next
            if curr2.next:
                curr2.next = curr2.next.next
            else:
                curr2.next = None
        return head2

sol = Solution()
print(sol.removeNthFromEnd(generateLinkedListFromArray([1,2,3,4,5]),1))

