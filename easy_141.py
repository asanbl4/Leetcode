from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        visited = [curr]
        while curr:
            curr = curr.next
            if curr in visited:
                return True
            visited.append(curr)
        return False


if __name__ == '__main__':
    head = ListNode(3)
    a = ListNode(2)
    b = ListNode(0)
    c = ListNode(-4)
    head.next = a
    a.next = b
    b.next = c
    c.next = a
    print(Solution().hasCycle(head))
